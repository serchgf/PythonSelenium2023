import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demoqa.com/select-menu"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(URL)


    def test_old_style_select(self):

        element = self.driver.find_element(By.ID, "cars")
        select = Select(element)
        brand1 = "Volvo"
        brand2 = "Audi"

        select.select_by_visible_text(brand1)
        assert select.first_selected_option.text == brand1
        select.deselect_by_visible_text(brand1)

        #select.select_by_value(brand2)
        select.select_by_visible_text(brand2)
        assert select.first_selected_option.text == brand2


    def test_old_style_select_multiple_select(self):
        element = self.driver.find_element(By.ID, "cars")
        select = Select(element)
        brands = ["Volvo", "Audi"]
        for brand in brands:
            select.select_by_visible_text(brand)
        assert len(select.all_selected_options) == len(brands)

    def teardown_method(self):
        self.driver.quit()