import pyautogui as jb
import time
limit = input("Enter no. of messages: ")
msg = input("Message you want to send: ")

i = 0

time.sleep(10)

while i < int(limit):
    jb.typewrite(msg)
    jb.press('Enter')
    i += 1


