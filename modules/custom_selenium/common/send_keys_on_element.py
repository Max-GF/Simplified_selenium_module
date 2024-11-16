"""
    Just a easy way to send keys on element
"""
# ------------------------ IMPORTED LIBS -----------------------◹
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# --------------------------------------------------------------◿
def easy_wait_and_send_keys(web_driver : Chrome,
                            xpath  : str,
                            keys : str,
                            clear: bool = True,
                            search_time : float = 5) -> None:
    """
        Wait for an element to appear and be clickable,
        after which Selenium cleans the element, if necessary,
        and sends the information

    Args:
        web_driver (Chrome): WebDrive hook
        xpath (str): Web element xpath
        keys (str): keys to be inserted in element
        clear (bool, optional): Clear element before insertion?. Defaults to False.
        search_time (float): How long the search time needs to be
    """
    WebDriverWait(web_driver, search_time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    if clear:
        web_driver.find_element('xpath', xpath).clear()
    web_driver.find_element('xpath', xpath).send_keys(keys)
