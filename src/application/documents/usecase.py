from injector import Injector
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import SupabaseVectorStore

from src.domain.model.documents.documents_repository import DocumentsRepository


def from_documents_with_query(
    inj: Injector, docs: list[Document], query_name: str
) -> SupabaseVectorStore:
    r = inj.get(DocumentsRepository)
    return r.from_with_query(docs, query_name)


def delete_all_documents(inj: Injector) -> None:
    r = inj.get(DocumentsRepository)
    r.delete_all()
