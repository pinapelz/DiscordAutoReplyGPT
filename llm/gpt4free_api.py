from llm.llm import LLM
from gpt4free import you
class GPT4FreeAPI(LLM):
    def __init__(self, memory_length: int) -> None:
        super().__init__(memory_length)

    def get_response(self, message: str) -> str:
        response = you.Completion.create(
            prompt=message,
            include_links=False,
            detailed=False,
            chat=self._chat_log)
        if len(self._chat_log) > self._memory_length:
            self._chat_log.pop(0)
        self._chat_log.append({"question": message, "answer": response.text})
        print(response.text)
        return response.text

