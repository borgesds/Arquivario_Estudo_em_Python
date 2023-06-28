"""
pip install selenium
https://pypi.org/project/selenium/
https://chromedriver.chromium.org/downloads
"""

from selenium import webdriver
from time import sleep


class CookieClicker:
    def __init__(self):
        self.SITE_LINK = 'https://www.google.com.br/'
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=Perfil')
        self.drive = webdriver.Chrome(options=options)
        self.drive.maximize_window()

    def abrir_site(self):
        sleep(2)
        self.drive.get(self.SITE_LINK)
        sleep(10)


if __name__ == '__main__':
    teste = CookieClicker()
    teste.abrir_site()
