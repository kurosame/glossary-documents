from injector import Injector

from src.domain.model.documents.documents_repository import DocumentsRepository


def delete_all_documents(inj: Injector) -> None:
    r = inj.get(DocumentsRepository)
    r.delete_all()
