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

    def test_add_item(self):
        # click on  Desktop link
        desktops_button = self.driver.find_element(By.XPATH, "//li/a[contains(text(),'Desktops')]")
        assert desktops_button.is_displayed() and desktops_button.is_enabled(), "The button is not available"
        desktops_button.click()

        # Select Mac (1) option
        mac_1_option = self.driver.find_element(By.XPATH, "//li/a[contains(text(),'Mac (1)')]")
        mac_1_option.click()

        # verify Result Text
        search_result = self.driver.find_element(By.XPATH, "//h4/a[contains(text(),'Mac')]")
        print(search_result.text)
        expected_text = 'iMac'
        assert search_result.text == expected_text

        #click on search result
        search_result.click()

        # add to car
        add_car_button = self.driver.find_element(By.ID, "button-cart")
        add_car_button.click()
        time.sleep(1)
        # verify information of product added
        expected_info = "1 item(s) - $122.00"
        #//div[@id='cart']
        span_car = self.driver.find_element(By.XPATH, "//span[@id ='cart-total']")

        #span_car = self.__find_by_text(By.XPATH,"//div[@id='cart']", expected_text)

        total_text = span_car.text
        print(total_text)
        assert expected_info == total_text
        # try:
        #     assert expected_info == total_text
        # except AssertionError:
        #     span_car = self.driver.find_element(By.XPATH, "//span[@id ='cart-total']")
        #     total_text = span_car.text
        #     assert expected_info == total_text


    def __find_by_text(self, by: By, value: str, text: str):
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def teardown_method(self):
        self.driver.quit()