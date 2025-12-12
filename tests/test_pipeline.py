import os
import asyncio
import pytest
from fastapi import UploadFile
from io import BytesIO
from src.file_process.pipeline import FileProcessingPipeline

@pytest.fixture
def pipeline():
    """Create a FileProcessingPipeline instance for testing."""
    return FileProcessingPipeline()

@pytest.fixture
def test_files_dir():
    """Return the path to test files directory."""
    return "c:\\Apps\\Metis\\tests\\test_files"

@pytest.fixture
def mock_upload_files(test_files_dir):
    """Create mock UploadFile objects from test files."""
    upload_files = []
    
    # Get all test files except image (which is not supported)
    for filename in os.listdir(test_files_dir):
        if filename == "test_image.jpeg":
            continue  # Skip unsupported image format
            
        file_path = os.path.join(test_files_dir, filename)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as f:
                content = f.read()
            
            upload_file = UploadFile(
                filename=filename,
                file=BytesIO(content)
            )
            upload_files.append(upload_file)
    
    return upload_files

@pytest.mark.asyncio
async def test_pipeline_with_supported_files(pipeline, mock_upload_files, tmpdir):
    """Test the pipeline with supported test files."""
    # Process files through pipeline
    result = await pipeline.process_files(
        user_id="test_pipeline_user",
        knowledge_base="test_pipeline_kb",
        files=mock_upload_files
    )
    
    # Verify results
    assert result["status"] in ["success", "partial_success"]
    assert result["total"] == len(mock_upload_files)
    
    # Check that all supported files were processed
    for file_result in result["files"]:
        # All supported files should be successful
        assert file_result["status"] == "success"
        
        # Path should be set for successful uploads
        assert "path" in file_result
        assert os.path.exists(file_result["path"])
        
        # File should be parsed
        assert file_result.get("parsed", False) == True
        assert "parsed_path" in file_result
        assert os.path.exists(file_result["parsed_path"])
    
    # Verify parsing statistics
    assert result["parsing"]["total_parsed"] == len(mock_upload_files)
    assert result["parsing"]["failed_parsing"] == 0

@pytest.mark.asyncio
async def test_pipeline_with_mixed_files(pipeline, test_files_dir):
    """Test the pipeline with both supported and unsupported files."""
    upload_files = []
    
    # Include all test files including image
    for filename in os.listdir(test_files_dir):
        file_path = os.path.join(test_files_dir, filename)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as f:
                content = f.read()
            
            upload_file = UploadFile(
                filename=filename,
                file=BytesIO(content)
            )
            upload_files.append(upload_file)
    
    # Process files through pipeline
    result = await pipeline.process_files(
        user_id="test_mixed_user",
        knowledge_base="test_mixed_kb",
        files=upload_files
    )
    
    # Verify results
    assert result["status"] == "partial_success"
    assert result["total"] == len(upload_files)
    
    # Count successful and failed
    successful = 0
    failed = 0
    
    for file_result in result["files"]:
        if file_result["filename"] == "test_image.jpeg":
            # Image should fail
            assert file_result["status"] == "failed"
            assert "error" in file_result
            failed += 1
        else:
            # Other files should succeed
            assert file_result["status"] == "success"
            successful += 1
    
    assert successful == len(upload_files) - 1  # All except image
    assert failed == 1  # Only image should fail

@pytest.fixture(scope="module", autouse=True)
def cleanup_after_tests():
    """Cleanup test files after module runs."""
    yield
    
    # Remove test directories
    test_dirs = [
        "c:\\Apps\\Metis\\uploads\\test_pipeline_user",
        "c:\\Apps\\Metis\\uploads\\test_mixed_user"
    ]
    
    for test_dir in test_dirs:
        if os.path.exists(test_dir):
            for root, dirs, files in os.walk(test_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(test_dir)
