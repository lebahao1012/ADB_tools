const puppeteer = require('puppeteer');
const fs = require('fs');

(async() => {
    const browser = await puppeteer.launch({
        headless: false, // Nếu muốn xem trình duyệt hoạt động, đặt headless: true để ẩn giao diện trình duyệt
    });

    const page = await browser.newPage();
    await page.goto('https://84skins.com/#/m/register');

    // Đợi cho trang web tải hoàn tất
    await page.waitForSelector('.auth-canvas1_'); // Chờ cho element .auth-canvas1_ xuất hiện

    // Tạo hàm để chuyển canvas thành dữ liệu URL của hình ảnh
    async function canvasToDataURL(canvasSelector) {
        const dataURL = await page.evaluate((selector) => {
            const canvas = document.querySelector(selector);
            return canvas.toDataURL('image/png');
        }, canvasSelector);
        return dataURL;
    }

    // Chuyển đổi các canvas thành dữ liệu URL của hình ảnh bằng cách gọi hàm canvasToDataURL
    const img1 = await canvasToDataURL('.auth-canvas1_');
    const img2 = await canvasToDataURL('.auth-canvas2_');
    const img3 = await canvasToDataURL('.auth-canvas3_');

    // Lưu các dữ liệu URL vào các tệp PNG
    await saveDataURLToPNG(img1, 'canvas1.png');
    await saveDataURLToPNG(img2, 'canvas2.png');
    await saveDataURLToPNG(img3, 'canvas3.png');

    console.log('Đã lưu các hình ảnh thành công.');

    // Đóng trình duyệt khi hoàn thành
    await browser.close();
})();

// Hàm để lưu dữ liệu URL vào tệp PNG
async function saveDataURLToPNG(dataURL, filename) {
    // Tạo buffer từ dữ liệu URL
    const buffer = Buffer.from(dataURL.split(',')[1], 'base64');
    // Ghi buffer vào tệp PNG
    fs.writeFileSync(filename, buffer);
}