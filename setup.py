

import os
from termcolor import colored
from time import sleep

banner = colored("""
  ______ _        _____          _         __  __       _ _     ________   
 |  ____| |      |  __ \        | |       |  \/  |     | | |   /  ____  \  
 | |__  | |______| |__) |___  __| | __ _  | \  / | __ _| | |  /  / ___|  \ 
 |  __| | |______|  _  // _ \/ _` |/ _` | | |\/| |/ _` | | | |  | |       |
 | |____| |      | | \ \  __/ (_| | (_| | | |  | | (_| | | | |  | |___    |
 |______|_|      |_|  \_\___|\__,_|\__,_| |_|  |_|\__,_|_|_|  \  \____|  / 
                     By: Hossam Hamdy                          \________/  

""", "yellow")

print(colored(banner, "green"))
sleep(3)


libs = ["playsound", "pyqt5", "win10toast", "openpyxl", "xlsxwriter"]
for i in libs:
    print(colored(f"[+] Installing {i} Module :)", "green"))
    os.system(f"pip install {i}")
    os.system("cls")

print(colored("[+] I hope it works without any problems ;(", "green"))
print(colored("[-] Thank you for using this script <3.\n\n", "blue"))
