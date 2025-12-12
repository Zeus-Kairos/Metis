## Why
There is a need to automatically parse successfully uploaded files into markdown format to enable better content indexing and retrieval for the RAG system. This will enhance the user experience by making uploaded documents immediately available for querying.

## What Changes
- Add a document parsing layer that converts uploaded files to markdown
- Use MarikitDown for most file types (Markdown, plain text)
- Use html2text for HTML files
- Implement batch processing for efficient handling of multiple files
- Integrate parsing functionality with the existing file upload API

## Impact
- Affected specs: New capability "doc-parsing" will be added
- Affected code: 
  - src/utils/document_handler.py (new file)
  - src/api/upload.py (update existing API)
  - requirements.txt (add new dependencies)
