"""
    Module responsible for creating an instance
    for a WebDriver (Chrome )and configuring it.
    As an additional feature, it has some functions
    that facilitate Selenium interactions with some elements.
"""
# ---- BASE PYTHON LIBS ----◹
import json
import os
from typing import Any
# --------------------------◿

# ------------------------ IMPORTED LIBS -----------------------◹
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from undetected_chromedriver import Chrome as UnChrome
from undetected_chromedriver import ChromeOptions as UnChromeOptions
# --------------------------------------------------------------◿
# ------------------------ LOCAL IMPORTS -----------------------◹
from modules.custom_selenium.common import (easy_wait_and_send_keys,
                                            easy_wait_and_click,
                                            alert_handle,
                                            download)
# --------------------------------------------------------------

class SetupWebDriver:
    """
        Configuration for a base selenium.
        Allows you to define the download path and the
        "headless" option, but it is not recommended
        for the testing phase.
    """
    def __init__(self,
                 download_path : str,
                 web_driver_path : str,
                 headless : bool = False,
                 undetected : bool = False) -> None:
        if not os.path.exists(download_path):
            os.mkdir(download_path)
        self.download_path   : str = download_path
        self.web_driver_path : str = web_driver_path
        self.headless : bool = headless or False
        self.undetected = undetected
        self.web_driver : Chrome = self.__config_and_start_a_webdriver()

    def __config_and_start_a_webdriver(self) -> Chrome:
        """
            Configure selenium and start a webdriver

        Returns:
            Chrome: Selenium driver ready to operate
        """
        if self.undetected:
            options : UnChromeOptions = UnChromeOptions()
        else:
            options : ChromeOptions = ChromeOptions()
        app_state : dict[str,str|int|list[dict[str,str]]] = {
            "recentDestinations": [
                {
                    "id": "Save as PDF",
                    "origin": "local" 
                }
            ],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }
        json_app_state = json.dumps(app_state)

        prefs : dict[str,Any]= {
                                'printing.print_preview_sticky_settings.appState': json_app_state,
                                'savefile.default_directory':self.download_path,
                                'download.prompt_for_download': False,
                                'download.directory_upgrade': True,
                                'plugins.always_open_pdf_externally': True,
                                'download.default_directory' : self.download_path}
        options.add_experimental_option("prefs",prefs)
        options.add_argument('--kiosk-printing')
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        if self.headless:
            options.add_argument("--headless=new")
        if self.undetected:
            chrome = UnChrome(service=Service(executable_path=self.web_driver_path,
                                              log_output='SELENIUM_LOGS'),
                              options=options,
                              driver_executable_path=self.web_driver_path)
        else:
            chrome = Chrome(service=Service(self.web_driver_path,log_output='SELENIUM_LOGS.txt'),
                            options=options)
        return chrome

    def accept_alert(self, search_time : float) -> str:
        """
            Search for a Alert in WebDriver instace
            and accept it.
            Sometime the alet is important, so i get
            it every time.

        Args:
            search_time (float): How long the search time needs to be

        Returns:
            str: Text present in alert body
        """
        alert_text = alert_handle(self.web_driver,
                                  search_time)
        return alert_text

    def click_on_element(self,
                         xpath : str,
                         search_time : float = 5,
                         greed : bool = False) -> None:
        """
            Wait for an element to appear and be clickable,
            after that clicks on the element

        Args:
            xpath (str): Web element xpath
            search_time (float): How long the search time needs to be
            greed (bool, optional): Ignore overlapping elements that
                                    intercepted the click.
        """
        easy_wait_and_click(self.web_driver,
                            xpath,
                            search_time,
                            greed)

    def send_keys_on_element(self,
                             xpath  : str,
                             keys : str,
                             clear: bool = True,
                             search_time : float = 5) -> None:
        """
            Wait for an element to appear and be clickable,
            after which Selenium cleans the element, if necessary,
            and sends the information

        Args:
            xpath (str): Web element xpath
            keys (str): keys to be inserted in element
            clear (bool, optional): Clear element before insertion?. Defaults to True.
            search_time (float): How long the search time needs to be
        """
        easy_wait_and_send_keys(self.web_driver,
                                xpath,
                                keys,
                                clear,
                                search_time)

    def click_on_download_button_and_wait_file(self,
                                               download_xpath : str,
                                               file_extension : list[str],
                                               search_time : float = 5)  -> str:
        """
            Click on download button, by the xpath in arguments,
            then wait it ends

        Args:
            download_xpath (str): Web element xpath
            search_time (float): How long the search time needs to be
            file_extension (str): Wanted file extension
            

        Returns:
            str: last download path
        """
        download(self.web_driver,
                 self.download_path,
                 download_xpath,
                 file_extension,
                 search_time)
