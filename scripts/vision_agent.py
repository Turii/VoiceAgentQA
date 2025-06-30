from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # автоматично скачається, якщо не маєш

def analyze_image(image_path):
    results = model(image_path)
    results[0].save(filename="media/output_labeled.jpg")
    names = results[0].names
    detected = [names[int(cls)] for cls in results[0].boxes.cls]
    return list(set(detected))