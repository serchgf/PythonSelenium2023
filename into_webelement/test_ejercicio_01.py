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

    def test_buscar_iphone(self):

        search_bar = self.driver.find_element(By.XPATH, "//input[@name='search']")
        search_bar.send_keys("iphone")
        search_button = self.driver.find_element(By.XPATH, "//div[@id='search']//button")
        search_button.click()
        time.sleep(3)
        search_result = self.driver.find_element(By.XPATH, "//img[@alt='iPhone']")

        assert search_result.is_displayed()

    def teardown_method(self):
        self.driver.quit()





