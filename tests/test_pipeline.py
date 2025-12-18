import os
import asyncio
import pytest
from fastapi import UploadFile
from io import BytesIO
from src.file_process.pipeline import FileProcessingPipeline
from src.file_process.file_parser import PARSABLE_FORMATS
from src.file_process.file_upload import SUPPORTED_FORMATS

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
        user_id=1,
        knowledge_base="test_pipeline_kb",
        directory="test_directory",  # Add missing directory parameter
        files=mock_upload_files
    )

    # Print detailed results
    print(f"Pipeline Status: {result['status']}")
    print(f"Total Files: {result['total']}, Successful: {result['successful']}, Skipped: {result['skipped']}, Failed: {result['failed']}")
    print(f"Total Chunks: {result['total_chunks']}")  # Add total_chunks print
    print("\nFile Details:")
    for file_result in result['files']:
        print(f"  - {file_result['filename']}: Status={file_result['status']}, Parsed={file_result.get('parsed', False)}, Errors={file_result.get('errors', '')}")

    # Assertions
    assert result["status"] == "partial_success" or result["status"] == "success"
    assert result["total"] == 6
    assert result["successful"] + result["skipped"] + result["failed"] == result["total"]

    # Check that all supported files were processed successfully
    for file_result in result["files"]:
        if file_result["status"] == "success":
            file_ext = os.path.splitext(file_result["filename"])[1].lower()
            if file_ext in PARSABLE_FORMATS:
                assert file_result.get("parsed", False), f"{file_result['filename']} should be parsed"

    # Print pipeline result
    print("\n=== Pipeline Result (Supported Files) ===")
    print(f"Status: {result['status']}")
    print(f"Total: {result['total']}, Successful: {result['successful']}, Skipped: {result['skipped']}, Failed: {result['failed']}")
    print(f"Parsing - Total Parsed: {result['parsing']['total_parsed']}, Failed Parsing: {result['parsing']['failed_parsing']}")
    print(f"Total Chunks: \n{result['total_chunks']}")
    print("Files:")
    for file_result in result['files']:
        print(f"  {file_result['filename']} - Status: {file_result['status']}, Parsed: {file_result.get('parsed', 'N/A')}")
        if file_result['status'] != 'success':
            print(f"    Error: {file_result.get('error', '')}")
            print(f"    Message: {file_result.get('message', '')}")
        if file_result.get('parsed') == False:
            print(f"    Parsing Error: {file_result.get('parsing_error', '')}")
    print("========================================\n")
    
    # Verify results
    assert result["status"] in ["success", "partial_success"]
    assert result["total"] == len(mock_upload_files)
    
    # Check that all supported files were processed
    for file_result in result["files"]:
        # All supported files should be either successful or skipped (already exists)
        assert file_result["status"] in ["success", "skipped"]
        
        if file_result["status"] == "success":
            # Path should be set for successful uploads
            assert "path" in file_result
            assert os.path.exists(file_result["path"])
            
            # File should be parsed
            assert file_result.get("parsed", False) == True
            assert "parsed_path" in file_result
            assert os.path.exists(file_result["parsed_path"])
        else:  # skipped
            # Skip doesn't have path, but should have message
            assert "message" in file_result
    
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
        user_id=2,
        knowledge_base="test_mixed_kb",
        directory="test_directory",  # Add missing directory parameter
        files=upload_files
    )

    # Print detailed results
    print(f"Pipeline Status: {result['status']}")
    print(f"Total Files: {result['total']}, Successful: {result['successful']}, Skipped: {result['skipped']}, Failed: {result['failed']}")
    print(f"Total Chunks: {result['total_chunks']}")  # Add total_chunks print
    print("\nFile Details:")
    for file_result in result['files']:
        print(f"  - {file_result['filename']}: Status={file_result['status']}, Parsed={file_result.get('parsed', False)}, Errors={file_result.get('errors', '')}")

    # Assertions
    assert result["status"] == "partial_success" or result["status"] == "success"
    assert result["total"] >= 1  # At least one file should be processed
    assert result["successful"] + result["skipped"] + result["failed"] == result["total"]

    # Check that image file is handled appropriately
    image_extensions = ['.jpeg', '.jpg', '.png', '.gif', '.bmp']
    for file_result in result["files"]:
        filename = file_result["filename"]
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in image_extensions:
            assert file_ext not in SUPPORTED_FORMATS, f"Image files should not be in supported formats: {filename}"

    # Print pipeline result
    print("\n=== Pipeline Result (Mixed Files) ===")
    print(f"Status: {result['status']}")
    print(f"Total: {result['total']}, Successful: {result['successful']}, Skipped: {result['skipped']}, Failed: {result['failed']}")
    print(f"Parsing - Total Parsed: {result['parsing']['total_parsed']}, Failed Parsing: {result['parsing']['failed_parsing']}")
    print(f"Total Chunks: \n{result['total_chunks']}")
    print("Files:")
    for file_result in result['files']:
        print(f"  {file_result['filename']} - Status: {file_result['status']}, Parsed: {file_result.get('parsed', 'N/A')}")
        if file_result['status'] != 'success':
            print(f"    Error: {file_result.get('error', '')}")
            print(f"    Message: {file_result.get('message', '')}")
        if file_result.get('parsed') == False:
            print(f"    Parsing Error: {file_result.get('parsing_error', '')}")
    print("====================================\n")
    
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
            # Other files should be either success or skipped (already exists)
            assert file_result["status"] in ["success", "skipped"]
            if file_result["status"] == "success":
                successful += 1
    
    assert successful == len(upload_files) - 1  # All except image
    assert failed == 1  # Only image should fail

    vectorstore = result["vectorstore"]
    assert vectorstore is not None
    assert len(vectorstore.index_to_docstore_id) == result["total_chunks"]["total"]

    test_result = vectorstore.similarity_search_with_score("measurement accuracy of N8481A", k=3)
    print(test_result)

@pytest.fixture(scope="function", autouse=True)
def cleanup_after_tests():
    """Cleanup test files after each test runs."""
    yield
    
    # Remove test directories
    import shutil
    test_dirs = [
        r"c:\Apps\Metis\uploads\1",
        r"c:\Apps\Metis\uploads\2"
    ]
    
    for test_dir in test_dirs:
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir, ignore_errors=True)






