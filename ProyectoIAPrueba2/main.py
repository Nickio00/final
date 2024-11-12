# main.py
from utils.capture_document import capture_image
from utils.ocr_processing import extract_text_from_image
from utils.validation import validate_expiration_date, validate_document_authenticity, validate_surname
from models.detection_model import validate_document_structure

def main():
    capture_image()
    image_path = "captured_document.jpg"
    text = extract_text_from_image(image_path)

    # Validación de estructura del documento
    structure_validation = validate_document_structure(image_path)
    print("Resultado de validación de estructura del documento:", structure_validation)

    # Validación de autenticidad del documento
    if validate_document_authenticity(text):
        print("Documento válido.")
    else:
        print("Documento no válido.")

    # Validación de fecha de expiración
    expiration_status = validate_expiration_date(text)
    print(expiration_status)

    surname = validate_surname(text)
    print(surname)


if __name__ == "__main__":
    main()
