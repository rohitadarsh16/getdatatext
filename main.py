import pytesseract
from PIL import Image
import os

def get_image_text(filename):
    myconfig = "--psm 6 --oem 3"
    current_directory = os.getcwd()
    filepath = os.path.join(current_directory, filename)
    # text = pytesseract.image_to_string(Image.open(filename), config=myconfig)
    text = pytesseract.image_to_string(Image.open(filepath))
    return text



image_filename ="image.jpg"

print(get_image_text(image_filename))



import pytesseract
from PIL import Image

def get_image_text(filepath):
    myconfig = "--psm 6 --oem 3"
    text = pytesseract.image_to_string(Image.open(filepath), config=myconfig)
    return text

image_filepath = r"C:\ekbet\Screenshot (107).png"

print(get_image_text(image_filepath)
