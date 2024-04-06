import pyautogui
from time import sleep
N  = int(input())

sleep(5)
for i in range(N+1):
    for j in range(i):
        pyautogui.write('#')
    pyautogui.press('enter')
    





