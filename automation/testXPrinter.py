import cv2
import numpy as np
import pyautogui
import time

def find_button_on_screen(button_image_path, screenshot_path):
    # Load the images
    button_image = cv2.imread(button_image_path, cv2.IMREAD_GRAYSCALE)
    screenshot = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)

    # Use template matching to find the button on the screen
    result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # If match is found with high confidence
    threshold = 0.6
    if max_val >= threshold:
        button_height, button_width = button_image.shape
        button_center = (max_loc[0] + button_width // 2, max_loc[1] + button_height // 2)
        return button_center
    else:
        return None

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot_path = 'screenshot.png'
    screenshot.save(screenshot_path)
    return screenshot_path

# Allow some time to switch to the GUI application
time.sleep(5)

# Path to the image of the button
button_image_path = 'Xprinter/test.png'

# Take a screenshot of the current screen
screenshot_path = take_screenshot()

# Find the button on the screen
button_center = find_button_on_screen(button_image_path, screenshot_path)

if button_center:
    # Move the mouse to the center of the button and click it
    pyautogui.moveTo(button_center)
    pyautogui.click()
    print(f"Clicked the button at {button_center}")
else:
    print("Button not found on the screen")