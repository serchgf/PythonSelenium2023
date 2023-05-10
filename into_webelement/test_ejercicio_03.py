
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/index.php?route=account/login"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_login_simple(self):
        email_tbx = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_tbx.send_keys("userfalso")
        password_tbx = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_tbx.send_keys("passfalso")

        boton_login = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        boton_login.click()
        time.sleep(2)

        alerta = self.driver.find_element(By.XPATH,
                                          "//div[@class='alert alert-danger alert-dismissible']")
        assert "Warning: No match for E-Mail Address and/or Password." == alerta.text

    #     users =[{"email":"email1", "password":"pass1"},
    #     {"email":"email_valido", "password":"pass_valido"},
    #     {"email":"email_invalido", "password":"pass_invalido"},
    #     {"email":"email_formato_invalido", "password":"pass_invalido"}]
    #
    #
    #
    # #def hacer_login(self, email: str, password: str):
    # def hacer_login(self, locator_mail, locator_password, locator_boton, email:str, password:str):
    #     locator_mail.clear()
    #     locator_mail.send_keys(email)
    #     locator_password.clear()
    #     locator_password.send_keys(password)
    #     locator_boton.click()


    def teardown_method(self):
        self.driver.quit()


