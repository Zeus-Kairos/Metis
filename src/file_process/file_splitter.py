from dataclasses import asdict
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter
from chonkie import Pipeline

class FileSplitter:
    def __init__(self, chunk_size=1000, chunk_overlap=50):
        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on, strip_headers=False)
    
    def split_text(self, text: str, metadata: dict = None) -> list[Document]:
        # Fix mutable default argument issue
        if metadata is None:
            metadata = {}
        
        md_header_splits  = self.markdown_splitter.split_text(text)
        pipeline = Pipeline().process_with("markdown").chunk_with("recursive", chunk_size=self.chunk_size)
        documents = []
        chunk_index = 0
        for split in md_header_splits:
            docs, chunk_index = self._split_pipeline(pipeline, split, chunk_index, metadata)
            documents.extend(docs)
        return documents

    def _split_pipeline(self, pipeline: Pipeline, doc: Document, chunk_index: int, metadata: dict) -> list[Document]:
        """Split document into recursive chunks with Chonkie pipeline.
        
        Args:
            pipeline: Chonkie pipeline to use for chunking
            doc: Document to split
            chunk_index: Current chunk index
            metadata: Metadata to attach to chunks
            
        Returns:
            List of Document objects and updated chunk_index
        """
        document = pipeline.run(doc.page_content)
        chunks = getattr(document, 'chunks', [])
        images = getattr(document, 'images', [])
        tables = getattr(document, 'tables', [])
        codes = getattr(document, 'code', [])
        chunk_tuples = [(chunk.start_index, "text", chunk.text, {k: v for k, v in chunk.to_dict().items() if k != "text"}) for chunk in chunks]
        image_tuples = [(image.start_index, "image", "image", {k: v for k, v in asdict(image).items()}) for image in images]
        table_tuples = [(table.start_index, "table", table.content[:self.chunk_size], {k: v for k, v in asdict(table).items()}) for table in tables]
        code_tuples = [(code.start_index, "code", code.content[:self.chunk_size], {k: v for k, v in asdict(code).items()}) for code in codes]
    
        # Merge all tuples
        all_tuples = chunk_tuples + image_tuples + table_tuples + code_tuples
    
        # Sort by start index
        all_tuples.sort(key=lambda x: x[0])
    
        file_id = metadata.get("file_id", "")
        documents = []
        for _, chunk_type, content, chunk_meta in all_tuples:
            document = Document(page_content=content, 
                    metadata={
                        "chunk_id": f"{file_id}_{chunk_index}",
                        "chunk_type": chunk_type,
                        **doc.metadata,
                        **chunk_meta,                         
                        **metadata
                    })
            chunk_index += 1
            documents.append(document)
        return documents, chunk_index