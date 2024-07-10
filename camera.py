import cv2
import datetime

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise ValueError("Cannot open camera")

    ret, frame = cap.read()
    if not ret:
        cap.release()
        raise ValueError("Can't receive frame (stream end?). Exiting ...")

    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    image_path = f'static/captured_{timestamp}.png'
    
    if frame is None:
        cap.release()
        raise ValueError("Frame is empty")
    
    cv2.imwrite(image_path, frame)
    cap.release()
    
    return image_path
