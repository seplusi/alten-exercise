from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class homePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._accept_cookie()

    def _accept_cookie(self):
        try:
            self.wait_element_clicable((By.ID, 'tarteaucitronPersonalize2')).click()
        except TimeoutException:
            pass

    def get_sectores(self):
        self.wait_element_clicable((By.PARTIAL_LINK_TEXT, 'SECTORES')).click()
        sectors_elements = self.wait_for_elements((By.CSS_SELECTOR, 'div.expertise-item > a'))

        return [element.text for element in sectors_elements]

    def get_country_name(self):
        return self.wait_for_element((By.CSS_SELECTOR, 'div.in-the-world')).text
