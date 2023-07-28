from abc import ABC, abstractmethod

class LLM(ABC):

    def __init__(self, memory_length: int) -> None:
        if memory_length <= 1:
            raise ValueError("Memory length must be greater than 1.")
        self._memory_length = memory_length
        self._chat_log = []

    @abstractmethod
    def get_response(message: str) -> str:
        pass

