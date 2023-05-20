import asyncio
import openai
import time
import pyautogui
import json

from websockets.server import serve

def get_api_key():
    # reads api key from config.json
    with open("config.json", "r") as f:
        config = json.load(f)
    return config["OPEN_AI_APIKEY"]


def setup_window_position():
    window_pos = None
    def ask_confirm():
        while True:
            print("Enter 'p' to playback moving to mouse pos, 'c' to confirm position, 'r' to redo positioning")
            command = input()
            match command:
                case 'p':
                    pyautogui.moveTo(window_pos.x, window_pos.y, 1)
                case 'c':
                    return True
                case 'r':
                    return False
    pos_set = False
    while not pos_set:
        print("Setting up window position, Please hover over message box in the next 5 seconds")
        time.sleep(5)
        window_pos = pyautogui.position()
        print("Captured position: ", window_pos, "Enter 'p' to playback moving to mouse pos, 'c' to confirm position, 'r' to redo positioning")
        pos_set = ask_confirm()
    return window_pos


async def echo(websocket):
    message_log = []
    window_pos = setup_window_position()
    async for message in websocket:
        if len(message_log) >= 5:
            message_log = message_log[2:]
        print(f"Received message: {message}")
        payload = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ] + message_log
        print(payload)
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = payload
        )
        print(response.choices[0].message["content"]) # type: ignore
        pyautogui.moveTo(window_pos.x, window_pos.y, 1)
        pyautogui.click()
        pyautogui.write(str(response.text), interval=0.03)
        pyautogui.press('enter')
        message_log += [{"role": "user", "content": message}, {"role": "assistant", "content": response.choices[0].message["content"]}]
        await websocket.send(response.choices[0].message["content"]) # type: ignore

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    openai.api_key = get_api_key()
    asyncio.run(main())

