from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*locator))

    def wait_element_clicable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_elements(*locator))

    def scroll_to_element(self, locator, xoffset=0, yoffset=0):
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(self.wait_element_clicable(locator), xoffset=xoffset, yoffset=yoffset)
        actions.perform()
