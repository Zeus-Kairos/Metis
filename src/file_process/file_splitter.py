from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

class FileSplitter:
    def __init__(self, chunk_size=300, chunk_overlap=30):
        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on, strip_headers=False)
    
    def split_text(self, text: str, metadata: dict = {}) -> list[Document]:
        md_header_splits  = self.markdown_splitter.split_text(text)
        documents = []
        chunk_index = 0
        for split in md_header_splits:
            split_docs = self.text_splitter.split_documents([split])
            for doc in split_docs:
                doc.metadata.update({"chunk_id": f"{chunk_index}"})
                doc.metadata.update(metadata)
                chunk_index += 1
            documents.extend(split_docs)
        return documents