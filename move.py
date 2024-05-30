import time
import pyautogui

# Starting coordinates
start_x, start_y = 560, 715 # when the captions start on twitch
# start_x, start_y = 560, 380 # when the captions start by default
# Ending coordinates
end_x, end_y = 370, 260

# Duration of the drag (in seconds)
duration = 3

# Move the mouse to the starting position
pyautogui.moveTo(start_x, start_y)



# Drag the mouse to the ending position
pyautogui.dragTo(end_x, end_y, duration=duration)
