# Typeshit

![Typeshit Illustration](illustration.mp4)

Typeshit is a Python tool that detects and corrects text input, particularly useful for switching between Arabic and English typing.

## Installation

Install Typeshit using pip:
`pip install typeshit`
This will install the latest version already auto, It's recommended to use a virtual environment for isolated package management.
## Usage
in your python script:
```
from typeshit.main import autotypeshit

# Use the main function to start the keyboard listener
autotypeshit()
```

## How It Works

Typeshit uses a debounce mechanism to process input efficiently:

1. Each keypress triggers a timer reset.
2. If no keys are pressed within the debounce delay, the `process_buffer` function is called.
3. The function then processes the accumulated input, detecting the language and applying necessary corrections.

## Features

- Automatic language detection (Arabic/English)
- Real-time text correction
- Efficient input processing with debounce mechanism

## Development

For contributors and developers:

- `test.txt` is provided for input testing purposes.
- The main logic resides in `src/typeshit/main.py`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Ebrahim Ramadan - [ramadanebrahim791@gmail.com](mailto:ramadanebrahim791@gmail.com)

Project Link: [https://github.com/ebrahim-ramadan/wetype](https://github.com/ebrahim-ramadan/wetype)