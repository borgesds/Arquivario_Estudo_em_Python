"""
pip install selenium
https://pypi.org/project/selenium/
https://chromedriver.chromium.org/downloads
"""

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeAuto:
    def __init__(self):
        # self.SITE_LINK = 'https://www.google.com.br/'
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(options=options)
        self.chrome.maximize_window()

    def clica_sing_in(self):
        try:
            btn_sign_in = self.chrome.find_element(
                'css selector', 'a[data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in"]'
            )
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar no Sing in:', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def fazer_login(self):
        try:
            # Definindo o tempo máximo de espera em segundos
            wait = WebDriverWait(self.chrome, 10)

            input_login = wait.until(EC.presence_of_element_located((
                                     By.ID, 'login_field'
                                     )))
            input_password = wait.until(EC.presence_of_element_located((
                                        By.ID, 'password'
                                        )))
            btn_login = wait.until(EC.presence_of_element_located((
                                   By.NAME, 'commit'
                                   )))

            input_login.send_keys('borges.an@hotmail.com')
            input_password.send_keys('xxxxxxxxxxx')
            sleep(3)
            btn_login.click()
        except Exception as e:
            print('LoginError:', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    chrome.clica_sing_in()
    chrome.fazer_login()

    sleep(30)
    chrome.sair()
