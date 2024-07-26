from pynput import keyboard
from langdetect import detect
import time
from pynput.keyboard import Key, Controller
import threading

arabic_to_english_map = {
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't', 'غ': 'y', 'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p',
    'ج': '[', 'د': ']', 'ش': 'a', 'س': 's', 'ي': 'd', 'ب': 'f', 'ل': 'g', 'ا': 'h', 'ت': 'j', 'ن': 'k',
    'م': 'l', 'ك': ';', 'ط': '\'', 'ئ': 'z', 'ء': 'x', 'ؤ': 'c', 'ر': 'v', 'لا': 'b', 'ى': 'n', 'ة': 'm',
    'و': ',', 'ز': '.', 'ظ': '/', 'ذ': '`', '١': '1', '٢': '2', '٣': '3', '٤': '4', '٥': '5', '٦': '6',
    '٧': '7', '٨': '8', '٩': '9', '٠': '0', ' ': ' ', ',': ',', '.': '.', '/': '/', '`': '`', '-': '-',
    '=': '=', ';': ';', '\'': '\'', '[': '[', ']': ']', '\\': '\\'
}
# manual configs for the transilicteration or i dunno

def transliterate_arabic_to_english(text):
    return ''.join(arabic_to_english_map.get(char, char) for char in text)

def detect_and_correct_text(text):
    try:
        language = detect(text)
        print('read', language)
        if language == 'ar':
            corrected_text = transliterate_arabic_to_english(text)
            return corrected_text
        else:
            return text
    except Exception as e:
        print("err detecting language:", e)
        return text

input_buffer = []
last_key_time = time.time()
current_keys = set()
keyboard_controller = Controller()
debounce_timer = None
DEBOUNCE_DELAY = 0.5  


def process_buffer():
    global input_buffer
    if input_buffer:
        text = ''.join(input_buffer)
        corrected_text = detect_and_correct_text(text)
        
        # Type the corrected text
        keyboard_controller.press(Key.space) # type space (lol)
        keyboard_controller.type(corrected_text)
        
        keyboard_controller.press(Key.shift)
        for _ in range(len(corrected_text)):
            keyboard_controller.press(Key.left)
            keyboard_controller.release(Key.left)
        keyboard_controller.release(Key.shift)
        
        print("Converted Text:", corrected_text)
        input_buffer.clear()
    

def on_press(key): 
    global last_key_time, current_keys, debounce_timer

    try:
        if keyboard.Key.esc in current_keys and key == keyboard.Key.from_char('q'):
            print("Escape + Q pressed. Exiting...")
            return False  # This will stop the listener
# this scipt exiting doesnt work yet fuck have no idea
        if hasattr(key, 'char') and key.char:
            input_buffer.append(key.char)
        elif key == keyboard.Key.space:
            input_buffer.append(' ')
        elif key == keyboard.Key.backspace:
            if input_buffer:
                input_buffer.pop()
        elif key == keyboard.Key.enter:
            process_buffer()
            return

        current_keys.add(key)
        last_key_time = time.time()

        
        if debounce_timer is not None:
            debounce_timer.cancel()
        debounce_timer = threading.Timer(DEBOUNCE_DELAY, process_buffer)
        debounce_timer.start()

    except Exception as e:
        print("err processing key:", e)

def on_release(key):
    global current_keys
    try:
        current_keys.discard(key)
    except Exception as e:
        print("err processing key release:", e)


def autotypeshit():
    # Your existing code here
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Listening now for all typing events. Converted text will be logged here...")
        listener.join()

if __name__ == "__main__":
    autotypeshit()
    