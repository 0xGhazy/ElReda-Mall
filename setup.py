import os
from cores.functions import change_whours
libs = ["pyqt5", "win10toast", "openpyxl", "xlsxwriter"]
for i in libs:
    print(f"[+] Installing {i} Module :)")
    os.system(f"pip install {i}")

# changing working hours number
os.chdir(os.path.dirname(__file__))
change_whours()

print("[+] I hope it works without any problems ;(")
print("[-] Thank you for using this script <3.\n\n")
