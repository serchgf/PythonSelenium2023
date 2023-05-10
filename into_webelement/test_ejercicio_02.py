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

        tablets_liktext = self.driver.find_element(By.LINK_TEXT, "Tablets")
        tablets_liktext.click()
        item = self.driver.find_element(By.XPATH, "//a[contains(text(),'Samsung Galaxy Tab 10.1')]")
        item.click()
        time.sleep(2)
        costo_item = self.driver.find_element(By.XPATH, "//h2[contains(text(),'$241.99')]")
        #costo_item = self.driver.find_element(By.XPATH,"//div[@class='col-sm-4']//h2")
        assert costo_item.text == '$241.99'
        # agregar a wish list
        boton_wish_list = self.driver.find_element(By.XPATH, "//button[@data-original-title='Add to Wish List']")
        boton_wish_list.click()
        time.sleep(2)
        alerta = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']//a[contains(text(),'wish list')]")
        assert "wish list" in alerta.text
        time.sleep(1)
        # agregar al carrito de compra
        boton_carrito = self.driver.find_element(By.ID, "button-cart")
        boton_carrito.click()
        time.sleep(1)
        alerta = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']//a[contains(text(),'shopping cart')]")
        assert "shopping cart" in alerta.text



    def teardown_method(self):
        self.driver.quit()



