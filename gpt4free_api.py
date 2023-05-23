from gpt4free import you
from llm import LLM

class GPT4FreeAPI(LLM):
    def __init__(self) -> None:
        super().__init__()
        self._chat_log = []

    def get_response(self, message: str) -> str:
        response = you.Completion.create(
            prompt=message,
            include_links=False,
            detailed=True,
            chat=self._chat_log)
        if len(self._chat_log) > 4:
            self._chat_log.pop(0)
            self._chat_log.append({"question": message, "answer": response.text})
        return response.text
    