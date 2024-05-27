import time
import pyautogui
import random
from pynput import keyboard

# Coordinates for the buttons (top left and bottom right)
search_button_coords = ((663, 205), (850, 230))
first_stream_coords = ((450, 410), (700, 520))
chat_input_coords = ((1483, 1016), (1700, 1028))

# Define a flag to stop the script
stop_script = False

def on_press(key):
    global stop_script
    try:
        if key == keyboard.Key.esc:
            stop_script = True
            return False
    except AttributeError:
        pass

def get_random_coords(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    return x, y

def go_to(user):
    global stop_script

    if not stop_script:
        # Move to random point within search button and click
        search_coords = get_random_coords(*search_button_coords)
        print(f"Clicking search button at: {search_coords}")
        pyautogui.moveTo(search_coords[0], search_coords[1])
        pyautogui.click()
        time.sleep(0.5)
        
        # Type the search query
        print("Typing search query")
        pyautogui.write(user)
        pyautogui.press('enter')
        time.sleep(3)  # Short delay to allow search results to load

    if not stop_script:
        # Move to random point within first stream button and click
        stream_coords = get_random_coords(*first_stream_coords)
        print(f"Clicking first stream at: {stream_coords}")
        pyautogui.moveTo(stream_coords[0], stream_coords[1])
        pyautogui.click()

def send_message(message):
    global stop_script

    if not stop_script:
        # Move to random point within chat input and click
        chat_coords = get_random_coords(*chat_input_coords)
        print(f"Clicking chat input at: {chat_coords}")
        pyautogui.moveTo(chat_coords[0], chat_coords[1])
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        
    if not stop_script:
        # Type the message and press enter
        print("Typing chat message")
        pyautogui.write(message)
        pyautogui.press('enter')

# Start the keyboard listener
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Perform Alt+Tab to switch to the correct window immediately
print("Switching to the correct window")
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
time.sleep(1)  

# Example usage of the go_to and send_message functions
go_to('pixel gun 3d')

time.sleep(2)

send_message('Nice Guns')

# Ensure the keyboard listener is properly joined before exiting
keyboard_listener.join()
