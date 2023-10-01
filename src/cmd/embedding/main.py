import os

from dotenv import load_dotenv

from src.application.documents.usecase import (
    delete_all_documents,
    from_documents_with_query,
)
from src.domain.model.documents.document import Document
from src.middleware.di import di

load_dotenv(verbose=True)
inj = di()


if __name__ == "__main__":
    docs = []

    for root, _, files in os.walk(os.environ["DIR_PATH"]):
        for file in files:
            file_path = os.path.join(root, file)

            with open(file_path, "r") as f:
                lines = f.readlines()

                category = ""
                titles = []
                is_titles = False
                description = ""
                is_description = False

                for i in range(len(lines)):
                    if lines[i].strip() == "## category":
                        category = lines[i + 2].strip()
                    if is_titles:
                        if lines[i].strip() == "## description":
                            is_titles = False
                        elif lines[i].strip() != "":
                            titles.append(lines[i].strip())
                    if lines[i].strip() == "## titles":
                        is_titles = True
                    if is_description:
                        description += lines[i].strip()
                    if lines[i].strip() == "## description":
                        is_description = True

                docs.append(
                    Document.set(
                        page_content=description,
                        metadata={
                            "category": category,
                            "titles": titles,
                        },
                    )
                )
            break

    delete_all_documents(inj)
    store = from_documents_with_query(inj=inj, docs=docs, query_name="match_documents")

    print(store)
