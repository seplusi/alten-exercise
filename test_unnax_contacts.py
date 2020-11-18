import unittest
from src.page_objects.contacts import ContactsPage
from selenium import webdriver
from src.common.chromedriver_obj import Driver


chromedriver_path = '/home/luis/Programs/chromedriver/chromedriver'

driver = None

#driver = Driver(chromedriver_path)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")
options.add_experimental_option('w3c', False)
options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})

instance = webdriver.Chrome(executable_path=chromedriver_path, options=options)


instance.get("https://www.alten.es")
driver.instance.quit()
