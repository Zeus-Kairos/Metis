from dataclasses import dataclass


@dataclass
class KnowledgeBaseItem:
    """
    Represents an item in the knowledge base index.
    """
    id: int
    name: str
    root_path: str
    index_path: str
    description: str