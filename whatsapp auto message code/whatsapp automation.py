#Whatsapp auto message
import pyautogui as jabedkhanjb
import time

msg_limit = input("Enter the no. of message: ")
text_msg = input("Type something:\n")

i = 0
time.sleep(5)

while i < int(msg_limit):
    jabedkhanjb.typewrite(text_msg)
    jabedkhanjb.press("Enter")
    i += 1