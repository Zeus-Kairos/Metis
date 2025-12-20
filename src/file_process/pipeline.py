import os
from typing import List, Dict, Any
from fastapi import UploadFile
from src.file_process.indexer import Indexer
from src.file_process.file_splitter import FileSplitter
from src.file_process.file_upload import FileUploader
from src.file_process.file_parser import FileParser, PARSABLE_FORMATS
from src.utils.logging_config import get_logger

logger = get_logger(__name__)

class FileProcessingPipeline:
    """Pipeline that orchestrates file upload and parsing using separate components."""
    
    def __init__(self):
        self.file_uploader = FileUploader()
        self.file_parser = FileParser()
        self.file_splitter = FileSplitter()
    
    async def process_files(self, user_id: int, knowledge_base: str, files: List[UploadFile], directory: str = "") -> Dict[str, Any]:
        """Process files through the complete pipeline: upload -> parse.
        
        Args:
            user_id: User ID for the upload
            knowledge_base: Knowledge base name
            files: List of UploadFile objects
            directory: Directory to store files (optional, defaults to empty string)
            
        Returns:
            Dict containing complete processing results
        """
        logger.info(f"Starting file processing pipeline: user_id={user_id}, knowledge_base={knowledge_base}, directory={directory}, file_count={len(files)}")
        
        # Step 1: Upload files
        upload_results = await self.file_uploader.upload_files(user_id, knowledge_base, files, directory)
        
        # Step 2: Parse successful uploads and split parsed content
        all_documents = {}
        for file_result in upload_results["files"]:
            if file_result["status"] not in ["success", "updated"]:
                continue
            
            file_path = file_result["path"]
            filename = file_result["filename"]
            file_id = file_result["file_id"]
            
            # Check if file is parsable
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in PARSABLE_FORMATS:
                parse_result = self.file_parser.parse_file(file_path, save=True)
                if parse_result["success"]:
                    file_result["parsed"] = True
                    file_result["parsed_path"] = parse_result["parsed_file"]
                    logger.info(f"File parsed successfully: {filename} -> {parse_result['parsed_file']}")

                    # Step 3: Split parsed content
                    content = parse_result["content"]
                    metadata = {
                        "file_id": file_id,
                        "filename": filename,
                        'file_path': file_path,
                    }
                    documents = self.file_splitter.split_text(content, metadata)
                    all_documents[file_id] = documents
                    logger.info(f"File split into {len(documents)} documents: {filename}")
                else:
                    file_result["parsed"] = False
                    file_result["parsing_error"] = parse_result["error"]
                    logger.error(f"Failed to parse content for {filename}: {parse_result['error']}")
            else:
                file_result["parsed"] = False
                file_result["parsing_error"] = "File type not parsable"

        # Step 4: Index chunks
        self.indexer = Indexer(f"./index/{user_id}/{knowledge_base}")
        vectorstore = self.indexer.index_chunks(all_documents)
        
        # Calculate parsing metrics
        total_parsed = sum(1 for r in upload_results["files"] if r["status"] in ["success", "updated"] and r.get("parsed", False))
        failed_parsing = sum(1 for r in upload_results["files"] if r["status"] in ["success", "updated"] and not r.get("parsed", False))
        
        # Determine overall status
        all_successful = upload_results["successful"] == len(files) and upload_results["status"] == "success"
        overall_status = "success" if all_successful else "partial_success"
        
        total_chunks = {"total": sum(len(docs) for docs in all_documents.values())}
        total_chunks.update({file_id: len(docs) for file_id,docs in all_documents.items()})
        
        final_result = {
            "status": overall_status,
            "files": upload_results["files"],
            "total": upload_results["total"],
            "successful": upload_results["successful"],
            "skipped": upload_results["skipped"],
            "failed": upload_results["failed"],
            "parsing": {
                "total_parsed": total_parsed,
                "failed_parsing": failed_parsing,
            },
            "total_chunks": total_chunks,
            "knowledge_base": knowledge_base,
            "user_id": user_id,
        }
        
        logger.info(f"Pipeline completed: {final_result['status']}, total={final_result['total']}, successful={final_result['successful']}, parsed={final_result['parsing']['total_parsed']}, total_chunks={final_result['total_chunks']}")
        
        return final_result




