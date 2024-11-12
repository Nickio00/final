# capture_document.py
import cv2

def capture_image():
    cap = cv2.VideoCapture(1)  # Usa la cámara predeterminada
    width = 1280  # Ancho deseado
    height = 720  # Altura deseada
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

     # Coordenadas del rectángulo centrado
    rect_width = 800
    rect_height = 450
    rect_x = (width - rect_width) // 2
    rect_y = (height - rect_height) // 2

    while True:
        ret, frame = cap.read()
        if not ret:
            break
          # Dibuja el texto en la parte superior
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'Ubique el documento de identidad', (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

         
        # Dibuja un rectángulo centrado
        cv2.rectangle(frame, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (0, 255, 0), 2)

        
        cv2.imshow("Captura de Documento", frame)

        # Presiona 'c' para capturar la imagen
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite("captured_document.jpg", frame)
            print("Imagen capturada")
            break
        
         # Presiona "Esc" para cerrar
        if cv2.waitKey(1) & 0xFF == 27:  # El valor 27 corresponde a la tecla Esc
            print("Se ha cerrado el sistema")
            break
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()
