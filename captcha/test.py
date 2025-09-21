from selenium import webdriver

# Đường dẫn đến chromedriver
driver_path = 'E:\spacetech_antidetect_browser\chrome\orbita-browser-118\chrome'

# Tạo một phiên bản của trình duyệt
driver = webdriver.Chrome(executable_path=driver_path)

# Điều hướng đến trang web muốn chụp ảnh màn hình
driver.get('https://84skins.com/#/m/register')

# Chụp ảnh màn hình của một phần cụ thể của trang
element = driver.find_element_by_css_selector('.auth-body_')
element.screenshot('screenshot.png')

# Đóng trình duyệt
driver.quit()
