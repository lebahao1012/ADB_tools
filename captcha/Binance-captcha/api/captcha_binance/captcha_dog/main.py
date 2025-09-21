import os
from queue import Full
import requests
from ultralytics import YOLO
from loguru import logger
from PIL import Image
import io
import base64, time
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import numpy as np
from datetime import datetime
from pydantic import BaseModel

# Load a model
model = YOLO('yolov8n-cls-trained-10.pt').to('cpu')  # load a custom model
app = FastAPI()

class CaptchaImage(BaseModel):
    url: str
    entity: str
    phone: int
    
def getImage(url,phone):
    try:
        # Gửi yêu cầu GET tới URL
        response = requests.get(url)
        # Kiểm tra xem yêu cầu có thành công không
        response.raise_for_status()
        
        # Mở nội dung ảnh từ phản hồi
        image = Image.open(io.BytesIO(response.content))
        
        # Lưu ảnh vào đường dẫn được chỉ định
        save_path = f"pic/{phone}.png"
        image.save(save_path)
        logger.info(f'Ảnh đã được lưu tại {save_path}')
    except Exception as e:
        raise Exception(f'Có lỗi xảy ra: {e}')

def detectEntity(entity):
    if entity == "con voi":
        return "elephant"
    if entity == "gấu trúc":
        return "panda"
    if entity == "máy bay":
        return "plane"
    if entity == "xe đạp":
        return "bike"
    else:
        return "error"

def detector(img_base64,entity):
    # im = Image.open(input)
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

def get_element_selector(arr):
    result = []
    count = 0
    for value in arr:
        if value == 1:
            result.append(".page1 .bcap-image11 > .bcap-image-cell-image")
            count += 1
        elif value == 2:
            result.append(".page1 .bcap-image12 > .bcap-image-cell-image")
            count += 1
        elif value == 3:
            result.append(".page1 .bcap-image13 > .bcap-image-cell-image")
            count += 1
        elif value == 4:
            result.append(".page1 .bcap-image21 > .bcap-image-cell-image")
            count += 1
        elif value == 5:
            result.append(".page1 .bcap-image22 > .bcap-image-cell-image")
            count += 1
        elif value == 6:
            result.append(".page1 .bcap-image23 > .bcap-image-cell-image")
            count += 1
        elif value == 7:
            result.append(".page1 .bcap-image31 > .bcap-image-cell-image")
            count += 1
        elif value == 8:
            result.append(".page1 .bcap-image32 > .bcap-image-cell-image")
            count += 1
        elif value == 9:
            result.append(".page1 .bcap-image33 > .bcap-image-cell-image")
            count += 1
        else:
            continue
    return result, count

@app.get("/")
async def root():
    return {"message": "captcha-ocr"}

@app.post("/upload", response_class=JSONResponse)
async def upload(data: CaptchaImage):
    try:
        url = data.url
        entity = detectEntity(data.entity)
        phone = data.phone
        
        # t1 = time.time()
        getImage(url,phone)
        image_path = f"pic/{phone}.png"
        image = Image.open(image_path)
        image_np = np.array(image)
        img = Image.fromarray(image_np)
        s = detector(img,entity)
        selector, count = get_element_selector(s)
        # t2 = time.time()
        # current_time = datetime.now().strftime("%Y-%m-%d_%H:%M")
    except Exception as e:
        return JSONResponse(
        status_code=500,
        content={
            "status": "failed",
            "data": str(e)
        })
    logger.info(f"entity: {entity}")
    logger.info(f"image_path: {image_path}")
    logger.info(f"data: {s}")
    if os.path.exists(image_path):
        os.remove(image_path)
        logger.info(f"The file {image_path} has been deleted.")
    else:
        logger.info(f"The file {image_path} does not exist.")
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "data": selector,
        })

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)