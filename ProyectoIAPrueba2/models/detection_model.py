# models/detection_model.py
import cv2
import numpy as np

def check_watermark(image_path):
    """
    Intenta detectar la presencia de una marca de agua o patrón usando técnicas de procesamiento de imágenes.
    """
    image = cv2.imread(image_path, 0)  # Lee la imagen en escala de grises
    _, thresh = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)  # Umbral para resaltar áreas oscuras

    # Usar transformada de contornos para buscar patrones en el documento
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Simple heurística para verificar cantidad de contornos
    if len(contours) > 10:
        return "Posible marca de agua detectada"
    else:
        return "No se detectó marca de agua"

def detect_document_edges(image_path):
    """
    Detecta los bordes del documento y verifica si tiene una forma rectangular, 
    que es común en documentos de identidad válidos.
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Detectar contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Encontrar contorno con forma de rectángulo
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:  # Contorno con 4 lados, probablemente un rectángulo
            return "Forma rectangular detectada: posible documento válido"
    return "No se detectó forma rectangular en el documento"

def validate_document_structure(image_path):
    """
    Aplica verificaciones para detectar si la estructura del documento coincide con las esperadas.
    """
    watermark_status = check_watermark(image_path)
    edge_status = detect_document_edges(image_path)
    
    return {
        "watermark_status": watermark_status,
        "edge_status": edge_status
    }
