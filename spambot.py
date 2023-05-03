import pyautogui
import time

print("""\033[0;32m
  _____ ____   ____  ___ ___  ____    ___   ______ 
 / ___/|    \ /    ||   |   ||    \  /   \ |      |
(   \_ |  o  )  o  || _   _ ||  o  )|     ||      |
 \__  ||   _/|     ||  \_/  ||     ||  O  ||_|  |_|
 /  \ ||  |  |  _  ||   |   ||  O  ||     |  |  |  
 \    ||  |  |  |  ||   |   ||     ||     |  |  |  
  \___||__|  |__|__||___|___||_____| \___/   |__|   v1.0

       Made by BredSec\033[0m""")
print("")
print("""\033[0;31m       DISCLAIMER: Developers Not Liable For Any Damages
         Caused By Using This Tool. Use Responsibly.\033[0m""")

message = input("\033[1;34m\nWhat is your intended message>> \033[0m")

while True:
    time_length = input("\033[1;34mHow long would you like this to run (minutes)>> \033[0m")
    time_interval = input("\033[1;34mHow long in between each message (seconds)>> \033[0m")
    try:
        time_length = float(time_length) * 60
        time_interval = float(time_interval)
        break
    except:
        print("\033[0;31mEnter a number\033[0m")

print("\033[0;32m\n15 seconds until execution\033[0m")
time.sleep(15)

print("\033[0;32mExecuting...")
start = time.time()
while time.time() - start < time_length:
    pyautogui.typewrite(message) 
    pyautogui.press("enter")
    time.sleep(time_interval)

print("\033[0;32mScript completed\033[0m")