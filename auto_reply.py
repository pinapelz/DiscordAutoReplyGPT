
import asyncio
from websockets.server import serve
from gpt4free_api import GPT4FreeAPI
from openai_api import OpenAIAPI
from discord_messenger import DiscordMacroMessage, DiscordRequestMessenger
import json


def load_config() -> dict:
    with open("config.json", "r") as f:
        return json.load(f)

class AutoReply:
    def __init__(self, config: dict) -> None:
        super().__init__()
        self._llm = GPT4FreeAPI()
        self._messenger = None
        self._config = config
        print("Configuration loaded, AutoReply Server ready. Waiting for WebSocket connection...")

    async def reply(self, websocket) -> None:
        print("WebSocket connection established. Initializing Discord Messenger...")
        # self._messenger = DiscordMacroMessage()
        self._messenger = DiscordRequestMessenger(self._config["DISCORD_CHANNEL_ID"],self._config["DISCORD_AUTHORIZATION"])
        print("Discord Messenger initialized. Waiting for messages...")
        async for message in websocket:
            print(f"Received message: {message}")
            response: str = self._llm.get_response(message)
            print(f"Sending response: {response}")
            self._messenger.send_message(response)
            await websocket.send(response)

    
    
    async def start_service(self) -> None:
        async with serve(self.reply, self._config["WEBSOCKET_HOST"], self._config["WEBSOCKET_PORT"]):
            await asyncio.Future()

if __name__ == "__main__":
    replier = AutoReply(load_config())
    asyncio.run(replier.start_service())