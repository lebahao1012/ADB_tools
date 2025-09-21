import cv2
from matplotlib import pyplot as plt
import numpy as np

def find_white_color(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)
    
    # Chuyển đổi ảnh sang không gian màu HSV (Hue, Saturation, Value)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Đặt ngưỡng cho màu trắng trong không gian màu HSV
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 25, 255])
    
    # Tạo mask để tìm các điểm ảnh có màu trắng
    mask = cv2.inRange(hsv_image, lower_white, upper_white)
    
    # Tìm contours trong mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Tìm vùng có diện tích lớn nhất
    largest_area = 0
    largest_contour = None
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > largest_area:
            largest_area = area
            largest_contour = contour
    
    white_mask = np.zeros_like(mask)
    if largest_contour is not None:
        cv2.drawContours(white_mask, [largest_contour], -1, 255, -1)
        
        # Tính toán hình chữ nhật bao quanh
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Vẽ hình chữ nhật lên ảnh gốc
    
    cv2.imshow('Original Image', image)
    # Trả về mask của vùng màu trắng lớn nhất và tọa độ của hình chữ nhật
    return (x, y, w, h)

image_path = 'Captcha.PNG' 
rect_coords = find_white_color(image_path)

# Hiển thị kết quả
cv2.waitKey(0)
cv2.destroyAllWindows()

# rect_coords chứa tọa độ của hình chữ nhật (x, y, w, h)
print('Rectangle coordinates:', rect_coords)

def find_black_area_near_white(image_path):
    # Đọc ảnh từ đường dẫn
    img = cv2.imread(image_path)
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    for contour in contours:
        for point in contour:
            x, y = point[0]
            if 40 <= x <= 250:
                print(f"Point: ({x}, {y})")
                # Draw the point on the image (optional)
                cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
        # cv2.drawContours(img, contour, -1, (0, 255, 0), 3)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Gọi hàm để thực thi
find_black_area_near_white('Captcha2.PNG')
