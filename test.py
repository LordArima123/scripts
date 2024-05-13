import pyautogui
import cv2
import numpy as np
import pyscreeze
screenshot = pyautogui.screenshot()

# Convert screenshot to OpenCV format
screenshot_cv = np.array(screenshot)
screenshot_cv = cv2.cvtColor(screenshot_cv, cv2.COLOR_RGB2BGR)