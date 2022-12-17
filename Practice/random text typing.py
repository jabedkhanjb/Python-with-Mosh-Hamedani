import pyautogui as jb
import time
msg_limit = input("Enter the no. of message: ")
text = input("Enter your text:\n> ")
countdown = 0
time.sleep(5)
while countdown < int(msg_limit):
    jb.typewrite(text)
    jb.press("Enter")
    countdown += 1

