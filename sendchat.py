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


initialMessages = [
    "Hey",
    "Hi",
    "Yo",
    "Wassup",
    "What's up",
    "Eyyo",
    "Hey there",
    "Hi guys",
    "Howdy",
    "Wassup chat",
    "Hey folks",
    "Greetings",
    "What's good?",
    "Hey y'all!"
]

secondaryMessages = [
    "How's everyone doing today?",
    "What are you guys up to?",
    "How's the stream going?",
    "Anyone got any plans for the weekend?",
    "What did I miss so far?",
    "How's it going?",
    "Any good games lately?",
    "What's everyone playing?",
    "How's the vibe today?",
    "What's new with you all?",
    "Any recommendations for games?",
    "What are we watching?",
    "How's your day going?",
    "What’s everyone chatting about?",
    "What’s the highlight of the stream so far?",
    "What’s been happening?",
    "Any cool moments in the stream?",
    "How’s the streamer doing?",
    "What are we discussing?",
    "Any fun stuff going on?"
]

thirdMessages = [
    ["I'm doing great, just chilling!", "Not bad, how about you?", "Pretty good, thanks for asking!"],
    ["Just hanging out, you?", "Not much, what about you?", "Watching some streams, you?"],
    ["It's awesome, loving the content!", "Great, the streamer is on fire!", "Really enjoying it!"],
    ["Just relaxing, maybe some gaming.", "Not sure yet, what about you?", "Thinking of some outdoor activities."],
    ["Just got here too, let's find out!", "Not sure, just tuned in.", "Catching up from the start!"],
    ["Pretty good, you?", "All good here, thanks!", "Going well, how's yours?"],
    ["Playing a bit of everything, you?", "Loving some RPGs lately, you?", "Mostly shooters, what about you?"],
    ["Just started a new RPG, you?", "Mixing it up, what about you?", "Playing some classics, you?"],
    ["Vibe is great, loving the energy.", "Pretty chill, how's yours?", "Really good, enjoying the chat."],
    ["Not much, how about you?", "Just the usual, you?", "Catching up on streams, you?"],
    ["Depends on what you like, any genre?", "Try the new releases, they are fun!", "Some indie games are great!"],
    ["Catching up on the latest content.", "A mix of everything, you?", "Some gameplay and chat, you?"],
    ["Good, just relaxing.", "Not bad, thanks!", "Pretty well, you?"],
    ["Just chatting about games mostly.", "Some random topics, you?", "Games and more, you?"],
    ["The gameplay is awesome!", "Some great moments here!", "Really enjoying the highlights!"],
    ["Just the usual, you?", "Not much, just chilling.", "Same old, what about you?"],
    ["Some epic gameplay moments!", "A few great clips!", "Loving the stream highlights!"],
    ["Streamer's doing great, very interactive!", "Really enjoying the streamer!", "Streamer's energy is awesome!"],
    ["Games, mostly. You?", "A bit of everything, you?", "Some random topics, you?"],
    ["Some fun discussions!", "A lot of interesting chats.", "Great conversations happening!"]
]



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
