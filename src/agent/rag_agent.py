import json
import os
import re
from datetime import datetime, timezone
from typing import Any, Dict, Generator, List

from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.types import Send

from src.agent.types import KnowledgeBaseItem
from src.memory.memory import MemoryManager 
from src.memory.thread import ThreadManager
from src.agent.prompts import (
    classify_intent_prompt,
    filter_documents_prompt,
    find_relative_aspects_prompt,
    format_answer_prompt,
    handle_chat_prompt,
    plan_rag_prompt,
    refine_query_prompt,
    reference_check_prompt,
    review_answer_prompt,
    synthesize_answer_prompt,
)
from src.rag.rag_flow import RAGFlow, RAGType
from src.utils.paths import get_index_path, get_upload_dir
from src.utils.logging_config import get_logger
from src.utils.merger import merge_documents
from src.agent.types import RAGResult, AgentState, DeepRAGState, DeepSearchState
from src.utils.embeddings import get_embedding_runner

logger = get_logger(__name__)

class RAGAgent:
    def __init__(self, thread_manager: ThreadManager = None, user_id: int = None, on_langgraph_server: bool = False):
        """
        Initialize the agent.
        
        Args:
            thread_manager: Thread manager instance
            user_id: User ID to use for API configuration
            on_langgraph_server: Whether running on LangGraph server
        """
        try:
            rag_type_str = os.getenv("RAG_TYPE", "simple").lower()
            rag_type = RAGType(rag_type_str)
        except ValueError:
            rag_type = RAGType.SIMPLE        
        self.rag_type = rag_type    
        self.rag_k = int(os.getenv("RAG_K", 10))      
        
        self.user_id = user_id
        self.llm_runner = None
        self.embedding_runner = None
        self.thread_manager = thread_manager
        self.knowledgebase_id = 0
        self.knowledgebase_item = None
        self.on_langgraph_server = on_langgraph_server
        self.conn_str = os.getenv("DB_URI")
        if self.conn_str:
            with PostgresSaver.from_conn_string(self.conn_str) as checkpointer: 
                checkpointer.setup()
        self.builder = self._build_graph()

        self.update_dict = {
            "classify_intent": "User intent classified",
            "handle_rag": "Retrieved documents from knowledge base.",
            "filter_documents": "Filtered documents.",
            "deep_retrieve": "Retrieved addtional documents from knowledge base.",
            "filter_additional_documents": "Filtered additional documents.",
            "complement_answer": "Complemented the answer with additional documents.",
        }

    def _get_llm_runner(self):
        """Lazily create the LLM runner to avoid heavy imports on non-chat endpoints."""
        if self.llm_runner is None:
            if self.user_id:
                from src.agent.api_llm import get_api_llm_runner
                self.llm_runner = get_api_llm_runner(self.user_id)
            else:
                from src.agent.llm import LLMRunner
                self.llm_runner = LLMRunner()
        return self.llm_runner

    def _event(self, stage: str, detail: Dict[str, Any] | None = None) -> Dict[str, Any]:
        payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "stage": stage,
        }
        if detail:
            payload.update(detail)
        return payload

    def _build_graph(self):
        """
        Build the graph for the agent.
        """
        builder = self._build_base_graph()
        return builder

    def _classify_intent(self, state: AgentState) -> AgentState:
        """
        Classify the intent of the user query.
        """     

        prompt = classify_intent_prompt(state)

        response = self._get_llm_runner().invoke([SystemMessage(content=prompt)])
        intent = response.content.strip().lower()
        if intent not in ["rag", "chat"]:
            intent = "chat"

        # For debugging with LangGraph server
        if self.on_langgraph_server:
            return {
                "intent": intent,
                "messages": [{"role": "user", "content": state["query"]}],
                "knowledge_base_item": self.get_knowledgebase_item(self.user_id, 31),
                "agent_events": [self._event("classify_intent", {"intent": intent})],
            }
            
        return {
            "intent": intent,
            "agent_events": [self._event("classify_intent", {"intent": intent})],
        }

    def _handle_chat(self, state: AgentState) -> AgentState:
        """
        Handle the chat.
        """
        system_prompt = handle_chat_prompt(state)

        response = self._get_llm_runner().invoke([SystemMessage(content=system_prompt)])

        return {
            "messages": [response],
            "agent_events": [self._event("handle_chat")],
        }
    
    def _refine_query(self, state: AgentState) -> AgentState:
        """
        Refine the query.
        """
        if self.rag_type == RAGType.SIMPLE:
            refined_query = state["query"]
        else:
            prompt = refine_query_prompt(state)
            response = self._get_llm_runner().invoke([SystemMessage(content=prompt)])
            refined_query = response.content.strip()
        return {
            "refined_query": refined_query,
            "display": f"{refined_query}\n",
            "agent_events": [self._event("refine_query", {"refined_query": refined_query})],
        }

    def _handle_rag(self, state: AgentState) -> AgentState:
        """
        Handle the RAG.
        """
        refined_query = state["refined_query"]
        if self.embedding_runner is None and self.user_id is not None:
            self.embedding_runner = get_embedding_runner(self.user_id)
            
        rag_flow = RAGFlow(state["knowledge_base_item"].index_path, embedding_runner=self.embedding_runner)
        results = rag_flow.retrieve(self.rag_type, refined_query, k=self.rag_k)
        return {
            "documents": results,
            "agent_events": [self._event("handle_rag", {"retrieved_count": len(results)})],
        }

    def _filter_documents(self, state: AgentState) -> AgentState:
        """
        Filter the documents.
        """
        documents = state["documents"]
        if self.rag_type == RAGType.SIMPLE:
            return {
                "documents": documents,
                "agent_events": [self._event("filter_documents", {"selected_count": len(documents)})],
            }
        else:
            query = state["refined_query"]
            documents = state["documents"]          
            prompt = filter_documents_prompt(query, documents)
            response = self._get_llm_runner().invoke([SystemMessage(content=prompt)])
            try:
                filtered_document_indices = list(map(int, response.content.strip().split(",")))
            except ValueError:
                filtered_document_indices = list(range(len(documents)))
            return {
                "documents": [documents[i] for i in filtered_document_indices],
                "agent_events": [self._event("filter_documents", {"selected_count": len(filtered_document_indices)})],
            }

    def _format_answer(self, state: AgentState) -> AgentState:
        """
        Format the answer.
        """
        prompt = format_answer_prompt(state)
        response = self._get_llm_runner().invoke([SystemMessage(content=prompt)])
        
        return {
            "answer": response.content.strip(),
            "messages": [response],
            "agent_events": [self._event("format_answer", {"answer_length": len(response.content.strip())})],
        }

    def _plan_rag(self, state: DeepRAGState) -> AgentState:
        """
        Plan the RAG.
        """
        prompt = plan_rag_prompt(state)
        response = self._get_llm_runner().invoke([SystemMessage(content=prompt)])
        try:
            # use regex to extract the JSON array
            match = re.search(r"\[.*\]", response.content.strip().lower(), re.DOTALL)
            if match:
                aspects_to_explore = json.loads(match.group(0))
            else:
                aspects_to_explore = []
        except (json.JSONDecodeError, AttributeError):
            aspects_to_explore = []
        return {
            "aspects_to_explore": aspects_to_explore,
            "display": f"\nExplore aspects:\n{"\n".join(aspects_to_explore)}\n",
            "agent_events": [self._event("plan_rag", {"aspect_count": len(aspects_to_explore)})],
        }
    
    def _find_reused_aspects(self, state: DeepRAGState) -> DeepRAGState:
        """
        Find the reused aspects.
        """
        related_aspect_indices = []
        if "searched_aspects" in state and len(state["searched_aspects"]) > 0:
            searched_aspects = state["searched_aspects"]
            prompt = find_relative_aspects_prompt(state)
            response = self._get_llm_runner().invoke([SystemMessage(content=prompt)])
            try:
                related_aspect_indices = list(map(int, response.content.strip().split(",")))
                reused_aspects = [searched_aspects[index].aspect for index in related_aspect_indices]
            except ValueError:
                reused_aspects = []
            return {
                "reused_aspects": reused_aspects,
            }

        return {
            "searched_aspects": [],
        }

    def _collect_plan(self, state: DeepRAGState) -> DeepRAGState:
        """
        Collect the plan.
        """
        aspects_to_explore = state["aspects_to_explore"]
        reused_aspects = state["reused_aspects"] if "reused_aspects" in state else []
        return {
            "aspects_to_explore": [aspect for aspect in aspects_to_explore if aspect not in reused_aspects],
        }

    # Conditional edge function to create llm_call workers that each write a section of the report
    def _assign_researchers(self, state: DeepRAGState):
        """Assign a researcher to each aspect in the plan"""

        # Kick off section writing in parallel via Send() API
        return [Send("deep_search", {
                        "aspect": aspect, 
                        "knowledge_base_item": state["knowledge_base_item"],
                        }) 
            for aspect in state["aspects_to_explore"]]

    def _deep_search(self, state: DeepSearchState) -> DeepRAGState:
        """
        Handle the deep search.
        """
        from src.agent.researcher import Researcher

        aspect = state["aspect"]
        knowledgebase_item = state["knowledge_base_item"]
        researcher = Researcher(self._get_llm_runner())
        output = researcher.graph.invoke(
            {
            "aspect": aspect,
            "knowledge_base_item": knowledgebase_item,
            },
            config={"recursion_limit": 50},
        )
        result = RAGResult(
            aspect=aspect,
            documents=output["documents"] if "documents" in output else [],
            answer=output["answer"] if "answer" in output else "",
            is_done=output["is_done"] if "is_done" in output else False,
        )

        return {
            "searched_aspects": [result],
            "agent_events": [self._event("deep_search", {"aspect": aspect, "doc_count": len(result.documents), "is_done": result.is_done})],
        }

    def _synthesize_answer(self, state: DeepRAGState) -> DeepRAGState:
        """
        Synthesize the answer.
        """   
        searched_aspects = state["searched_aspects"]
        aspects_to_explore = state["aspects_to_explore"]
        reused_aspects = state["reused_aspects"] if "reused_aspects" in state else []
        related_aspects = aspects_to_explore + reused_aspects
        logger.info(f"[synthesize_answer] Related aspects: {related_aspects}")

        useful_aspects = [aspect for aspect in searched_aspects if aspect.aspect in related_aspects]

        all_docs = [doc for aspect in useful_aspects for doc in aspect.documents]
        documents = merge_documents(all_docs)      
        
        query = state["refined_query"]
        prompt = synthesize_answer_prompt(query, useful_aspects)
        response = self._get_llm_runner().invoke([SystemMessage(content=prompt)])
        return {
            "documents": documents,
            "answer": response.content.strip(),
            "display": f"\n{response.content.strip()}\n",
            "agent_events": [self._event("synthesize_answer", {"doc_count": len(documents)})],
        }


    # def _deep_rag(self, state: DeepRAGState) -> DeepRAGState:
    #     """
    #     Handle the deep RAG.
    #     """
    #     new_aspects_to_explore = state["new_aspects_to_explore"]
    #     if all(aspect["status"] == "done" for aspect in new_aspects_to_explore):
    #         return { "messages": AIMessage(content="end")}

    #     prompt = deep_rag_prompt(state)
    #     response = self.llm_runner.invoke([SystemMessage(content=prompt)], [list_children_tool, rag_search_tool])
    #     if response.content.strip():
    #         logger.info(f"[deep_rag] Response: {response.content.strip()}")
    #     return {
    #         "messages": [response],
    #     }

    def _reference_check(self, state: DeepRAGState) -> DeepRAGState:
        """
        Check the reference.
        """       
        root_path = get_upload_dir(self.user_id, state["knowledge_base_item"].name, "")
        prompt = reference_check_prompt(state, root_path)
        response = self._get_llm_runner().invoke([SystemMessage(content=prompt)])
        return {
            "answer": response.content.strip(),
            "messages": [response],
            "agent_events": [self._event("reference_check", {"answer_length": len(response.content.strip())})],
        }

    def _build_base_graph(self) -> StateGraph:
        """
        Build the base graph for the agent.
        """
        if self.rag_type == RAGType.AGENTIC:
            graph = StateGraph(DeepRAGState)
        else:
            graph = StateGraph(AgentState)  

        graph.add_node("classify_intent", self._classify_intent)
        graph.add_node("refine_query", self._refine_query)
        graph.add_node("handle_chat", self._handle_chat)
        if self.rag_type == RAGType.AGENTIC:
            graph.add_node("plan_rag", self._plan_rag)
            graph.add_node("find_reused_aspects", self._find_reused_aspects)
            graph.add_node("collect_plan", self._collect_plan)
            graph.add_node("deep_search", self._deep_search)       
            graph.add_node("synthesize_answer", self._synthesize_answer)
            graph.add_node("reference_check", self._reference_check)
        else:
            graph.add_node("handle_rag", self._handle_rag)
            graph.add_node("filter_documents", self._filter_documents)
            graph.add_node("format_answer", self._format_answer)

        graph.add_edge(START, "classify_intent")
        graph.add_conditional_edges(
            "classify_intent",
            lambda state: state["intent"],
            {
                "rag": "refine_query",
                "chat": "handle_chat",
            }
        )
        graph.add_edge("handle_chat", END)
        if self.rag_type == RAGType.AGENTIC:
            graph.add_edge("refine_query", "plan_rag")
            graph.add_edge("refine_query", "find_reused_aspects")
            graph.add_edge("plan_rag", "collect_plan")
            graph.add_edge("find_reused_aspects", "collect_plan")
            graph.add_conditional_edges(
                "collect_plan", self._assign_researchers, ["deep_search"]
            )
            graph.add_edge("deep_search", "synthesize_answer")            
            graph.add_edge("synthesize_answer", "reference_check")
            graph.add_edge("reference_check", END)
        else:
            graph.add_edge("refine_query", "handle_rag")
            graph.add_edge("handle_rag", "filter_documents")
            graph.add_edge("filter_documents", "format_answer")
            graph.add_edge("format_answer", END)     

        return graph

    def get_conversation_history(self, user_id: int, thread_id: str) -> List[Dict[str, Any]]:
        """
        Get the conversation history for a user and thread.
        """
        if self.conn_str:
            with PostgresSaver.from_conn_string(self.conn_str) as checkpointer: 
                graph = self.builder.compile(checkpointer=checkpointer)
                return self.thread_manager.get_conversation_history(user_id, thread_id, graph)
        else:      
            graph = self.builder.compile(checkpointer=InMemorySaver())
            return self.thread_manager.get_conversation_history(user_id, thread_id, graph)

    def delete_thread(self, thread_id: str) -> None:
        """
        Delete the conversation history for a user and thread.
        """
        if self.conn_str:
            with PostgresSaver.from_conn_string(self.conn_str) as checkpointer: 
                checkpointer.delete_thread(thread_id)
        else:      
            checkpointer=InMemorySaver()
            checkpointer.delete_thread(thread_id)
    
    def chat(self, query: str, user_id: int, knowledge_base_id: int, config: Dict[str, Any] = None) -> Generator[Dict[str, Any], None, None]:
        """
        Chat with the agent.
        """

        knowledgebase_item = self.get_knowledgebase_item(user_id, knowledge_base_id)

        logger.info(f"Chat with Knowledgebase: {knowledgebase_item.name}")

        initial_state = {
            "query": query,
            "messages": [{"role": "user", "content": query}],
            "knowledge_base_item": knowledgebase_item,
        }
        final_trace_payload = {
            "run_id": config.get("run_id") if config else None,
            "user_id": user_id,
            "thread_id": config.get("configurable", {}).get("thread_id") if config else None,
            "knowledgebase_id": knowledge_base_id,
            "knowledgebase_name": knowledgebase_item.name,
            "rag_type": self.rag_type.value,
            "query": query,
            "refined_query": query,
            "retrieval": [],
            "final_answer": "",
            "reference_annotated_answer": "",
            "agent_events": [],
        }

        if self.conn_str:
            with PostgresSaver.from_conn_string(self.conn_str) as checkpointer: 
                graph = self.builder.compile(checkpointer=checkpointer)
                # Streaming mode: yield chunks as they become available          
                for subgraph, mode, chunk in graph.stream(initial_state, 
                                                config=config, 
                                                subgraphs=True,
                                                stream_mode=["updates", "messages"]):                   
                    if mode == "updates":
                        for node, state in chunk.items():
                            if state and "display" in state and state["display"]:
                                yield { "display": state["display"] }
                            if state:
                                if "refined_query" in state and state["refined_query"]:
                                    final_trace_payload["refined_query"] = state["refined_query"]
                                if "documents" in state and state["documents"]:
                                    final_trace_payload["retrieval"] = state["documents"]
                                if "answer" in state and state["answer"]:
                                    final_trace_payload["final_answer"] = state["answer"]
                                    if node == "reference_check":
                                        final_trace_payload["reference_annotated_answer"] = state["answer"]
                                if "agent_events" in state and state["agent_events"]:
                                    final_trace_payload["agent_events"] = state["agent_events"]

                    elif mode == "messages":
                        message, meta = chunk
                        if message.content and meta["langgraph_node"] in ["handle_chat", "format_answer", "deep_retrieve", "synthesize_answer", "reference_check"]:
                            last_assistant_message = message.content   
                            # if subgraph:
                            #     logger.info(f"{subgraph}: {message}: {meta}")
                            if meta["langgraph_node"] in ["deep_retrieve", "synthesize_answer"]:
                                yield {
                                    "display": last_assistant_message,
                                }
                            else:
                                yield {
                                    "response": last_assistant_message,
                                }
                if not final_trace_payload.get("final_answer"):
                    final_trace_payload["final_answer"] = last_assistant_message if "last_assistant_message" in locals() else ""
                yield {"trace_payload": final_trace_payload}
                yield { "run_id": config["run_id"] }
        else:
            graph = self.builder.compile(checkpointer=InMemorySaver())
            
            # Streaming mode: yield chunks as they become available                
            for subgraph, mode, chunk in graph.stream(initial_state, 
                                            config=config, 
                                            subgraphs=True,
                                            stream_mode=["updates", "messages"]):                   
                if mode == "updates":
                    for node, state in chunk.items():
                        if "display" in state and state["display"]:
                            yield { "display": state["display"] }
                        if "refined_query" in state and state["refined_query"]:
                            final_trace_payload["refined_query"] = state["refined_query"]
                        if "documents" in state and state["documents"]:
                            final_trace_payload["retrieval"] = state["documents"]
                        if "answer" in state and state["answer"]:
                            final_trace_payload["final_answer"] = state["answer"]
                            if node == "reference_check":
                                final_trace_payload["reference_annotated_answer"] = state["answer"]
                        if "agent_events" in state and state["agent_events"]:
                            final_trace_payload["agent_events"] = state["agent_events"]
                    logger.info(f"subgraph: {subgraph}")
                elif mode == "messages":
                    message, meta = chunk
                    if message.content and meta["langgraph_node"] in ["handle_chat", "format_answer", "deep_retrieve", "synthesize_answer", "reference_check"]:
                        last_assistant_message = message.content   
                        # if subgraph:
                        #     logger.info(f"{subgraph}: {message}: {meta}")
                        if meta["langgraph_node"] in ["deep_retrieve", "synthesize_answer"]:
                            yield {
                                "display": last_assistant_message,
                            }
                        else:
                            yield {
                                "response": last_assistant_message,
                            }
            if not final_trace_payload.get("final_answer"):
                final_trace_payload["final_answer"] = last_assistant_message if "last_assistant_message" in locals() else ""
            yield {"trace_payload": final_trace_payload}
            yield { "run_id": config["run_id"] }
    
    def get_knowledgebase_item(self, user_id: int, knowledgebase_id: int) -> KnowledgeBaseItem:
        """
        Get the knowledge base item.
        """
        if knowledgebase_id == self.knowledgebase_id:
            return self.knowledgebase_item

        knowledgebase_manager = MemoryManager().knowledgebase_manager
        knowledgebase = knowledgebase_manager.get_knowledgebase(knowledgebase_id)
        knowledgebase_name = knowledgebase["name"]
        root_path = get_upload_dir(user_id, knowledgebase_name, "")
        index_path = get_index_path(user_id, knowledgebase_name)

        knowledgebase_item = KnowledgeBaseItem(
            id=knowledgebase_id,
            name=knowledgebase_name,
            root_path=root_path,
            index_path=index_path,
            description=knowledgebase["description"],
        )        

        self.knowledgebase_id = knowledgebase_id
        self.knowledgebase_item = knowledgebase_item

        return knowledgebase_item
        
