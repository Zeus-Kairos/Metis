import os
import asyncio
import shutil
import re
from typing import List, Dict, Any, Optional, Tuple
from markitdown import MarkItDown
import html2text
import pymupdf.layout
import pymupdf4llm

from src.utils.paths import get_parsed_path
from src.utils.logging_config import get_logger

logger = get_logger(__name__)

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
    
    def _read_file_with_encoding(self, file_path: str) -> str:
        """
        Read a text file trying multiple encodings in order of likelihood.
        
        Args:
            file_path: Path to the file to read
            
        Returns:
            File content as string
            
        Raises:
            UnicodeDecodeError: If all encodings fail
        """
        # Try encodings in order of likelihood
        encodings = [
            'utf-8',           # Most common modern encoding
            'windows-1252',    # Common for Windows files, especially HTML (handles byte 0xa0)
            'iso-8859-1',      # Latin-1, common fallback
        ]
        
        last_error = None
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read()
                logger.debug(f"Successfully read {file_path} with encoding: {encoding}")
                return content
            except UnicodeDecodeError as e:
                last_error = e
                logger.debug(f"Failed to read {file_path} with encoding {encoding}: {e}")
                continue
            except Exception as e:
                # For other errors (like file not found), re-raise immediately
                logger.error(f"Error reading file {file_path}: {e}")
                raise
        
        # If all encodings failed, try utf-8 with error handling as last resort
        logger.warning(f"All encodings failed for {file_path}, trying utf-8 with error replacement")
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            logger.warning(f"Read {file_path} with utf-8 and error replacement (some characters may be lost)")
            return content
        except Exception as e:
            logger.error(f"Final attempt to read {file_path} failed: {e}")
            raise UnicodeDecodeError(
                'utf-8',
                b'',
                0,
                1,
                f"Could not decode file {file_path} with any encoding. Last error: {last_error}"
            ) from last_error
    
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
                content = self._read_file_with_encoding(file_path)
                parsed_content = self._parse_markdown(content)
            elif file_type == 'text':
                content = self._read_file_with_encoding(file_path)
                parsed_content = self._parse_text(content)
            elif file_type == 'html':
                content = self._read_file_with_encoding(file_path)
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
            logger.exception(f"Error parsing file {file_path}: {str(e)}", stack_info=True)
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
        parsed_dir, filename = get_parsed_path(file_path)
        image_path = os.path.join(parsed_dir, f"{filename}_images")
                
        md_text = pymupdf4llm.to_markdown(
            doc=file_path,  # The file, either as a file path or a PyMuPDF Document.
            headers=False,  # Optional, disables header detection logic.
            footer=False,  # Optional, disables footer detection logic.
            page_chunks=False,  # If True, output is a list of page-specific dictionaries. Set to False for single string.
            show_progress=True,  # Displays a progress bar during processing.
            hdr_info=True,  # Optional, disables header detection logic.
            write_images=True,  # Saves images found in the document as files.
            # embed_images=True,  - Embeds images directly as base64 in markdown.
            image_size_limit=0.05,  # Exclude small images below this size threshold.
            dpi=150,  # Image resolution in dots per inch, if write_images=True.
            image_path=image_path,  # Directory to save images if write_images=True.
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

        # # Clean up image links without descriptions
        # md_text, removed_images = self._clean_image_links(md_text)
        # # remove the images not referenced in the markdown text
        # for img in removed_images:
        #     if os.path.exists(img):
        #         os.remove(img)

        return md_text

    def _clean_image_links(self, md_text: str) -> tuple[str, list[str]]:
        """
        Remove image links that don't have OCR descriptions.
        Keeps images that have the description block format with both start and end markers.
        
        Returns:
            tuple: (cleaned markdown content, list of removed image links)
        """
        # More strict pattern for image links - handles optional whitespace in parentheses
        image_pattern = r'!\[\]\s*\(\s*[^)]+\s*\)'
        
        # More strict pattern for description block start - handles the exact format with optional <br> tags
        desc_start_pattern = r'\s*\*\*----- Start of picture text -----\*\*\s*(<br>)?\s*'
        # More strict pattern for description block end - handles the exact format with optional <br> tags
        desc_end_pattern = r'\s*\*\*----- End of picture text -----\*\*\s*(<br>)?\s*'
        
        # Find all image links and their positions
        images = list(re.finditer(image_pattern, md_text))
        
        # If no images, return as is
        if not images:
            return md_text, []
        
        removed_images = []
        
        # Process images in reverse order to avoid position shifts when removing
        for image in reversed(images):
            image_start = image.start()
            image_end = image.end()
            
            # Get text after the image
            text_after = md_text[image_end:]
            
            # Check if there's a description block after this image
            # Look for the description start within a reasonable distance (1000 chars)
            max_check_length = min(1000, len(text_after))
            text_after_check = text_after[:max_check_length]
            
            # Use more strict pattern matching - ensure ONLY whitespace between image and description start
            # Match must start immediately after image with only whitespace in between
            # Construct the strict pattern directly to avoid issues with string manipulation
            strict_pattern = r'^\s*\*\*----- Start of picture text -----\*\*\s*(<br>)?\s*'
            desc_start_match = re.match(strict_pattern, text_after_check, re.DOTALL)
            
            if desc_start_match:
                # Look for end pattern after the start pattern
                remaining_text = text_after_check[desc_start_match.end():]
                desc_end_match = re.search(desc_end_pattern, remaining_text, re.DOTALL)
            else:
                desc_end_match = None
            
            if not (desc_start_match and desc_end_match):
                # No complete description, remove the image link and any trailing whitespace
                # Also remove any blank lines that might be left after the image
                next_content_start = image_end
                # Skip any whitespace/newlines after the image
                while next_content_start < len(md_text) and md_text[next_content_start] in (' ', '\t', '\n', '\r'):
                    next_content_start += 1
                
                # Store the removed image link
                removed_image = image.group().split('(')[1].split(')')[0].strip()
                removed_images.append(removed_image)
                
                # Remove the image and any trailing whitespace
                md_text = md_text[:image_start] + md_text[next_content_start:]
        
        return md_text, removed_images

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
            parsed_dir, filename = get_parsed_path(original_file_path)
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

    