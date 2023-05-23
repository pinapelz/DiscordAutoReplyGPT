import openai
from llm import LLM

class OpenAIAPI(LLM):
    def __init__(self, api_key: str) -> None:
        super().__init__()
        self.chat_log = []
        self.api_key = api_key

    def get_response(self, message: str) -> str:
        if len(self._chat_log) >= 5:
            self._chat_log = self._chat_log[2:]
        payload = [
            {"role": "system", "content": "You are a helpful assistant."},
        ] + self._chat_log + [{"role": "user", "content": message}]
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = payload
        )
        print(response.choices[0].message["content"]) # type: ignore
        return response.choices[0].message["content"]


