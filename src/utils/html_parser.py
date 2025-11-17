import html2text
import re

def html_to_text(file_path='input.html', output_path='output.md'):
    # Try different encodings in order of likelihood
    encodings = ['utf-8', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                html = f.read()
            text = html2text.html2text(html)
            # Replace all .htm links with .md links, preserving anchor tags
            # Handle links with or without anchor tags
            text = re.sub(r'(\[.*?\]\(.*?)\.htm(#.*?)?(\))', r'\1.md\2\3', text)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            return text
        except UnicodeDecodeError:
            continue
    
    raise UnicodeDecodeError("All encodings failed", b"", 0, 1, "Could not decode file with any of the common encodings")


import os

if __name__ == '__main__':
    try:
        # Process a single file for testing
        # text = html_to_text("./Docs/VNA-Help/Home.htm", "./Docs/VNA_Help_MD/Home.md")
        # print("Single file conversion completed.")
        
        # Process all HTML files in the directory
        source_dir = "./Docs/VNA-Help"
        target_dir = "./Docs/VNA_Help_MD"
        
        # Create target directory structure if it doesn't exist
        for root, dirs, files in os.walk(source_dir):
            for dir in dirs:
                source_path = os.path.join(root, dir)
                relative_path = os.path.relpath(source_path, source_dir)
                target_path = os.path.join(target_dir, relative_path)
                os.makedirs(target_path, exist_ok=True)
        
        # Convert all HTML files
        total_files = 0
        success_count = 0
        
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                if file.lower().endswith('.htm'):
                    total_files += 1
                    source_path = os.path.join(root, file)
                    relative_path = os.path.relpath(source_path, source_dir)
                    target_filename = file[:-4] + '.md'  # Replace .htm with .md
                    target_path = os.path.join(target_dir, os.path.dirname(relative_path), target_filename)
                    
                    try:
                        html_to_text(source_path, target_path)
                        success_count += 1
                        print(f"Converted: {relative_path} -> {os.path.join(os.path.dirname(relative_path), target_filename)}")
                    except Exception as e:
                        print(f"Error converting {relative_path}: {e}")
        
        print(f"\nConversion complete: {success_count} of {total_files} files converted successfully.")
    
    except Exception as e:
        print(f"Error in main: {e}")