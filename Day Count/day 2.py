import pyautogui
import time


text = input("Text: ")
limit = input("Number of message you want to send : ")
i = 0
time.sleep(2)
while i < int(limit):
    i += 1
    pyautogui.typewrite(text)
    pyautogui.press("Enter")
