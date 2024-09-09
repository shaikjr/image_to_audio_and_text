from PIL import Image
from gtts import gTTS
import pytesseract
import os
from playsound import playsound

# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert_to_sound(image):
    try:
        # Open the image
        open_image = Image.open(image)
        
        # Extract text using Tesseract
        text = pytesseract.image_to_string(open_image)
        text_file = " ".join(text.split("\n"))
        print(text_file)
        
        # Convert text to speech
        sound = gTTS(text_file, lang="en")
        sound.save("sound.mp3")
        
        # Play the sound
        playsound("sound.mp3")
        
        return True

    except Exception as bug:
        print("The error while executing the code\n", bug)
        return

if __name__ == "__main__":
    convert_to_sound("C:\imageaudio\__pycache__\ocr-test.png")
    input()
