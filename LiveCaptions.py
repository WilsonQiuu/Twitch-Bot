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
    # Remove "Live Caption" from the beginning of each line
    cleaned_text = '\n'.join([line for line in text.split('\n') if line.strip() and line.strip() != "Live Caption"])
    return cleaned_text

def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]

def extract_new_text(prev_text, new_text):
    common_substring = longest_common_substring(prev_text, new_text)
    if common_substring:
        return new_text.split(common_substring, 1)[1].strip()
    return new_text

def hash_text(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

# Updated region where captions appear (x, y, width, height)
caption_region = (390, 305, 759, 295)

captured_text = []
seen_hashes = set()
output_file = 'captions.txt'
previous_text = ""

try:
    while True:
        screenshot = capture_screenshot(caption_region)
        text = extract_text_from_image(screenshot)
        text_hash = hash_text(text)

        if text_hash not in seen_hashes and text.strip():
            new_text = extract_new_text(previous_text, text)
            if new_text:
                seen_hashes.add(text_hash)
                captured_text.append(new_text)
                with open(output_file, 'a', encoding='utf-8') as file:
                    file.write(new_text + '\n')
                print(new_text)  # Print or save the new text
            previous_text = text
        time.sleep(1)  # Capture every second
except KeyboardInterrupt:
    # Stop capturing on keyboard interrupt
    pass

# Combine all captured text at the end (optional)
with open(output_file, 'a', encoding='utf-8') as file:
    file.write('\n'.join(captured_text))
