import uuid

def get_file_id(file_path: str) -> str:
    """Generate a unique file_id for the given filename.
    
    Args:
        file_path: Path of the file
        
    Returns:
        Unique file_id as a string
    """
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, file_path))
