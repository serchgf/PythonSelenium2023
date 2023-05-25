from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_ejericio_01(self):
        expected_title = "Your Store"
        print(f"Verify webdriver open the following URL: {URL} with the title: {expected_title}")
        expected_title = "Your Store"
        assert expected_title in self.driver.title, "Title not expected"


    def teardown_method(self):
        self.driver.quit()