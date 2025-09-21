import base64

def read_txt_and_convert_to_image(file_path, output_image_path):
    try:
        # Đọc nội dung của file .txt
        with open(file_path, 'r') as file:
            content = file.read()

        # Tìm đoạn mã base64 từ nội dung (giả sử bắt đầu từ 'base64,' và kết thúc tại dấu ngoặc kép)
        base64_data = []
        lines = content.splitlines()
        for line in lines:
            if 'base64,' in line:
                start = line.find('base64,') + len('base64,')
                end = line.find('"', start)
                base64_str = line[start:end]
                base64_data.append(base64_str)
        
        # Lưu ảnh từ từng đoạn mã base64
        for idx, b64_data in enumerate(base64_data):
            image_data = base64.b64decode(b64_data)
            with open(f"{output_image_path}_{idx}.png", 'wb') as img_file:
                img_file.write(image_data)

        print("Ảnh đã được lưu thành công!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {str(e)}")

# Sử dụng hàm
read_txt_and_convert_to_image('SB_captcha.txt', 'output_image')
