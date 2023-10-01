from langchain.schema import Document as LDocument


class Document:
    @staticmethod
    def set(page_content: str, metadata: dict) -> LDocument:
        return LDocument(page_content=page_content, metadata=metadata)
