import cv2
from loguru import logger
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Path to the downloaded model file
model_path = 'yolov8m-obb.pt'

# Load the model
model = YOLO(model_path)
# model = YOLO('best.pt')

# Load the image using PIL
img = "output_image_0.png"
image = Image.open(img)

# Convert the image to RGB if it has an alpha channel (RGBA)
if image.mode == 'RGBA':
    image = image.convert('RGB')

# Convert the image to a NumPy array
image_np = np.array(image)

# Run the model on the NumPy array image
results = model(image, show = True)

# # Print the results
# print(results)
