import pyautogui as jb
import time

limit = int(input("Enter the no. of messages: "))
message = input("Send text\n: ")

i = 0
time.sleep(10)
while i < limit:
    jb.typewrite(message)
    jb.press("Enter")
    i += 1