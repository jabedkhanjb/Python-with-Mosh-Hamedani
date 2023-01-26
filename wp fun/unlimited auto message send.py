import pyautogui as jb
import time

limit = input("Text Limit: ")
text = input("What's on your mind?\n").strip()
i = 1

time.sleep(9)
while i <= int(limit):
        jb.typewrite(text + ' ' + str(i))
        jb.press("Enter")
        i += 2