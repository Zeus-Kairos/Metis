import json
from dataclasses import dataclass
from typing import List
import os

@dataclass
class KnowledgeBaseItem:
    """
    Represents an item in the knowledge base index.
    """
    id: int
    name: str
    path: str
    description: str

class KnowledgeBaseReader:
    """
    Reader for the knowledge base index file.
    """
    
    def __init__(self, index_path: str = "Docs/knowledge_base_index.json"):
        """
        Initialize the knowledge base reader.
        
        Args:
            index_path: Path to the knowledge base index JSON file.
        """
        self.index_path = os.path.abspath(index_path)
        self.knowledge_base_items = self._read_knowledge_base_index()

    def get_knowledge_base_item(self, item_id: int) -> KnowledgeBaseItem:
        """
        Get a knowledge base item by its ID.
        
        Args:
            item_id: ID of the knowledge base item to retrieve.
            
        Returns:
            The KnowledgeBaseItem object with the specified ID.
            
        Raises:
            ValueError: If no item with the specified ID is found.
        """
        for item in self.knowledge_base_items:
            if item.id == item_id:
                return item
        raise ValueError(f"Knowledge base item with ID {item_id} not found.")
    
    def get_all_knowledge_base_items(self) -> List[KnowledgeBaseItem]:
        """
        Get all knowledge base items.
        
        Returns:
            List of all KnowledgeBaseItem objects in the index.
        """
        return self.knowledge_base_items
    
    def _read_knowledge_base_index(self) -> List[KnowledgeBaseItem]:
        """
        Read the knowledge base index JSON file into a list of KnowledgeBaseItem objects.
        
        Returns:
            List of KnowledgeBaseItem objects parsed from the JSON file.
            
        Raises:
            FileNotFoundError: If the knowledge base index file is not found.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(self.index_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                
            # Convert the list of dictionaries to a list of KnowledgeBaseItem objects
            items = []
            for item_dict in data:
                item = KnowledgeBaseItem(
                    id=item_dict.get('id'),
                    name=item_dict.get('name'),
                    path=item_dict.get('path'),
                    description=item_dict.get('description')
                )
                items.append(item)
            
            return items
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Knowledge base index file not found: {self.index_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in knowledge base index file: {e.msg}", e.doc, e.pos)