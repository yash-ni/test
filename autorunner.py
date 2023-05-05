import pyautogui
from time import sleep

while True:
    for _ in range(3):
        pyautogui.moveRel(0, 1000, duration=1)
        sleep(1)
        pyautogui.moveRel(1000, 0, duration=1)
        sleep(1)
        pyautogui.click()
        sleep(1)
        pyautogui.moveRel(0, -1000, duration=1)
        sleep(1)
        pyautogui.moveRel(-1000, 0, duration=1)
        sleep(1)
    sleep(10)

# Trying to revert this now.