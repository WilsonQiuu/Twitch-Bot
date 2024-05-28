from pynput import mouse, keyboard


def get_coords(x, y):
    print('Mouse coords: {0}, {1}'.format(x, y))

def on_press(key):
    try:
        if key.char == 'q':
            # Stop both listeners
            mouse_listener.stop()
            return False
    except AttributeError:
        pass

# Start the mouse listener
mouse_listener = mouse.Listener(on_move=get_coords)
mouse_listener.start()

# Start the keyboard listener
with keyboard.Listener(on_press=on_press) as keyboard_listener:
    keyboard_listener.join()

# Ensure the mouse listener is properly joined before exiting
mouse_listener.join()
