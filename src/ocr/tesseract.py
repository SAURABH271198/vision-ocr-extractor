from pytesseract import image_to_string
from PIL import Image

def extract_text(image_path):
    """Extract raw text from an image using Tesseract OCR."""
    img = Image.open(image_path)
    return image_to_string(img)
