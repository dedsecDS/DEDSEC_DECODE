import pyfiglet
from colorama import Fore, Style
from ..utils.terminal import TerminalUtils

class DisplayManager:
    def __init__(self):
        self.terminal = TerminalUtils()
    
    def show_banner(self):
        self.terminal.clear_screen()
        custom_fig = pyfiglet.Figlet(font="small")
        ascii_art = custom_fig.renderText(" Dead Security  DedSec")
        terminal_width = self.terminal.get_terminal_width()
        
        for line in ascii_art.split("\n"):
            print(Fore.RED + line.center(terminal_width) + Style.RESET_ALL)
    
    def show_loading(self):
        self.terminal.show_progress_bar()
    
    def show_interface(self):
        custom_fig = pyfiglet.Figlet(font="small")
        ascii_art = custom_fig.renderText("DS-COD/DECOD")
        info = [
            "BY: DedSec",
            "Youtube: ",
            "Github: github.com/dedsec"
        ]
        
        border = "=" * 40
        print(Fore.GREEN + border + Style.RESET_ALL)
        print(Fore.RED + ascii_art + Style.RESET_ALL)
        for line in info:
            print(Fore.RED + f"  {line}" + Style.RESET_ALL)
        print(Fore.GREEN + border + Style.RESET_ALL)