from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os

# Import the upload handler from another file
from src.api.upload import handle_file_upload

app = FastAPI(title="Metis File Upload API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API endpoint for file uploads
@app.post("/api/upload")
async def upload_files(
    user_id: str = Form(...),
    knowledge_base: str = Form(...),
    files: List[UploadFile] = File(...)
):
    """Upload one or more files to a knowledge base."""
    try:
        # Call the upload handler
        result = await handle_file_upload(user_id, knowledge_base, files)
        return result
    except Exception as e:
        # Return an error response with status code 400
        raise HTTPException(status_code=400, detail=str(e))

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint to verify API is running."""
    return {"status": "ok", "message": "File Upload API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)