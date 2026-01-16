from typing import List

from langchain_core.messages import BaseMessage


def format_messages(messages: List[BaseMessage]) -> List[str]:
    """Format a list of BaseMessage objects into a list of strings.
    
    Args:
        messages: List of BaseMessage objects
        
    Returns:
        List of formatted message strings
    """
    formatted_messages = []
    for message in messages:
        message_type = type(message).__name__
        if message_type == "HumanMessage":
            formatted_messages.append(f"User: {message.content}")
        elif message_type == "AIMessage":
            formatted_message = "Assistant:"
            if message.content:
                formatted_message += message.content
            if hasattr(message, "tool_calls") and message.tool_calls:
                formatted_message += f" Tool Calls: {message.tool_calls}"
            formatted_messages.append(formatted_message)    
        elif message_type == "ToolMessage":
            formatted_messages.append(f"Tool: {message}")
        else:
            formatted_messages.append(message.content)
    return formatted_messages