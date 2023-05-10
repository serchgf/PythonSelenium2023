import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_seleccionar_tablets(self):

        tablets_liktext = self.driver.find_element(By.LINK_TEXT, "Laptops & Notebooks")
        tablets_liktext.click()
        windows_linktext = self.driver.find_element(By.XPATH, "//a[contains(text(),'Windows (0)')]")
        windows_linktext.click()
        time.sleep(2)
        mensaje = self.driver.find_element(By.XPATH, "//p[contains(text(),'There are no products to list in this category.')]")
        assert mensaje.is_displayed()
        btn_continue = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]")
        if btn_continue.is_displayed() and btn_continue.is_enabled():
            btn_continue.click()
            assert self.driver.title == "Your Store"

    def teardown_method(self):
        self.driver.quit()



