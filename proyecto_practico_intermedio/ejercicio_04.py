import time

from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)
        self.wait_driver = WebDriverWait(self.driver, 10)

    def test_item_price(self):
        # identify default currency
        currency = self.driver.find_element(By.XPATH, "//strong")
        assert "$" in currency.text, "Symbol '$' should be showed"

        # Search samsung
        search_bar =  self.driver.find_element(By.XPATH, "//input[@name='search']")
        search_bar.send_keys("Samsung")

        search_button = self.driver.find_element(By.XPATH, "//div[@id='search']//button")
        search_button.click()

        # select item 'Samsung SyncMaster 941Bw'
        item_selected = self.driver.find_element(By.XPATH, "//a[contains(text(),'Samsung SyncMaster 941BW')]")
        item_selected.click()

        # get item dolar price
        item_price = self.driver.find_element(By.XPATH, "//div[@class='col-sm-4']//h2")
        # save the dolar value
        dollar_item_price = item_price.text.replace("$","")

        # click on currency button dropdown
        currency_button = self.driver.find_element(By.XPATH, "//div[@class='pull-left']//div/button")
        currency_button.click()

        # Select EURO option
        euro_option = self.driver.find_element(By.XPATH, "//button[@name='EUR']")
        euro_option.click()

        # get item euro price
        item_price = self.driver.find_element(By.XPATH, "//div[@class='col-sm-4']//h2")
        euro_item_price = item_price.text.replace("$", "")

        assert "€" in euro_item_price, "Symbol '€' should be showed"
        assert euro_item_price < dollar_item_price, f"The Euro value: {euro_item_price} should be minor than Dollar Value: {dollar_item_price}"



    def teardown_method(self):
        self.driver.quit()