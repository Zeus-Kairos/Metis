import os
import asyncio
import shutil
from typing import List, Dict, Any, Optional, Tuple
from markitdown import MarkItDown
import html2text
import pymupdf.layout
import pymupdf4llm
import logging

from src.utils.logging_config import get_logger

logger = get_logger(__name__)

# Define supported file formats for parsing
PARSABLE_FORMATS = {'.txt', '.md', '.html', '.htm', '.pdf', '.docx', '.pptx', '.xlsx', '.html', '.csv'}

class FileParser:
    """
    File parsing module that converts uploaded files to markdown format.
    Supports Markdown, Plain Text, and HTML file types with batch processing capability.
    """
    
    def __init__(self):
        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = False
        self.html_converter.body_width = 0  # No line wrapping
        self.markdownable_parser = MarkItDown(enable_plugins=False)
    
    def detect_file_type(self, file_path: str) -> str:
        """
        Detect file type based on extension.
        """
        _, extension = os.path.splitext(file_path)
        extension = extension.lower()
        
        if extension in ['.md', '.markdown']:
            return 'markdown'
        elif extension in ['.txt', '.csv']:
            return 'text'
        elif extension in ['.html', '.htm']:
            return 'html'
        elif extension in ['.pdf']:
            return 'pdf'
        elif extension in ['.docx', '.pptx', '.xlsx']:
            return 'markdownable'
        else:
            return 'unknown'
    
    def parse_file(self, file_path: str, save: bool = True) -> Dict[str, Any]:
        """
        Parse a single file based on its type and return the result.
        
        Args:
            file_path: Path to the file to parse
            save: Whether to save the parsed content to disk
            
        Returns:
            Dict containing:
                - 'success': bool indicating if parsing succeeded
                - 'content': parsed markdown content (if successful)
                - 'original_file': path to original file
                - 'parsed_file': path to parsed file (if saved)
                - 'error': error message (if failed)
        """
        try:
            file_type = self.detect_file_type(file_path)
            
            parsed_content = None
            if file_type == 'markdown':
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                parsed_content = self._parse_markdown(content)
            elif file_type == 'text':
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                parsed_content = self._parse_text(content)
            elif file_type == 'html':
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                parsed_content = self._parse_html(content)
            elif file_type == 'pdf':
                parsed_content = self._parse_pdf(file_path)
                # Check if we got a list of page chunks or a single string
                if isinstance(parsed_content, list):
                    logger.info(f"Parsed PDF content in {len(parsed_content)} pages")
                    parsed_content = '\n\n'.join([page['text'] for page in parsed_content])
                else:
                    # Single string case
                    logger.info(f"Parsed PDF content")
            elif file_type == 'markdownable':
                # For binary files, don't read them directly as text
                parsed_content = self._parse_markdownable(file_path)
            else:
                logger.warning(f"Unsupported file type for parsing: {file_path}")
                return {
                    'success': False,
                    'content': None,
                    'original_file': file_path,
                    'parsed_file': None,
                    'error': f"Unsupported file type: {file_type}"
                }
                
            if parsed_content is not None and save:
                parsed_file_path = self.save_parsed_content(file_path, parsed_content)
            else:
                parsed_file_path = None
                
            return {
                'success': True,
                'content': parsed_content,
                'original_file': file_path,
                'parsed_file': parsed_file_path,
                'error': None
            }
                
        except Exception as e:
            logger.error(f"Error parsing file {file_path}: {str(e)}")
            return {
                'success': False,
                'content': None,
                'original_file': file_path,
                'parsed_file': None,
                'error': str(e)
            }
    
    def _parse_markdown(self, content: str) -> str:
        """
        Parse Markdown content using MarkitDown.
        """
        return content
    
    def _parse_text(self, content: str) -> str:
        """
        Parse Plain Text content into Markdown format.
        """
        if not content.strip():
            return ''
        
        # Convert newlines to markdown line breaks
        content = content.replace('\r\n', '\n')
        return content
    
    def _parse_html(self, content: str) -> str:
        """
        Parse HTML content using html2text.
        """
        return self.html_converter.handle(content)

    def _parse_pdf(self, file_path: str) -> str:
        """
        Parse PDF content using PyPDF2.
        """
        parsed_dir, filename = self._get_parsed_path(file_path)
        # copy the file to parsed_dir
        target_image_path = os.path.join(parsed_dir, f"{filename}_images")
        os.makedirs(target_image_path, exist_ok=True)
        target_file_path = os.path.join(target_image_path, f"{filename}.pdf")
        shutil.copy(file_path, target_file_path)
        # image_path = os.path.join(parsed_dir, f"{filename}_images")
                
        md_text = pymupdf4llm.to_markdown(
            doc=target_file_path,  # The file, either as a file path or a PyMuPDF Document.
            page_chunks=False,  # If True, output is a list of page-specific dictionaries. Set to False for single string.
            show_progress=True,  # Displays a progress bar during processing.
            hdr_info=True,  # Optional, disables header detection logic.
            write_images=True,  # Saves images found in the document as files.
            # embed_images=True,  - Embeds images directly as base64 in markdown.
            image_size_limit=0.5,  # Exclude small images below this size threshold.
            dpi=150,  # Image resolution in dots per inch, if write_images=True.
            # image_path=image_path,  # Directory to save images if write_images=True.
            image_format="png",  # Image file format, e.g., "png" or "jpg".
            force_text=True,  # Include text overlapping images/graphics.
            margins=0,  # Specify page margins for text extraction.
            # page_width=612,  # Desired page width for reflowable documents.
            # page_height=None,  - Desired page height for reflowable documents.
            table_strategy="lines_strict",  # Strategy for table detection.
            # graphics_limit=5000,  # Limit the number of vector graphics processed.
            ignore_code=False,  # If True, avoids special formatting for mono-spaced text.
            extract_words=False,  # Adds word-level data to each page dictionary.
        )

        # remove the copied pdf file from the image path
        os.remove(target_file_path)

        return md_text

    def _parse_markdownable(self, file_path: str) -> str:
        """
        Parse Markdownable content using MarkitDown.
        """
        return self.markdownable_parser.convert(file_path).text_content
    
    async def parse_batch(self, file_paths: List[str], save: bool = True) -> Dict[str, Any]:
        """
        Parse multiple files in batch using asyncio.
        
        Args:
            file_paths: List of paths to files to parse
            save: Whether to save parsed content to disk
            
        Returns:
            Dict containing:
                - 'results': Dict mapping original file paths to their parsing results
                - 'original_to_parsed': Dict mapping original file paths to parsed file paths
                - 'parsed_to_original': Dict mapping parsed file paths to original file paths
                - 'summary': Summary statistics about the batch parsing
        """
        results = {}
        original_to_parsed = {}
        parsed_to_original = {}
        success_count = 0
        failure_count = 0
        saved_count = 0
        
        async def parse_file_async(file_path):
            result = self.parse_file(file_path, save=save)
            return file_path, result
        
        tasks = [parse_file_async(file_path) for file_path in file_paths]
        completed_tasks = await asyncio.gather(*tasks, return_exceptions=True)
        
        for file_path, result in completed_tasks:
            if isinstance(result, Exception):
                results[file_path] = {
                    'success': False,
                    'content': None,
                    'original_file': file_path,
                    'parsed_file': None,
                    'error': str(result)
                }
                failure_count += 1
                logger.error(f"Error parsing file {file_path}: {str(result)}")
            else:
                results[file_path] = result
                if result['success']:
                    success_count += 1
                    if save and result['parsed_file']:
                        original_to_parsed[file_path] = result['parsed_file']
                        parsed_to_original[result['parsed_file']] = file_path
                        saved_count += 1
                else:
                    failure_count += 1
        
        return {
            'results': results,
            'original_to_parsed': original_to_parsed,
            'parsed_to_original': parsed_to_original,
            'summary': {
                'total_files': len(file_paths),
                'successful_parsing': success_count,
                'failed_parsing': failure_count,
                'saved_parsed_files': saved_count
            }
        }
    
    def save_parsed_content(self, original_file_path: str, parsed_content: str, base_upload_dir: str = "uploads") -> Optional[str]:
        """
        Save parsed markdown content to the appropriate parsed folder structure.
        Original path format: uploads/user_id/knowledge_base/origin/filename.ext
        Parsed path format: uploads/user_id/knowledge_base/parsed/filename.md
        
        Handles filename conflicts by appending a counter if the filename already exists.
        """
        try:
            # Extract user_id, knowledge_base, and filename from original path
            parsed_dir, filename = self._get_parsed_path(original_file_path)
            try:  
                
                # Create parsed file path with .md extension, handling conflicts
                base_filename = filename
                counter = 1
                parsed_file_path = os.path.join(parsed_dir, f"{base_filename}.md")
                
                # Check if file exists and increment counter if needed
                while os.path.exists(parsed_file_path):
                    parsed_file_path = os.path.join(parsed_dir, f"{base_filename}_{counter}.md")
                    counter += 1
                
                # Save parsed content
                with open(parsed_file_path, 'w', encoding='utf-8') as f:
                    f.write(parsed_content)
                
                return parsed_file_path
                
            except ValueError as e:
                logger.error(f"Error extracting path components from {original_file_path}: {str(e)}")
                return None
                
        except Exception as e:
            logger.error(f"Error saving parsed content for {original_file_path}: {str(e)}")
            return None

    def _get_parsed_path(self, original_file_path: str, base_upload_dir: str = "uploads") -> Tuple[str, str]:
        """
        Get the parsed file path from the original file path.
        
        Returns:
            Tuple of (parsed_dir, filename) where:
            - parsed_dir: Directory path where parsed content will be saved
            - filename: Filename without extension
        """
        # Extract user_id, knowledge_base, and filename from original path
        path_parts = original_file_path.split(os.sep)
            
        # Find the origin folder index
        try:
            origin_idx = path_parts.index("origin")
            if origin_idx < 2:  # Need at least uploads/user_id/knowledge_base/origin
                raise ValueError("Invalid path structure")
                    
            # Build parsed directory path
            parsed_dir_parts = path_parts[:origin_idx] + ["parsed"]
            parsed_dir = os.sep.join(parsed_dir_parts)
            # Create parsed directory if it doesn't exist
            os.makedirs(parsed_dir, exist_ok=True)
                
            # Get filename without extension and original extension
            filename_with_ext = path_parts[-1]
            filename, original_ext = os.path.splitext(filename_with_ext)
                
            return parsed_dir, filename
        except ValueError as e:
            logger.error(f"Error extracting path components from {original_file_path}: {str(e)}")
            return None