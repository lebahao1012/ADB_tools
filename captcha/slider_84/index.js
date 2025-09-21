const puppeteer = require('puppeteer')

async function run() {
    const browser = await puppeteer.launch({
        headless: false,
        defaultViewport: { width: 1366, height: 768 }
    })
    const page = await browser.newPage()

    await page.evaluateOnNewDocument(() => {
        Object.defineProperty(navigator, 'webdriver', {
            get: () => false
        })
    })

    await page.goto('https://84skins.com/#/p/home')

    const elements = await page.$x('/html/body/div[1]/div/div/div[3]/div[2]/div/div[10]/div[1]')
    if (elements.length > 0) {
        await elements[0].click();
    } else {
        console.error('Element not found');
    }
    // await page.type('#password', 'password123')

    // let SliderElement = await page.$('.slidetounlock')
    // let slider = await SliderElement.boundingBox()

    // let SliderHandle = await page.$('.nc_iconfont.btn_slide')
    // let handle = await SliderHandle.boundingBox()

    // await page.mouse.move(handle.x + handle.width / 2, handle.y + handle.height / 2)
    // await page.mouse.down()
    // await page.mouse.move(handle.x + slider.width, handle.y + handle.height / 2, { steps: 50 })
    // await page.mouse.up()

    // success!

    await browser.close()
}

run()