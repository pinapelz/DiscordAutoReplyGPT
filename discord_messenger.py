from abc import ABC, abstractmethod
import pyautogui
import time


class DiscordMessenger(ABC):

    @abstractmethod
    def send_message(message: str) -> None:
        pass


class DiscordMacroMessage(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._window_pos = None

    def setup_window_position(self) -> None:
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
    
