from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.contador = 1
        self.URL = 'https://www.bmgconsig.com.br/principal/fsconsignataria.jsp'
        self.driver = webdriver.Chrome(
            executable_path='chromedriver',
            options=options
        )
        self.driver.get(self.URL)


if __name__ == '__main__':
    chrome = ChromeAuto()

