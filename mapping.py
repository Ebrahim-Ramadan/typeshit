from langdetect import detect

# Define a mapping from Arabic to English based on QWERTY keyboard layout
arabic_to_english_map = {
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't', 'غ': 'y', 'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p',
    'ج': '[', 'د': ']', 'ش': 'a', 'س': 's', 'ي': 'd', 'ب': 'f', 'ل': 'g', 'ا': 'h', 'ت': 'j', 'ن': 'k',
    'م': 'l', 'ك': ';', 'ط': '\'', 'ئ': 'z', 'ء': 'x', 'ؤ': 'c', 'ر': 'v', 'لا': 'b', 'ى': 'n', 'ة': 'm',
    'و': ',', 'ز': '.', 'ظ': '/', 'ذ': '`', '١': '1', '٢': '2', '٣': '3', '٤': '4', '٥': '5', '٦': '6',
    '٧': '7', '٨': '8', '٩': '9', '٠': '0', '': '-', '': '='
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

# Example usage
user_input = input('Type in Arabic: ')
corrected_input = detect_and_correct_text(user_input)
print("Corrected Input:", corrected_input)
