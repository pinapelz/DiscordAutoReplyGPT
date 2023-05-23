
import asyncio
from websockets.server import serve
from gpt4free_api import GPT4FreeAPI
from openai_api import OpenAIAPI
from discord_messenger import DiscordMacroMessage
import json


def load_config() -> dict:
    with open("config.json", "r") as f:
        return json.load(f)

class AutoReply:
    def __init__(self, config: dict) -> None:
        super().__init__()
        self._llm = GPT4FreeAPI()
        self._messenger = DiscordMacroMessage()
        self._config = config

    async def reply_macro(self, websocket) -> None:
        self._messenger.setup_window_position()
        async for message in websocket:
            print(f"Received message: {message}")
            response: str = self._llm.get_response(message)
            self._messenger.send_message(response)
            await websocket.send(response)
    
    async def start_service(self) -> None:
        async with serve(self.reply_macro, self._config["WEBSOCKET_HOST"], self._config["WEBSOCKET_PORT"]):
            await asyncio.Future()

if __name__ == "__main__":
    replier = AutoReply(load_config())
    asyncio.run(replier.start_service())