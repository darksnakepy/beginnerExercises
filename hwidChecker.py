import os, subprocess
from typing import Text
import requests
import os, sys, time, traceback, pickle, random

os.system("cls")
print("Auth system by DarkSnake")
checkhwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip() 
r = requests.get("https://pastebin.com/YZzagfHd")

try:
    if checkhwid in r.text:
        print("HWID Confirmed")
    else:
        print("Wrong HWID, you tried bud")
        time.sleep(5)
        os.close()
except:
    print("Check your wifi")
    time.sleep(5)

print("Logged in")
input()
