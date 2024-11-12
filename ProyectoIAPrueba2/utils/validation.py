# validation.py
from datetime import datetime
import re

def validate_surname(text):
    # Buscar las frases clave que indican el apellido
    surname_patterns = [
        r'(Apellido|Surname|Last Name)[^\w]*([A-Za-z]+)',  # Busca las palabras clave y captura el apellido
        r'(Apellido|Surname|Last Name)\s*[:;]?\s*([A-Za-z]+)'  # Permite algunos separadores después de la palabra clave
    ]
    
    for pattern in surname_patterns:
        match = re.search(pattern, text)
        
        if match:
            surname = match.group(2)  # El apellido está en el segundo grupo de la expresión regular
            print(f"Apellido detectado: {surname}")
            return surname  # Retorna el apellido encontrado
    return "No se encontró apellido"



def validate_expiration_date(text):
    # Buscar variaciones de la frase que podría contener la fecha de vencimiento
    date_of_issue_pattern = r'(Date of expiry)[^\d]*(\d{1,2}\s+[A-Za-z]{3}\s+\d{2,4})'

    match = re.search(date_of_issue_pattern, text)
    
    if match:
        # Extraemos la fecha encontrada después de la frase clave
        expiration_date_str = match.group(2)
        print(f"Fecha de vencimiento encontrada: {expiration_date_str}")
        
        # Convertir la fecha en formato texto (Ejemplo: "13 FEB 2033") a un objeto datetime
        try:
            expiration_date = datetime.strptime(expiration_date_str, '%d %b %Y')  # Formato: "13 FEB 2033"
            # Comprobamos si la fecha está expirada
            if expiration_date > datetime.now():
                return "Documento válido"
            else:
                return "Documento expirado"
        except ValueError:
            return "Formato de fecha no válido"
    
    return "No se encontró fecha de vencimiento"

def validate_document_authenticity(text):
    # Expresión regular para detectar números con puntos (Ejemplo: 27.345.231)
    document_regex = r'\b\d{2}\.\d{3}\.\d{3}\b'

    # Buscar el número de identificación con puntos en el texto
    match = re.search(document_regex, text)
    
    if match:
        document_number = match.group(0)  # Obtener el número de documento encontrado
        print(f"Número de documento encontrado: {document_number}")
        return True  # Si se encuentra el número válido con puntos
    else:
        return False  # Si no se encuentra el número con puntos