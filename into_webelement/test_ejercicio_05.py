import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#//div[@class='product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12']//img
CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_validate_item_price_caption(self):

        item_precio_list =[("MacBook","$602.00"),
                            ("iPhone","$123.20"),
                            ('Apple Cinema 30"', "$110.00"),
                            ("Canon EOS 5D", "$98.00")]

        lista_productos_features_caption = self.driver.find_elements(By.XPATH, "//div[@class='caption']")
        for index, element in enumerate(lista_productos_features_caption):
            assert item_precio_list[index][0] in element.text and item_precio_list[index][1] in element.text ,"The expected item-price does not correspond to the actual item-price"
            #assert item_precio_list[index][0] in element.text, "The expected item-is not present in element"
            #assert item_precio_list[index][1] in element.text, "The expected price is not present in element"

    def test_validate_item_price_2(self):
        item_precio_list =[("MacBook","$602.00"),
                            ("iPhone","$123.20"),
                            ('Apple Cinema 30"', "$110.00"),
                            ("Canon EOS 5D", "$98.00")]
        lista_productos_features_names = self.driver.find_elements(By.XPATH, "//div[@class='caption']/h4")
        lista_productos_features_price = self.driver.find_elements(By.XPATH, "//div[@class='caption']/p[@class='price']")

        price_list = self.clean_price_text(lista_productos_features_price)
        actual_item_name_list = []
        for index, name in enumerate(lista_productos_features_names):
            actual_item_name_list.append((name.text, price_list[index]))

        assert item_precio_list == actual_item_name_list, "The expected item-price does not correspond to the actual item-price"

    def clean_price_text(self, webelement_list: list) -> list:
        price_list=[]
        for price in webelement_list:
            lprice=price.text.split('\n')
            lprice = lprice[0].split()
            price_list.append(lprice[0])

        return price_list

    def teardown_method(self):
        self.driver.quit()


