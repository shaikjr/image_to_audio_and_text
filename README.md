# Image-to-Speech Converter using Python

This project converts text from images into speech using Python. It uses Optical Character Recognition (OCR) to extract text from images and then converts the text into speech using Google's Text-to-Speech (gTTS) API.

## Features
- Extracts text from images using Tesseract OCR.
- Converts extracted text into speech.
- Automatically plays the generated audio file.

## Technologies Used
- **Python**: Programming language.
- **Pillow**: Library for image processing.
- **pytesseract**: For Optical Character Recognition (OCR).
- **gTTS**: Google Text-to-Speech API.
- **playsound**: For playing the audio file.

## Prerequisites

Make sure you have the following installed:

- **Python 3.x**
- **Tesseract-OCR**: You can download it from the [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract) or the [official website](https://tesseract-ocr.github.io/tessdoc/Installation.html).

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/image-to-speech-converter.git
    cd image-to-speech-converter
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file should contain the following:

    ```txt
    Pillow
    pytesseract
    gTTS
    playsound
    ```

3. Set the path to Tesseract in `app.py` or `new.py`:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```

### Usage

1. Place the image from which you want to extract text in the project directory.
2. Run the Python script:
    ```bash
    python app.py
    ```

The script will extract text from the image and convert it to speech. The output audio will be saved as `sound.mp3` and played automatically.

## Example

### Input Image:
![ocr-test](https://github.com/user-attachments/assets/4b3c8968-d5e1-4861-9c8c-e838239ac28a)
### Output:
![Screenshot 2024-09-09 112009](https://github.com/user-attachments/assets/c8f0ac56-a374-4845-842f-cfcea25a35fe)
- The extracted text will be printed in the console.
- The speech will be saved as `sound.mp3`.
