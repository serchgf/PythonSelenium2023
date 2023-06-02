from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(5)
        self.wait_driver = WebDriverWait(self.driver, 60)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_click_validate_text_visibility(self):
        # Obtener el elemento, y el estado importa
        button_download = self.__find_clickable_element(By.XPATH, "//button[@id='downloadButton']")
        button_download.click()
        button_close = self.__find_clickable_element(By.XPATH,"//button[contains(text(),'Close')]")
        assert button_close, "No llego es clickeable"
        label_complete= self.__find_by_text(By.XPATH, "//div[@class='progress-label']", 'Complete!')
        assert label_complete, "label incorrecta"



    def __find_clickable_element(self, by: By, value: str):
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str):
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_by_text(self, by: By, value: str, text: str):
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def __wait_until_disappears(self, by: By, value: str):
        self.wait_driver.until(EC.invisibility_of_element((by, value)))

    def teardown_method(self):
        self.driver.quit()


"""
Respuesta ejercicio 09:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html "


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(5)
        self.wait_driver = WebDriverWait(self.driver, 120)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_download(self):
        # Obtener el elemento, y el estado importa
        download = self.__find_clickable_element(By.ID, "cricle-btn")
        download.click()
        self.__find_by_text(By.CLASS_NAME, "percenttext", "100%")

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_by_text(self, by: By, value: str, text: str) -> WebElement:
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def __wait_until_disappears(self, by: By, value: str):
        self.wait_driver.until(EC.invisibility_of_element((by, value)))

    def teardown_method(self):
        self.driver.quit()


"""