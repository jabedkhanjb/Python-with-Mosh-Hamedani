import pyautogui as jabedkhanjb
import time

limit = input("Enter number of message: ")
message = input("What's on your mind?\n")

i = 0
time.sleep(5)

while i < int(limit):
      jabedkhanjb.typewrite(message)
      jabedkhanjb.press("Enter")
      i += 1