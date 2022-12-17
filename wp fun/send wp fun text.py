import pyautogui as jb
import time

time.sleep(5)

text = open("animals.txt")

name = input("")
person = f"{name} is a"

for i in text:
	jb.write(person +' '+ i)
	jb.press("Enter")
