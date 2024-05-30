import pytesseract
import pyautogui
from PIL import Image, ImageEnhance, ImageFilter
import time
import hashlib

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_screenshot(region):
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

def preprocess_image(image):
    # Convert to grayscale
    image = image.convert('L')
    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    # Apply a threshold filter
    image = image.point(lambda x: 0 if x < 140 else 255, '1')
    return image

def extract_text_from_image(image):
    image = preprocess_image(image)
    custom_config = r'--oem 3 --psm 6'  # LSTM OCR Engine, Assume a single uniform block of text
    text = pytesseract.image_to_string(image, config=custom_config, lang='eng')
    return text

def hash_text(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

# Define the region where captions appear (x, y, width, height)
caption_region = (100, 100, 600, 200)  # Adjust this based on your screen resolution

captured_text = []
seen_hashes = set()

try:
    while True:
        screenshot = capture_screenshot(caption_region)
        text = extract_text_from_image(screenshot)
        text_hash = hash_text(text)

        if text_hash not in seen_hashes:
            seen_hashes.add(text_hash)
            captured_text.append(text)
            print(text)  # Print or save the new text
        time.sleep(1)  # Capture every second
except KeyboardInterrupt:
    # Stop capturing on keyboard interrupt
    pass

# Combine all captured text
full_text = '\n'.join(captured_text)
print(full_text)
