"""
pip install selenium
https://pypi.org/project/selenium/
https://chromedriver.chromium.org/downloads
"""

from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(self.driver_path, options=self.options)


if __name__ == '__main__':
    chrome = ChromeAuto()
