from ultralytics import YOLO
from PIL import Image
from detection import YOLOVisualizer

output = YOLO('runs/detect/train/weights/best.pt')
img_path = "asset/captcha_73_jpg.rf.6f0fd71ce1f78bf0ba8ea6be4b260f44.jpg"
img = Image.open(img_path)
yolo_visualizer = YOLOVisualizer(output, Image.open(img_path))
yolo_visualizer.visualize_matching_boxes()

# Output sẽ có dạng [((x1,y1), w1, h1), ((x2.y2), w2, h2)]
# Với (x,y) là tọa độ của góc dưới bên trái của hình chữ nhật.
#  w, h lần lượt là chiều rộng và chiều cao của hình chữ nhật