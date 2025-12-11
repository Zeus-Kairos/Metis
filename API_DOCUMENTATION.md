# Metis File Upload API Documentation

## Overview
The Metis File Upload API provides endpoints for uploading files to a structured storage system organized by user ID and knowledge base.

## Base URL
```
http://localhost:8000
```

## Authentication
Currently, the API does not require authentication. In production environments, it is recommended to implement API key authentication or OAuth2.

## Endpoints

### Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Description**: Verify the API is running
- **Response**:
  ```json
  {
    "status": "ok",
    "message": "File Upload API is running"
  }
  ```

### File Upload
- **URL**: `/api/upload`
- **Method**: `POST`
- **Description**: Upload one or more files to a knowledge base
- **Content-Type**: `multipart/form-data`

#### Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | String | Yes | Unique identifier for the user |
| `knowledge_base` | String | Yes | Name of the knowledge base |
| `files` | File(s) | Yes | One or more files to upload |

#### Supported File Formats
- `.txt`
- `.md`
- `.pdf`
- `.docx`
- `.pptx`
- `.xlsx`

#### File Size Limit
- Maximum file size: 50MB per file
- Maximum files per request: 10 files

#### Response
```json
{
  "status": "success",
  "files": [
    {
      "filename": "example.txt",
      "status": "success",
      "path": "uploads/user_id/knowledge_base/origin/example.txt"
    }
  ],
  "total": 1,
  "successful": 1,
  "skipped": 0,
  "failed": 0
}
```

#### Error Response
```json
{
  "status": "error",
  "files": [
    {
      "filename": "example.exe",
      "status": "failed",
      "reason": "Unsupported file format"
    }
  ],
  "total": 1,
  "successful": 0,
  "skipped": 0,
  "failed": 1
}
```

## Storage Structure
Uploaded files are stored in the following directory structure:
```
uploads/
└── {user_id}/
    └── {knowledge_base}/
        └── origin/
            └── {filename}
```

## Duplicate Handling
- Files with identical content (based on MD5 hash) are automatically skipped
- Files with the same name but different content are renamed with a numeric suffix

## Usage Examples

### Python (requests)
```python
import requests
from io import BytesIO

# Create test file
content = b"Test content"
files = {'files': ('test.txt', BytesIO(content), 'text/plain')}
data = {'user_id': 'test_user', 'knowledge_base': 'test_kb'}

# Send request
response = requests.post('http://localhost:8000/api/upload', data=data, files=files)

print(response.json())
```

### JavaScript (Fetch)
```javascript
const formData = new FormData();
formData.append('user_id', 'test_user');
formData.append('knowledge_base', 'test_kb');

// Create test file
const blob = new Blob(['Test content'], { type: 'text/plain' });
formData.append('files', blob, 'test.txt');

fetch('http://localhost:8000/api/upload', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

## Error Codes
| Status Code | Description |
|-------------|-------------|
| 200 | Successful upload |
| 400 | Bad request (invalid parameters, unsupported format, etc.) |
| 500 | Internal server error |

## Development

### Running the API
```bash
cd c:\Apps\Metis
python -m src.api.main
```

### Testing
```bash
# Run unit tests
python -m pytest tests/test_upload.py -v

# Run integration tests
python tests/test_api.py
```

## Deployment

### Environment Variables
The following environment variables can be configured:
- `UPLOAD_DIR`: Base directory for file uploads (default: `uploads`)
- `MAX_FILE_SIZE`: Maximum file size in bytes (default: 50MB)
- `MAX_FILES_PER_REQUEST`: Maximum files per request (default: 10)

### Production Recommendations
1. Configure proper CORS settings
2. Implement authentication
3. Set up a production storage solution (S3, Azure Blob Storage, etc.)
4. Add monitoring and logging
5. Enable HTTPS

## Version History
- **1.0.0**: Initial release with basic file upload functionality
