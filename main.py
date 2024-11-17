# ---- BASE PYTHON LIBS ----◹
import os
# --------------------------◿
# ------------------------ IMPORTED LIBS -----------------------◹
from dotenv import load_dotenv
# --------------------------------------------------------------◿

# ------------------------ LOCAL IMPORTS -----------------------◹
from modules import CustomSelenium
# --------------------------------------------------------------

load_dotenv()

TEST_LINK : str = os.getenv("TEST_LINK",
                            "https://play1.automationcamp.ir/")
DOWNLOAD_PATH : str = os.getenv("DOWNLOAD_PATH",
                                os.getcwd())
CHROME_DRIVER_PATH  : str = os.getenv("CHROME_DRIVER_PATH",
                                      os.getcwd())

def test_custom_selenium() -> None:
    custom_selenium = CustomSelenium(
        download_path=DOWNLOAD_PATH,
        web_driver_path=CHROME_DRIVER_PATH
    )
    custom_selenium.web_driver.get(TEST_LINK)
    custom_selenium.click_on_element('/html/body/div[2]/div[3]/div[1]/div/div[2]/a')
    custom_selenium.click_on_element('//*[@id="user"]')
    custom_selenium.send_keys_on_element('//*[@id="user"]',"admin")
    custom_selenium.click_on_element('//*[@id="password"]')
    custom_selenium.send_keys_on_element('//*[@id="password"]',"admin")
    custom_selenium.click_on_element('//*[@id="login"]')
    custom_selenium.click_on_element('//*[@id="rad_medium"]')
    custom_selenium.click_on_element('//*[@id="select_flavor"]')
    custom_selenium.click_on_element('//*[@id="select_flavor"]/option[3]')
    custom_selenium.click_on_element('//*[@id="rad_barbeque"]')
    custom_selenium.click_on_element('//*[@id="onions"]')
    custom_selenium.send_keys_on_element('//*[@id="quantity"]',"3")
    custom_selenium.click_on_element('//*[@id="submit_button"]')
    input('Please, if you wanna close the WebDriver, just press "Enter" on terminal')

if __name__ == "__main__":
    test_custom_selenium()
