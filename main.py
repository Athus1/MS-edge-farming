import pyautogui
import time
import string
import random
import subprocess

string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 10
#
x = 34

subprocess.Popen(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
time.sleep(5)
while x > 0:
    pyautogui.hotkey("ctrl", "t")
    while a > 0:
        pyautogui.write(random.choice(string.ascii_letters))
        a = a - 1
    pyautogui.press("enter")
    x = x - 1
    a = 10

    time.sleep(0.1)


string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 5
c = 20

time.sleep(5)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("bing.com")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("f12")
time.sleep(2)
#IF NEEDED ADD ABSOLUTE PATH OF IMAGE IN THE LINE BELOW
button7location = pyautogui.locateOnScreen(r'searchfind.png')
print(button7location)
button7point = pyautogui.center(button7location)
button7x, button7y = button7point
pyautogui.click(button7x, button7y)
while b > 0:
    pyautogui.write(random.choice(string.ascii_letters))
    b = b - 1
b = 5
pyautogui.press("enter")
time.sleep(2)
#IF NEEDED ADD ABSOLUTE PATH OF IMAGE IN THE LINE BELOW
button2location = pyautogui.locateOnScreen(r'phase2finder.png')
button2point = pyautogui.center(button2location)
print(button2point)
while c > 0:
    pyautogui.click(button2point)
    while b > 0:
        pyautogui.write(random.choice(string.ascii_letters))
        b = b - 1
    pyautogui.press("enter")
    c = c-1
    print(c)
    time.sleep(0.3)
    b = 5
