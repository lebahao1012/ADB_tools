import cv2

def find_area(image_path):
    # Đọc ảnh từ đường dẫn
    img = cv2.imread(image_path)
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]

    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    
    for contour in contours:
        for point in contour:
            x, y = point[0]
            if 40 <= x <= 250:
                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y
    
    print(min_x, min_y, max_x, max_y)
    cv2.rectangle(img, (max_x, max_y), (min_x, min_y), (0, 255, 0), 2)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Gọi hàm để thực thi
find_area('Captcha4.PNG')