import requests
import base64

# # Đọc ảnh và mã hóa base64
# with open("E:\\crawl\\captcha_binance\\pic\\xe đạp42.png", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Tạo payload
payload = {
    "url": "https://bin.bnbstatic.com/image/antibot/BOX/img/20240708/07/0803efeaffa146deb4a1f3a2a226b0a2.png",
    "entity": "xe đạp",
    "phone": "123456789"
}

# Gửi yêu cầu POST
response = requests.post("http://localhost:8000/post_captcha",json = payload)

# In phản hồi
print(response.json())

