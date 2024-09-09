from PIL import Image
from gtts import gTTS
import pytesseract
from playsound import playsound
import os

# Tesseract path setup (if not already set in main script)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def image_to_sound(image):
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
