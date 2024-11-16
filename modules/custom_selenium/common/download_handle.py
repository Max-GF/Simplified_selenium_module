"""
    Download handle setup
"""
# ---- BASE PYTHON LIBS ----◹
import time
import os
# --------------------------◿
# ------------------------ IMPORTED LIBS -----------------------◹
from selenium.webdriver import Chrome
# --------------------------------------------------------------◿
# ------------------------ LOCAL IMPORTS -----------------------◹
from modules.custom_selenium.common.click_on_element import easy_wait_and_click
# --------------------------------------------------------------◿
def download(web_driver : Chrome,
             download_folder_path: str,
             download_xpath : str,
             file_extension : list[str],
             search_time : float)  -> str:
    """
        Click on download button, by the xpath in arguments,
        then wait it ends

    Args:
        download_folder_path (str) : Folder where downloaded files will be save
        web_driver (Chrome): WebDrive hook
        download_xpath (str): Web element xpath
        file_extension (str): Wanted file extension
        search_time (float, optional): How long the search time
                                needs to be. Defaults to 5.

    Returns:
        str: last download path
    """
    previous_folder_state : list = os.listdir(download_folder_path)
    easy_wait_and_click(web_driver,
                        download_xpath,
                        False,
                        search_time)
    after_folder_state : list = os.listdir(download_folder_path)
    while previous_folder_state == after_folder_state:
        time.sleep(0.5)
        after_folder_state = os.listdir(download_folder_path)
    last_download : str = most_recent_file(download_folder_path)
    while not  f'.{last_download.split('.')[-1]}' in file_extension:
        time.sleep(0.5)
        last_download = most_recent_file(download_folder_path)
    time.sleep(1)
    last_download = most_recent_file(download_folder_path)
    return last_download

def most_recent_file(download_folder_path: str) -> str:
    """
        Read download path and look for
        the most rescent file

    Returns:
        str: Most recent file of a folder path as a string 
    """
    files = os.listdir(download_folder_path)
    paths = [os.path.join(download_folder_path, basename) for basename in files]
    return max(paths, key=os.path.getctime)
