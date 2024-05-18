import cv2
import pytesseract
import pyautogui
import time
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def find_text_on_screen(target_text):
    # Take a screenshot of the current screen
    screenshot = pyautogui.screenshot()
    
    # Convert the screenshot to a format suitable for OpenCV
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Use pytesseract to extract text and bounding boxes
    data = pytesseract.image_to_data(screenshot_cv, output_type=pytesseract.Output.DICT)
    
    # Iterate through the detected text elements
    for i in range(len(data['text'])):
        if target_text.lower() in data['text'][i].lower():
            # Extract the bounding box coordinates
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            return x + w // 2, y + h // 2  # Return the center of the bounding box
    
    return None

# Allow some time to switch to the GUI application
time.sleep(5)

# Text to find on the screen
target_text = "accept"

# Find the text on the screen
text_center = find_text_on_screen(target_text)

if text_center:
    # Move the mouse to the center of the text and click it
    pyautogui.moveTo(text_center)
    pyautogui.click()
    print(f"Clicked on the text '{target_text}' at {text_center}")
else:
    print(f"Text '{target_text}' not found on the screen")