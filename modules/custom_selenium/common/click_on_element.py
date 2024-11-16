"""
    Just a easy way to click on element
"""
# ------------------------ IMPORTED LIBS -----------------------◹
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Chrome
# --------------------------------------------------------------◿
def easy_wait_and_click(web_driver : Chrome,
                        xpath : str,
                        greed : bool,
                        search_time : float) -> None:
    """ 
        Wait for an element to appear and be clickable,
        after that clicks on the element

    Args:
        web_driver (Chrome): WebDrive hook
        xpath (str): Element xath
        search_time (float, optional): How long the search time
                                       needs to be.
        greed (bool, optional): Ignore overlapping elements that
                                intercepted the click.
    """
    if not greed:
        WebDriverWait(web_driver, search_time).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        web_driver.find_element('xpath', xpath).click()
        return

    while True:
        try:
            WebDriverWait(web_driver, search_time).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
            web_driver.find_element('xpath', xpath).click()
            break
        except ElementClickInterceptedException:
            pass
