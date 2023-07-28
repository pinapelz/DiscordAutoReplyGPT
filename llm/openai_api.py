import openai
from llm.llm import LLM

class OpenAIAPI(LLM):
    def __init__(self, memory_length: int, api_key: str, content: str = "You are a helpful assistant", max_tokens: int = 500) -> None:
        super().__init__(memory_length)
        openai.api_key = api_key
        self._chat_log = []
        self._context = content
        self._max_tokens = max_tokens

    def get_response(self, message: str) -> str:
        if len(self._chat_log) >= self._memory_length*2: # We append two messages at a time
            self._chat_log = self._chat_log[2:]
        payload = [
            {"role": "system", "content": self._context},
        ] + self._chat_log + [{"role": "user", "content": message}]
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = payload,
            max_tokens = self._max_tokens,
        )
        self._chat_log += [{"role": "user", "content": message}, 
                           {"role": "assistant", "content": response.choices[0].message["content"]}]
        print(response.choices[0].message["content"]) # type: ignore
        return response.choices[0].message["content"]


