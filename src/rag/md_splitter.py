import os
from pathlib import Path
from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter
from collections import defaultdict

class MarkdownSplitter:
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]

    def split_markdown_file(self, file_path: str):
        """Read and split the Markdown file, returning the split results."""
        markdown_splitter = MarkdownHeaderTextSplitter(self.headers_to_split_on, strip_headers=False)
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
        docs = markdown_splitter.split_text(content)
        # Add file_path to the metadata of each Document
        for doc in docs:
            doc.metadata["file_path"] = file_path
        return docs

    def split_all_markdown_files(self, root_dir: str, include_filepath: bool=True) -> List[Document]:
        """
        Recursively traverse all Markdown files under root_dir, split by headers, and return a list of all Documents.
        
        Args:
            root_dir (str): The root directory to start the search for Markdown files.
            include_filepath (bool, optional): Whether to include the file_path in the metadata of each Document. Defaults to True.
                                               All file_path values use relative paths with respect to root_dir.
        
        Returns:
            list: A list of all split Documents.
        
        
        """
        root_path = Path(root_dir).resolve()
        all_docs = []

        for md_file in root_path.rglob("*.md"):
            docs = self.split_markdown_file(str(md_file))
            # Update file_path in metadata to the relative path
            if include_filepath:
                # Compute the relative path with respect to root_dir
                rel_path = os.path.relpath(md_file, root_path).replace("\\", "/")
                for doc in docs:
                    doc.metadata["file_path"] = rel_path
            all_docs.extend(docs)

        return all_docs


if __name__ == '__main__':
    # Test the function with a sample directory
    sample_dir = "./Docs/VNA_Help_MD/Applications"
    markdown_splitter = MarkdownSplitter()
    split_results = markdown_splitter.split_all_markdown_files(sample_dir, include_filepath=True)
    print(f"Split {sample_dir} into {len(split_results)} sections.")
    grouped = defaultdict(list)
    for section in split_results:
        grouped[section.metadata["file_path"]].append(section)

    for file_path, sections in grouped.items():
        print(f"{file_path}: {len(sections)} sections")
