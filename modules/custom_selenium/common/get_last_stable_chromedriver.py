"""
    Update chromedriver setup
"""
# ---- BASE PYTHON LIBS ----◹
import re
import zipfile
import os
import requests
# --------------------------◿

def update_chromedriver_to_last_stable_version(chrome_driver_folder_path : str):
    """
    Update chromedriver.exe to the last stable version.
    Based on link:
    https://googlechromelabs.github.io/chrome-for-testing/
    

    Args:
        chrome_driver_folder_path (str): Folder where chromedriver will be save
    """
    last_stable_version = get_chromedriver_last_stable_version()
    downloaded_zip_folder = download_the_last_stable_version(last_stable_version,
                                                             chrome_driver_folder_path)
    extract_chromedriver_file_from_zip(downloaded_zip_folder,
                                       chrome_driver_folder_path)

def get_chromedriver_last_stable_version() -> str:
    """
    Collect the latest stable version
    of Chromedriver available at the link:
    https://googlechromelabs.github.io/chrome-for-testing/

    Returns:
        str: Last stable version as string
    """
    url_chrome = 'https://googlechromelabs.github.io/chrome-for-testing/'
    page_html = requests.get(url_chrome, timeout=10).text
    version = re.findall(r'Stable\<\/a\>\<td\>\<code\>([\d\.]+)', page_html)[0]
    return version

def download_the_last_stable_version(version: str,
                                     download_folder_path : str) -> str:
    """
        Download latest stable version of Chromedriver.
        Based on the link:
        https://storage.googleapis.com/chrome-for-testing-public/{version}/win64/chromedriver-win64.zip
        


    Args:
        version (str): Version to be downloaded
        download_folder_path (str): Folder where downloaded files will be save

    Raises:
        requests.exceptions.HTTPError: Unable to download the latest
                                       version of Chromedriver

    Returns:
        str: Downloaded chromedriver path
    """
    download_url = (
    "https://storage.googleapis.com/chrome-for-testing-public/"
    f"{version}/win64/chromedriver-win64.zip")

    response = requests.get(download_url, timeout=10)

    if response.status_code == 200:
        file_path = os.path.join(download_folder_path, "chromedriver-win64.zip")
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
    raise requests.exceptions.HTTPError("Unable to download the latest version of Chromedriver")

def extract_chromedriver_file_from_zip(chromedriver_zip_folder_path : str,
                                       chromedriver_folder_path : str) -> None:
    """
    Extract chromedriver.exe from downloaded zip file

    Args:
        chromedriver_zip_folder_path (str): chromedriver downloaded zip path
        chromedriver_folder_path (str): Folder where chromedriver will be save
    """
    with zipfile.ZipFile(chromedriver_zip_folder_path, 'r') as zip_ref:
        zip_ref.extract(member='chromedriver-win64/chromedriver.exe',
                        path=chromedriver_folder_path)
    if os.path.exists(os.path.join(chromedriver_folder_path,'chromedriver.exe')):
        os.remove(os.path.join(chromedriver_folder_path,'chromedriver.exe'))

    os.rename(os.path.join(chromedriver_folder_path,r'chromedriver-win64\chromedriver.exe'),
        os.path.join(chromedriver_folder_path,'chromedriver.exe'))
    os.removedirs(os.path.join(chromedriver_folder_path,'chromedriver-win64'))
    os.remove(os.path.join(chromedriver_folder_path,'chromedriver-win64.zip'))
