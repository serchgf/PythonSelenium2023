from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(5)
        self.wait_driver = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_click_validate_verificar_mensaje(self):
        # Obtener el elemento, y el estado importa
        button_autocloseable = self.__find_clickable_element(By.XPATH, "//button[contains(text(),'Autocloseable success message')]")
        button_autocloseable.click()
        visible = self.__find_visible_element(By.XPATH,"//div[@class='alert alert-success alert-autocloseable-success']")
        invisible = self.__wait_until_disappears(By.XPATH, "//div[@class='alert alert-success alert-autocloseable-success']")
        # assert invisible



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

Respuesta ejercicio 10:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(1)
        self.wait_driver = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_slow_loading_page(self):
        # Obtener el elemento, y el estado importa
        dialogo = self.__find_clickable_element(By.ID, "autoclosable-btn-success")
        dialogo.click()
        self.__find_visible_element(By.XPATH, "//*[@class='alert alert-success alert-autocloseable-success']")
        self.__wait_until_disappears(By.XPATH, "//*[@class='alert alert-success alert-autocloseable-success']")

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_by_text(self, by: By, value: str, text: str) -> WebElement:
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def __wait_until_disappears(self, by: By, value: str) -> WebElement:
        self.wait_driver.until(EC.invisibility_of_element((by, value)))

    def teardown_method(self):
        self.driver.quit()

"""