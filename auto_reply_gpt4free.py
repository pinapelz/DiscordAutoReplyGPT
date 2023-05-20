import asyncio
import pyautogui
import time
from gpt4free import you
from websockets.server import serve

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
    chat_log = []
    window_pos = setup_window_position()
    async for message in websocket:
        print(f"Received message: {message}")
        response = you.Completion.create(
            prompt=message,
            include_links=False,
            detailed=True,
            chat=chat_log)
        print(response.text)
        pyautogui.moveTo(window_pos.x, window_pos.y, 1)
        pyautogui.click()
        pyautogui.write(str(response.text), interval=0.03)
        pyautogui.press('enter')
        if len(chat_log) > 4:
            chat_log.pop(0)
        chat_log.append({"question": message, "answer": response.text})
        await websocket.send(response.text)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(main())

