import os
import hashlib
from typing import List
from fastapi import UploadFile, HTTPException
from src.utils.logging_config import get_logger

logger = get_logger(__name__)

# Define supported file formats
SUPPORTED_FORMATS = {
    ".txt",
    ".pdf",
    ".md",
    ".docx",
    ".pptx",
    ".xlsx",
    ".html",
    ".csv"
}

# Define maximum file size (100MB)
MAX_FILE_SIZE = 100 * 1024 * 1024

MAX_FILES_PER_UPLOAD = 20

async def handle_file_upload(user_id: str, knowledge_base: str, files: List[UploadFile]):
    """
    Handle file uploads with validation, existence checking, and storage.
    
    Args:
        user_id: User ID for the upload
        knowledge_base: Knowledge base name
        files: List of UploadFile objects
        
    Returns:
        Dictionary with upload results
    """
    # Validate user_id and knowledge_base
    if not user_id or not knowledge_base:
        raise HTTPException(status_code=400, detail="Missing required parameters: user_id and knowledge_base")
    
    # Validate file count
    if not files or len(files) == 0:
        raise HTTPException(status_code=400, detail="No files provided")
    
    if len(files) > MAX_FILES_PER_UPLOAD:
        raise HTTPException(status_code=400, detail=f"Maximum {MAX_FILES_PER_UPLOAD} files allowed per upload")
    
    # Create upload directory structure
    upload_dir = os.path.join("uploads", user_id, knowledge_base, "origin")
    os.makedirs(upload_dir, exist_ok=True)
    
    # Process each file
    upload_results = []
    all_successful = True
    
    for file in files:
        try:
            # Get file extension and validate format
            file_ext = os.path.splitext(file.filename)[1].lower()
            if file_ext not in SUPPORTED_FORMATS:
                upload_results.append({
                    "filename": file.filename,
                    "status": "failed",
                    "error": f"Unsupported file format: {file_ext}. Supported formats: {', '.join(SUPPORTED_FORMATS)}"
                })
                all_successful = False
                continue
            
            # Read file content
            content = await file.read()
            
            # Check file size
            if len(content) > MAX_FILE_SIZE:
                upload_results.append({
                    "filename": file.filename,
                    "status": "failed",
                    "error": f"File size exceeds maximum limit (100MB)"
                })
                all_successful = False
                continue
            
            # Check if file already exists based on content hash
            file_hash = hashlib.md5(content).hexdigest()
            existing_files = os.listdir(upload_dir)
            
            file_exists = False
            for existing_file in existing_files:
                existing_path = os.path.join(upload_dir, existing_file)
                if os.path.isfile(existing_path):
                    with open(existing_path, "rb") as f:
                        existing_hash = hashlib.md5(f.read()).hexdigest()
                    if existing_hash == file_hash:
                        file_exists = True
                        break
            
            if file_exists:
                # Keep existing file, return message
                upload_results.append({
                    "filename": file.filename,
                    "status": "skipped",
                    "message": "File already exists with identical content"
                })
                continue
            
            # Save new file
            file_path = os.path.join(upload_dir, file.filename)
            
            # Handle filename collisions by appending number if needed
            counter = 1
            base_filename, ext = os.path.splitext(file.filename)
            while os.path.exists(file_path):
                new_filename = f"{base_filename}_{counter}{ext}"
                file_path = os.path.join(upload_dir, new_filename)
                counter += 1
            
            with open(file_path, "wb") as f:
                f.write(content)
            
            # Log successful upload
            logger.info(f"File uploaded successfully: {file.filename} -> {file_path}")
            
            # Add to results
            upload_results.append({
                "filename": file.filename,
                "status": "success",
                "path": file_path
            })
            
        except Exception as e:
            logger.error(f"Error processing file {file.filename}: {str(e)}")
            upload_results.append({
                "filename": file.filename,
                "status": "failed",
                "error": str(e)
            })
            all_successful = False
    
    # Determine overall status
    overall_status = "success" if all_successful else "partial_success"
    
    return {
        "status": overall_status,
        "files": upload_results,
        "total": len(files),
        "successful": sum(1 for r in upload_results if r["status"] == "success"),
        "skipped": sum(1 for r in upload_results if r["status"] == "skipped"),
        "failed": sum(1 for r in upload_results if r["status"] == "failed")
    }