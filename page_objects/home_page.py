from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class homePage(BasePage):
    ACCEPT_COOKIE_ID = 'tarteaucitronPersonalize2'
    SECTORES_BUTTON = 'SECTORES'
    SECTORES_ELEMENTS = 'div.expertise-item > a'
    COUNTRY_SELECTOR = 'div.in-the-world'
    BOTTOM_LINK_TEXT = 'Políticas de Calidad y Medio Ambiente'
    EVENTOS_LINK_TEXT = 'Eventos'
    MENU_HEADER_SELECTORS = 'ul.menu > li > a'
    LANGUAGE_BUTTON = 'div.language-selector'
    LANGUAGE_BUTTON_SUBCLASS = 'current'
    NEW_LANGUAGE_BUTTON = 'div.language-selector.hover > div > a'


    def __init__(self, driver):
        super().__init__(driver)
        self._accept_cookie()

    def _accept_cookie(self):
        try:
            self.wait_element_clicable((By.ID, self.ACCEPT_COOKIE_ID)).click()
        except TimeoutException:
            pass

    def get_sectores(self):
        self.wait_element_clicable((By.PARTIAL_LINK_TEXT, self.SECTORES_BUTTON)).click()
        sectors_elements = self.wait_for_elements((By.CSS_SELECTOR, self.SECTORES_ELEMENTS))

        return [element.text for element in sectors_elements]

    def get_country_name(self):
        return self.wait_for_element((By.CSS_SELECTOR, self.COUNTRY_SELECTOR)).text

    def click_events_link(self):
        self.scroll_to_element((By.PARTIAL_LINK_TEXT, self.BOTTOM_LINK_TEXT))
        self.wait_element_clicable((By.PARTIAL_LINK_TEXT, self.EVENTOS_LINK_TEXT)).click()

    def get_header_elements(self, language='es'):
        header_elements_text = []
        elements = self.wait_for_element((By.ID, f'menu-header-{language}')).find_elements_by_css_selector(self.MENU_HEADER_SELECTORS)
        for element in elements:
            if element.text != '':
                header_elements_text.append(element.text)

        return header_elements_text

    def select_language(self):
        element = self.wait_for_element((By.CSS_SELECTOR, self.LANGUAGE_BUTTON))
        current_language = element.find_element_by_class_name(self.LANGUAGE_BUTTON_SUBCLASS).text

        self.scroll_to_element((By.CSS_SELECTOR, self.LANGUAGE_BUTTON), xoffset=0, yoffset=0)
        self.wait_element_clicable((By.CSS_SELECTOR, self.NEW_LANGUAGE_BUTTON)).click()
        selected_language = self.wait_element_clicable((By.CSS_SELECTOR, self.LANGUAGE_BUTTON)).text

        return current_language, selected_language
