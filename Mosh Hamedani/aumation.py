import pyautogui
import time
limit = input("Enter the no. of message: ")
text = input("Send text: ")

i = 0
while i < int(limit):
    pyautogui.typewrite(text)
    pyautogui.press("Enter")
    i += 1