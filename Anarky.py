# Importo le librerie
import webbrowser
import time
from time import sleep
from colorama import Fore  # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style  # DIM, NORMAL, BRIGHT, RESET_ALL

# Variabili
verde = Fore.GREEN
blu = Fore.BLUE
reset = Style.RESET_ALL
giallo = Fore.YELLOW
rosso = Fore.LIGHTRED_EX  # Colora Rosso e rende il testo brillante
brillante = Style.BRIGHT
opaco = Style.DIM
count = 0
# Pausa
time.sleep(1)
# Info
with open('ganarky.dll', encoding='utf8') as f:
    print(blu + f.read() + reset, '\n')


def open_url():
    global count
    webbrowser.open(url)
    time.sleep(2)
    count += 1


with open("Video.txt", "r") as file:
    links = file.read().splitlines()
    for link in links:
        url = link
        print(link)
        open_url()

print(f"Ho aperto {count} video.")
time.sleep(10)
