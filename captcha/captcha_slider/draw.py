import cv2
import numpy as np

# Load the image
image = cv2.imread("/Users/baole/Desktop/bao_work/code/captcha/captcha_slider/background.png")  # Replace with your image file path

# Define the pixel position
x = 250  # Replace with the desired x-coordinate
y = 80  # Replace with the desired y-coordinate

# Define the color of the dot (in BGR format)
dot_color = (0, 0, 255)  # Red in BGR format

# Draw a dot at the specified position
cv2.circle(image, (x, y), 2, dot_color, -1)  # 2 is the radius, -1 is for filled dot

# Display the image with the dot
cv2.imshow("Image with Dot", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
