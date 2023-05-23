from abc import ABC, abstractmethod
import pyautogui
import time
import requests


class DiscordMessenger(ABC):

    @abstractmethod
    def send_message(message: str) -> None:
        pass


class DiscordMacroMessage(DiscordMessenger):
    def __init__(self) -> None:
        super().__init__()
        self._setup_window_position()

    def _setup_window_position(self) -> None:
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
                    case _:
                        print("Invalid command, try again")
        window_pos = None
        pos_set = False
        while not pos_set:
            print("Setting up window position, Please hover over message box in the next 5 seconds")
            time.sleep(5)
            window_pos = pyautogui.position()
            print("Captured position: ", window_pos, "Enter 'p' to playback moving to mouse pos, 'c' to confirm position, 'r' to redo positioning")
            pos_set = ask_confirm()
        self._window_pos = window_pos
    
    def send_message(self, message: str) -> None:
        pyautogui.moveTo(self._window_pos.x, self._window_pos.y, 1)
        pyautogui.click()
        pyautogui.write(str(message), interval=0.03)
        pyautogui.press('enter')


class DiscordRequestMessenger(DiscordMessenger):
    def __init__(self, channel_id: str, authorization: str, base_url: str = "https://discord.com/api/v9/channels/") -> None:
        super().__init__()
        self._channel_id = channel_id
        self._headers  = {
            "authorization": authorization
        }
        self._url = base_url + channel_id + "/messages"
    def send_message(self, message: str) -> None:
        payload={
            "content": message
        }
        requests.post(self._url, data=payload, headers=self._headers)

    
