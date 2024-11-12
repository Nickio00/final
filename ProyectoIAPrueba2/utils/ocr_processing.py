# ocr_processing.py
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    
    # Mejorar la claridad de la imagen
    img = img.convert('L')  # Convertir a escala de grises
    img = img.filter(ImageFilter.SHARPEN)  # Aplicar un filtro de nitidez
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)  # Aumentar el contraste
    
    # Extraer texto
    text = pytesseract.image_to_string(img)
    return text
