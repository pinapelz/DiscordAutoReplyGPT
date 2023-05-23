from abc import ABC, abstractmethod

class LLM(ABC):

    @abstractmethod
    def get_response(message: str) -> str:
        pass

