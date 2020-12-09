from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class EventosPage(BasePage):

    FILTER_CATEGORY = 'a.selected'
    FOOTER_MENU = 'menu-footer-es'
    ALL_HREFS = '[href^=http]'

    def __init__(self, driver):
        super().__init__(driver)
        self._wait_for_categories()

    def _wait_for_categories(self):
        self.wait_for_element((By.CSS_SELECTOR, self.FILTER_CATEGORY))

    def get_footer_menu(self):
        elements = self.driver.find_element_by_id(self.FOOTER_MENU).find_elements_by_css_selector(self.ALL_HREFS)

        return [element.text for element in elements]
