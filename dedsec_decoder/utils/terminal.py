import os
import time
from colorama import Fore, Style

class TerminalUtils:
    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")
    
    @staticmethod
    def get_terminal_width():
        return os.get_terminal_size().columns
    
    @staticmethod
    def show_progress_bar():
        print("\n")
        for i in range(1, 101):
            print(Fore.GREEN + f"\rInitializing DedSec systems: {i}%", end="", flush=True)
            time.sleep(0.05)
        print(Style.RESET_ALL)
        time.sleep(0.5)