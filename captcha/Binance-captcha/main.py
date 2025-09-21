# from roboflow import Roboflow
# rf = Roboflow(api_key="sfmPRKqONOKcZnohRIYz")
# project = rf.workspace("hao-wsfav").project("binance_ci")
# model = project.version(1).model
# from ultralytics import YOLO

# model = YOLO("yolov8n-cls.pt")  # load an official model
# results = model("E:\crawl\captcha_binance\cutpic\con voi8_0_0.png")
# infer on a local image
# print(model.predict("E:\crawl\captcha_binance\cutpic\con voi8_0_0.png").json())

# visualize your prediction
# model.predict("your_image.jpg").save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True).json())

from loguru import logger
from ultralytics import YOLO
from PIL import Image

# Path to the downloaded model file
model_path = 'yolov8n-cls-trained-10.pt'

# Load the model
model = YOLO(model_path)
img = "E:\\crawl\\captcha_binance\\pic\\xe đạp42.png"
entity = "bike"
image = Image.open(img)

def detector(img_base64,entity):
    # im = Image.open(input)
    print('entity: ',entity)
    xPieces, yPieces = 3 , 3
    imgwidth, imgheight = img_base64.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    result = []
    q = 1
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = img_base64.crop(box)
            try:
                results = model(a,verbose=False)
                cls = results[0].probs.top1
                x = results[0].names[cls]
                if entity == x:
                    result.append(q)
                q += 1
            except Exception as e:
                logger.error(e)
                pass
    return result

# # You can now use the model for inference or further tasks
# # For example, to predict on an image:
# results = model.predict('E:\crawl\captcha_binance\cutpic\con voi500_1_0.png')

# cls = results[0].probs.top1
# x = results[0].names[cls]
# # Print the prediction results
# print(results)
# print(x)
rs = detector(image, entity)
print(rs)