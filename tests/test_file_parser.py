import os
import pytest
import tempfile
from src.file_process.file_parser import FileParser

# Create a temporary directory for test files
@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

# Test file parser initialization
def test_file_parser_initialization():
    parser = FileParser()
    assert parser is not None
    assert parser.html_converter is not None

# Test file type detection
def test_detect_file_type():
    parser = FileParser()
    
    assert parser.detect_file_type("test.md") == "markdown"
    assert parser.detect_file_type("test.txt") == "text"
    assert parser.detect_file_type("test.csv") == "text"
    assert parser.detect_file_type("test.html") == "html"
    assert parser.detect_file_type("test.htm") == "html"
    assert parser.detect_file_type("test.pdf") == "pdf"
    assert parser.detect_file_type("test.docx") == "markdownable"
    assert parser.detect_file_type("test.pptx") == "markdownable"
    assert parser.detect_file_type("test.xlsx") == "markdownable"
    assert parser.detect_file_type("test.unknown") == "unknown"

# Test markdown parsing

def test_parse_markdown(temp_dir):
    parser = FileParser()
    
    # Create a test markdown file
    markdown_content = "# Heading 1\n\nThis is a paragraph.\n\n## Heading 2"
    markdown_file = os.path.join(temp_dir, "test.md")
    
    with open(markdown_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    # Parse the file without saving
    parsed_content = parser.parse_file(markdown_file, save=False)
    
    # Verify parsing
    assert parsed_content is not None
    assert parsed_content["success"] is True
    assert "Heading 1" in parsed_content["content"]
    assert "Heading 2" in parsed_content["content"]
    assert parsed_content["parsed_file"] is None

# Test text parsing

def test_parse_text(temp_dir):
    parser = FileParser()
    
    # Create a test text file
    text_content = "This is a text file.\n\nIt has multiple lines."
    text_file = os.path.join(temp_dir, "test.txt")
    
    with open(text_file, "w", encoding="utf-8") as f:
        f.write(text_content)
    
    # Parse the file without saving
    parsed_content = parser.parse_file(text_file, save=False)
    
    # Verify parsing
    assert parsed_content is not None
    assert parsed_content["success"] is True
    assert "This is a text file." in parsed_content["content"]
    assert "It has multiple lines." in parsed_content["content"]
    assert parsed_content["parsed_file"] is None

# Test HTML parsing

def test_parse_html(temp_dir):
    parser = FileParser()
    
    # Create a test HTML file
    html_content = "<html><head><title>Test</title></head><body><h1>Heading</h1><p>Paragraph</p></body></html>"
    html_file = os.path.join(temp_dir, "test.html")
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Parse the file without saving
    parsed_content = parser.parse_file(html_file, save=False)
    
    # Verify parsing
    assert parsed_content is not None
    assert parsed_content["success"] is True
    assert ("# Heading" in parsed_content["content"] or "Heading" in parsed_content["content"])
    assert "Paragraph" in parsed_content["content"]
    assert parsed_content["parsed_file"] is None

# Test unparseable file

def test_parse_unknown_file_type(temp_dir):
    parser = FileParser()
    
    # Create a test file with unknown extension
    unknown_content = "Unknown file content"
    unknown_file = os.path.join(temp_dir, "test.xyz")
    
    with open(unknown_file, "w", encoding="utf-8") as f:
        f.write(unknown_content)
    
    # Parse the file
    parsed_content = parser.parse_file(unknown_file)
    
    # Verify parsing fails for unknown file type
    assert parsed_content is not None
    assert parsed_content["success"] is False
    assert parsed_content["error"] is not None

# Test that PDF files are treated as markdownable (not unknown)
def test_pdf_is_pdf_type(temp_dir):
    parser = FileParser()

    # Create a test PDF file (simulated)
    pdf_content = "%PDF-1.4 PDF content"  # Minimal PDF header
    pdf_file = os.path.join(temp_dir, "test.pdf")

    with open(pdf_file, "w", encoding="utf-8") as f:
        f.write(pdf_content)

    # Detect file type
    file_type = parser.detect_file_type(pdf_file)
    assert file_type == "pdf"

# Test save_parsed_content functionality

def test_save_parsed_content(temp_dir):
    parser = FileParser()
    
    # Create a mock original path structure
    original_path = os.path.join(temp_dir, "uploads", "user123", "kb1", "origin", "test.txt")
    os.makedirs(os.path.dirname(original_path), exist_ok=True)
    
    with open(original_path, "w", encoding="utf-8") as f:
        f.write("Test content")
    
    # Parse and save
    parsed_content = "Parsed content"
    parsed_path = parser.save_parsed_content(original_path, parsed_content, temp_dir)
    
    # Verify parsed file was saved correctly
    assert parsed_path is not None
    assert "parsed" in parsed_path
    assert parsed_path.endswith(".md")
    
    # Check the parsed content
    with open(parsed_path, "r", encoding="utf-8") as f:
        saved_content = f.read()
    
    assert saved_content == parsed_content
    assert os.path.exists(parsed_path)

# Test filename collision handling

def test_filename_collision_handling(temp_dir):
    parser = FileParser()
    
    # Create mock original path structures for two different files with same base name
    original_path_1 = os.path.join(temp_dir, "uploads", "user123", "kb1", "origin", "test.txt")
    original_path_2 = os.path.join(temp_dir, "uploads", "user123", "kb1", "origin", "test.md")
    os.makedirs(os.path.dirname(original_path_1), exist_ok=True)
    
    with open(original_path_1, "w", encoding="utf-8") as f:
        f.write("Text content")
    
    with open(original_path_2, "w", encoding="utf-8") as f:
        f.write("# Markdown content")
    
    # Parse and save both files
    parsed_path_1 = parser.save_parsed_content(original_path_1, "Parsed text", temp_dir)
    parsed_path_2 = parser.save_parsed_content(original_path_2, "# Parsed markdown", temp_dir)
    
    # Verify both files were saved with different names
    assert parsed_path_1 is not None
    assert parsed_path_2 is not None
    assert parsed_path_1 != parsed_path_2
    
    # One should have _1 suffix
    assert ("test.md" in parsed_path_1 and "test_1.md" in parsed_path_2) or \
           ("test_1.md" in parsed_path_1 and "test.md" in parsed_path_2)
    
    assert os.path.exists(parsed_path_1)
    assert os.path.exists(parsed_path_2)

# Test file mappings
@pytest.mark.asyncio
async def test_file_mappings(temp_dir):
    parser = FileParser()
    
    # Create mock original path structures
    original_path_1 = os.path.join(temp_dir, "uploads", "user123", "kb1", "origin", "test1.txt")
    original_path_2 = os.path.join(temp_dir, "uploads", "user123", "kb1", "origin", "test2.md")
    os.makedirs(os.path.dirname(original_path_1), exist_ok=True)
    
    with open(original_path_1, "w", encoding="utf-8") as f:
        f.write("Text content 1")
    
    with open(original_path_2, "w", encoding="utf-8") as f:
        f.write("# Markdown content 2")
    
    # Parse both files
    results = await parser.parse_batch([original_path_1, original_path_2])
    
    # Verify mappings exist
    assert "original_to_parsed" in results
    assert "parsed_to_original" in results
    
    # Check original to parsed mapping
    assert original_path_1 in results["original_to_parsed"]
    assert original_path_2 in results["original_to_parsed"]
    
    parsed_path_1 = results["original_to_parsed"][original_path_1]
    parsed_path_2 = results["original_to_parsed"][original_path_2]
    
    # Check parsed to original mapping
    assert parsed_path_1 in results["parsed_to_original"]
    assert parsed_path_2 in results["parsed_to_original"]
    
    assert results["parsed_to_original"][parsed_path_1] == original_path_1
    assert results["parsed_to_original"][parsed_path_2] == original_path_2

# Test batch parsing functionality
@pytest.mark.asyncio
async def test_parse_batch(temp_dir):
    parser = FileParser()
    
    # Create test files
    files = [
        ("markdown.md", "# Heading", "markdown"),
        ("text.txt", "Text content", "text"),
        ("csv.csv", "column1,column2\ndata1,data2", "text"),
        ("html.html", "<h1>HTML Heading</h1>", "html")
    ]
    
    file_paths = []
    for filename, content, _ in files:
        file_path = os.path.join(temp_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        file_paths.append(file_path)
    
    # Parse batch without saving
    results = await parser.parse_batch(file_paths, save=False)
    
    # Verify results
    assert "results" in results
    assert "original_to_parsed" in results
    assert "parsed_to_original" in results
    assert "summary" in results
    
    # Check results structure
    assert len(results["results"]) == len(file_paths)
    assert results["summary"]["total_files"] == len(file_paths)
    
    # Check successful parsing for supported formats
    for file_path in file_paths:
        assert results["results"][file_path]["success"] is True
        assert results["results"][file_path]["content"] is not None

# Test error handling in parsing

def test_parse_file_error(temp_dir):
    parser = FileParser()
    
    # Create a test file with invalid content (simulate encoding error)
    bad_file = os.path.join(temp_dir, "bad.txt")
    
    # Write invalid UTF-8 content
    with open(bad_file, "wb") as f:
        f.write(b"Invalid UTF-8 content: \xff\xfe\xfd")
    
    # Parse the file - should return error in the dict
    parsed_content = parser.parse_file(bad_file)
    assert parsed_content is not None
    assert parsed_content["success"] is False
    assert parsed_content["error"] is not None

# Test empty file handling

def test_parse_empty_file(temp_dir):
    parser = FileParser()
    
    # Create empty files
    empty_files = [
        os.path.join(temp_dir, "empty.md"),
        os.path.join(temp_dir, "empty.txt"),
        os.path.join(temp_dir, "empty.html")
    ]
    
    for file_path in empty_files:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("")
        
        parsed_content = parser.parse_file(file_path, save=False)
        assert parsed_content is not None
        assert parsed_content["success"] is True
        assert parsed_content["content"].strip() == ""