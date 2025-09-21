from gologin.factory import OrbitaCustom
import uuid
import time

mode = None
proxy = ""
port = ""

browser = OrbitaCustom()
profile_uuid = str(uuid.uuid4())
try:
    driver = browser.create_new(
        mode=mode,
        proxy=proxy,
        port=port,
        # name=profile_uuid,
        name="binance_test_1",
        executable_path=r"C:\Users\DELL\Documents\spacetech_antidetect_browser\chrome\orbita-browser-118\chrome.exe",
        chrome_driver_path=r"C:\Users\DELL\Documents\spacetech_antidetect_browser\chrome\chromedriver-118\chromedriver.exe",
        extensions_path=r"",
        headless_mode=False,
        profile_path=r"C:\Users\DELL\Documents\spacetech_antidetect_browser\custom_profile"
        # profile_path=r"/Users/baole/Desktop/bao_work/code/traffic-increaser-apps/custom_profile"
    )
    input("STOP")
except Exception as e:
    print(e)
finally:
    if driver:
        driver.close()
        driver.quit()
        # browser.stop(delete_profile=True)