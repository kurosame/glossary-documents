from abc import ABC, abstractmethod


class DocumentsRepository(ABC):
    @abstractmethod
    def delete_all(self) -> None:
        raise NotImplementedError()
