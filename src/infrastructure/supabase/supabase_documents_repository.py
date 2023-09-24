import os

from supabase import create_client

from src.domain.model.documents.documents_repository import DocumentsRepository


class SupabaseDocumentsRepository(DocumentsRepository):
    def __init__(self):
        self.supabase = create_client(
            os.environ.get("SUPABASE_API_URL"), os.environ.get("SUPABASE_API_KEY")
        )
        auth = self.supabase.auth.sign_in_with_password(
            {
                "email": os.environ.get("SUPABASE_GLOSSARY_EMAIL"),
                "password": os.environ.get("SUPABASE_GLOSSARY_PASSWORD"),
            }
        )
        self.supabase.postgrest.auth(auth.session.access_token)

    def __del__(self):
        self.supabase.auth.sign_out()

    def delete_all(self) -> None:
        self.supabase.table("documents").delete().neq("content", None).execute()
