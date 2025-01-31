from colorama import init, Fore, Style
from .core.binary import BinaryConverter
from .core.display import DisplayManager

def main():
    init()  # Initialize colorama
    display = DisplayManager()
    converter = BinaryConverter()
    
    display.show_banner()
    display.show_loading()
    display.terminal.clear_screen()
    display.show_interface()
    
    while True:
        print(Fore.GREEN + "\n=== DedSec Binary Conversion Tool ===" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Encode message to binary" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Decode binary to message" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Exit" + Style.RESET_ALL)
        
        choice = input(Fore.GREEN + "Enter your choice (1/2/3): " + Style.RESET_ALL)
        
        if choice == "1":
            message = input(Fore.GREEN + "Enter message to encode: " + Style.RESET_ALL)
            try:
                binary = converter.encode(message)
                print(Fore.RED + f"Encoded message: {binary}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)
        
        elif choice == "2":
            binary = input(Fore.GREEN + "Enter binary to decode: " + Style.RESET_ALL)
            try:
                message = converter.decode(binary)
                print(Fore.RED + f"Decoded message: {message}" + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Error: Invalid binary format" + Style.RESET_ALL)
        
        elif choice == "3":
            print(Fore.RED + "Goodbye, fellow DedSec member!" + Style.RESET_ALL)
            break
        
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()