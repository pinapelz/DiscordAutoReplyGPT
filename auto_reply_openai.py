import asyncio
import openai
import time
import pyautogui
from websockets.server import serve

def setup_window_position():
    print("Setting up window position, Please hover over message box in the next 5 seconds")
    time.sleep(5)


async def echo(websocket):
    async for message in websocket:
        print(f"Received message: {message}")
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        print(response.choices[0].message["content"]) # type: ignore
        await websocket.send(response.choices[0].message["content"]) # type: ignore

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    openai.api_key = "OPEN_AI_API_KEY"
    asyncio.run(main())

