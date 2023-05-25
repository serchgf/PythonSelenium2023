from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_search_in_products_description(self):
        # Escribir Iphone
        search_input = self.driver.find_element(By.NAME, "search")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_input.send_keys("Display")

        # Dar click en buscar
        search_btn = self.driver.find_element(By.XPATH, "//div[@id='search']//button")
        search_btn.click()

        # Verificar que es visible el mensaje mensaje ""There is no product that matches the search criteria."
        expected_message = self.driver.find_element(By.XPATH, "//p[contains(text(),'There is no product that matches the search criteria.')]")
        #print(expected_message.text)
        assert expected_message.is_displayed(), "There is no product that matches the search criteria. message should be displayed"

        # click on checkbox
        checkbox_description = self.driver.find_element(By.XPATH, "//input[@id='description']")
        checkbox_description.click()

        # click on search button
        search_button = self.driver.find_element(By.XPATH, "//input[@id='button-search']")
        search_button.click()

        # get found elements title
        expected_results = ['Apple Cinema 30"','iPod Nano', 'iPod Touch', 'MacBook Pro']
        results = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']//img")
        title_getted_results = []
        for result in results:
            title_getted_results.append(result.get_attribute("title"))

        assert title_getted_results == expected_results

    def teardown_method(self):
        self.driver.quit()