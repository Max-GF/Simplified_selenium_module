"""
    Alert handle setup
"""
# ---- BASE PYTHON LIBS ----◹
import time
# --------------------------◿

# ------------------------ IMPORTED LIBS -----------------------◹
from selenium.webdriver import Chrome
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
# --------------------------------------------------------------◿
def alert_handle(web_driver : Chrome,
                 search_time : float = 5) -> str:
    """
        Search for a Alert in WebDriver instace
        and accept it.
        Sometime the alet is important, so i get
        it every time.

    Args:
        web_driver (Chrome): WebDrive hook
        search_time (float, optional): How long the search time
                                       needs to be. Defaults to 5.

    Returns:
        str: Text present in alert body
    """
    while search_time >= 0:
        try:
            alert_text : str = Alert(web_driver).text
            Alert(web_driver).accept()
            break
        except NoAlertPresentException:
            time.sleep(0.1)
            search_time -= 0.1
    return {alert_text}
