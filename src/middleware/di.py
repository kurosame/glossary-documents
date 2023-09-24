import injector

from src.domain.model.documents.documents_repository import DocumentsRepository
from src.infrastructure.supabase.supabase_documents_repository import (
    SupabaseDocumentsRepository,
)


def bind(binder):
    binder.bind(DocumentsRepository, to=SupabaseDocumentsRepository)


def di() -> injector.Injector:
    return injector.Injector(bind)
