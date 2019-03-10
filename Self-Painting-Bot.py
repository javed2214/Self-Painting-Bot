# Painting Bot using PyautoGUI

import pyautogui
import time
import subprocess

subprocess.Popen(r"C:/WINDOWS/system32/mspaint.exe")

time.sleep(6)
pyautogui.moveTo(300,300)

pyautogui.click()
distance = 300

while distance > 0:
    pyautogui.dragRel(distance, 0, duration = 0.1)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration = 0.1)
    pyautogui.dragRel(-distance, 0, duration = 0.1)
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration = 0.1)
    
    
