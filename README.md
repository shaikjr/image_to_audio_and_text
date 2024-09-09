# Image-to-Speech Converter using Python

This project converts text from images into speech using Python. It uses Optical Character Recognition (OCR) to extract text from images and then converts the text into speech using Google's Text-to-Speech (gTTS) API.

## Features
- Extract text from images using Tesseract OCR
- Convert extracted text into speech
- Play the audio file automatically

## Technologies Used
- Python
- `Pillow` for image processing
- `pytesseract` for OCR
- `gTTS` for text-to-speech
- `playsound` for playing the audio file

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- Tesseract-OCR (download from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract) or [official website](https://tesseract-ocr.github.io/tessdoc/Installation.html))

### Python Packages
Install the required Python packages by running:
```bash
pip install -r requirements.txt
