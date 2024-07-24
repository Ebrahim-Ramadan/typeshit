from pynput import keyboard
from langdetect import detect
import time  # Import time module for adding delay

# Defining a mapping from Arabic to English based on QWERTY keyboard layout
arabic_to_english_map = {
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't', 'غ': 'y', 'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p',
    'ج': '[', 'د': ']', 'ش': 'a', 'س': 's', 'ي': 'd', 'ب': 'f', 'ل': 'g', 'ا': 'h', 'ت': 'j', 'ن': 'k',
    'م': 'l', 'ك': ';', 'ط': '\'', 'ئ': 'z', 'ء': 'x', 'ؤ': 'c', 'ر': 'v', 'لا': 'b', 'ى': 'n', 'ة': 'm',
    'و': ',', 'ز': '.', 'ظ': '/', 'ذ': '`', '١': '1', '٢': '2', '٣': '3', '٤': '4', '٥': '5', '٦': '6',
    '٧': '7', '٨': '8', '٩': '9', '٠': '0', ' ': ' ', ',': ',', '.': '.', '/': '/', '`': '`', '-': '-',
    '=': '=', ';': ';', '\'': '\'', '[': '[', ']': ']', '\\': '\\'
}

def transliterate_arabic_to_english(text):
    return ''.join(arabic_to_english_map.get(char, char) for char in text)

def detect_and_correct_text(text):
    try:
        language = detect(text)
        if language == 'ar':
            corrected_text = transliterate_arabic_to_english(text)
            return corrected_text
        else:
            return text
    except Exception as e:
        print("Error detecting language:", e)
        return text

# Buffer to store the input text
input_buffer = []
last_processed_time = time.time()  # Initialize last processed time
current_keys = set()  # Set to keep track of currently pressed keys

def on_press(key):
    global last_processed_time, current_keys  # Access the global variables

    try:
        # Add key to the set of currently pressed keys
        if hasattr(key, 'char') and key.char:
            input_buffer.append(key.char)
        elif key == keyboard.Key.space:  # Handle space key
            input_buffer.append(' ')
        elif key == keyboard.Key.backspace:  # Handle backspace key
            if input_buffer:
                input_buffer.pop()
        elif key == keyboard.Key.enter:
            text = ''.join(input_buffer)
            input_buffer.clear()
            corrected_text = detect_and_correct_text(text)
            print("Converted Text:", corrected_text)
            return  # Exit the function to avoid additional processing
        
        current_keys.add(key)

        # Check if Ctrl + X is pressed
        if keyboard.Key.ctrl_l in current_keys and hasattr(key, 'char') and key.char == 'x':
            print("Ctrl + X pressed. Exiting...")
            return False  # Stop the listener and exit the script

        # Check time since last processing
        current_time = time.time()
        if current_time - last_processed_time >= 0.5:  # Delay of 0.5 seconds
            text = ''.join(input_buffer)
            corrected_text = detect_and_correct_text(text)
            print("Converted Text:", corrected_text)
            last_processed_time = current_time  # Update last processed time

    except Exception as e:
        print("Error processing key:", e)

def on_release(key):
    global current_keys  # Access the global variable

    try:
        # Remove key from the set of currently pressed keys
        current_keys.discard(key)
    except Exception as e:
        print("Error processing key release:", e)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Listening for all typing events. Converted text will be logged here.")
    listener.join()