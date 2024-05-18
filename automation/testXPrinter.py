import pyautogui
import time
import subprocess
import cv2
# Xprinter = "Driver/XPrinter.exe"
# subprocess.Popen(["runas","/user:Administrator",Xprinter])
while True:
    try:
        agreeLocation = pyautogui.locateOnScreen("Xprinter/agree.png",confidence=0.7)   
        x,y = pyautogui.center(agreeLocation)
        pyautogui.click(x,y)
        time.sleep(1)

        nextx,nexty = pyautogui.locateCenterOnScreen("Xprinter/next.png")
        pyautogui.click(nextx,nexty)
        time.sleep(1)
        pyautogui.click(nextx,nexty)
        time.sleep(2)
        shortx,shorty = pyautogui.locateCenterOnScreen("Xprinter/shortcut.png")
        pyautogui.click(shortx,shorty)
        time.sleep(0.5)
        pyautogui.click(nextx,nexty)
        time.sleep(1)
        pyautogui.click(nextx,nexty)
        time.sleep(10)
        pyautogui.click(nextx,nexty)

        time.sleep(2.5)
        pyautogui.click(pyautogui.locateCenterOnScreen("Xprinter/usb.png")) 
        pyautogui.click(pyautogui.locateCenterOnScreen("Xprinter/XP-80C.png")) 
        pyautogui.click(nextx,nexty)
        time.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen("Xprinter/no.png"))
        break
    except :
        print("Rerunning the program")