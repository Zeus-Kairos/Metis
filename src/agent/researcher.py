import operator
from typing import Annotated, Dict, List, TypedDict

from langchain_core.documents import Document
from langchain_core.messages import AIMessage, SystemMessage
from langgraph.graph import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from src.agent.types import KnowledgeBaseItem
from src.agent.prompts import deep_search_prompt
from src.agent.tools import list_children_tool, rag_search_tool
from src.utils.logging_config import get_logger


logger = get_logger(__name__)

MAX_RETRIEVE_TRIES = 3

class ResearcherState(TypedDict):
    """
    State of the researcher.
    """
    aspect: str
    knowledge_base_item: KnowledgeBaseItem
    messages: Annotated[List[Dict[str, str]], add_messages]
    documents: list[Document] = []
    answer: str = ""
    is_done: bool = False
    searched_path: Dict[str, set[str]] = {}
    retrieve_tries: int = 0

class Researcher:
    def __init__(self, llm_runner):
        self.llm_runner = llm_runner
        self.graph = self._create_graph()

    def _research(self, state: ResearcherState) -> ResearcherState:
        """
        Research the aspect.
        """
        is_done = state["is_done"] if "is_done" in state else False
        retrieve_tries = state["retrieve_tries"] if "retrieve_tries" in state else 0
        logger.info(f"[research] aspect: {state['aspect']}, retrieve_tries: {retrieve_tries}")
        if is_done or retrieve_tries >= MAX_RETRIEVE_TRIES:
            return {
                "retrieve_tries": 0,
                "messages": [AIMessage(content="Max retrieve tries reached")],
            }

        system_prompt = deep_search_prompt(state)
        response = self.llm_runner.invoke([SystemMessage(content=system_prompt)], [list_children_tool, rag_search_tool])    
        if response.content.strip():
            logger.info(f"[deep_search] Response: {response.content.strip()}")
        return {
            "messages": [response],
        }

    def _create_graph(self):
        """
        Create the graph for the researcher.
        """
        graph = StateGraph(ResearcherState)
        graph.add_node("research", self._research)
        graph.add_node("deep_retrieve", ToolNode([list_children_tool, rag_search_tool]))

        graph.add_edge(START, "research")
        graph.add_conditional_edges(
            "research",
            tools_condition,
            {
                "tools": "deep_retrieve",
                "__end__": END,
            },
        )  
        graph.add_edge("deep_retrieve", "research")

        return graph.compile()


