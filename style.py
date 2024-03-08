from colorama import Fore, Style

def style(value,color):
    if color == "green":
        color = Fore.GREEN
    elif color == "red":
        color = Fore.RED
    elif color == "yellow":
        color = Fore.YELLOW
    return(color + value + Style.RESET_ALL)