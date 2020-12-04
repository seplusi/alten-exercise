import requests
import json
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

chromedriver_path = '/home/luis/Programs/chromedriver/chromedriver'
url = 'https://www.alten.es'

response = requests.get('https://api.covid19api.com/total/country/germany')
assert response.status_code == 200

for entry in json.loads(response.text):
    print('Fecha: %s   -    Num. Casos Activos: %d' %(entry['Date'], entry['Active']))


##############################################################################################
# Selenium exercise #
##############################################################################################


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")
options.add_experimental_option('w3c', False)
options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})

# Instanciate webdriver
instance1 = webdriver.Chrome(executable_path=chromedriver_path, options=options)
instance1.get("https://www.alten.es")

# Accept cookie if it exists
try:
    WebDriverWait(instance1, 10).until(EC.element_to_be_clickable((By.ID, "tarteaucitronPersonalize2"))).click()
except TimeoutException:
    pass

# Assert text SPAIN
assert WebDriverWait(instance1, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.in-the-world'))).text == "SPAIN"

# Click sectores and list all sectores text
WebDriverWait(instance1, 10).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'SECTORES'))).click()
sectors_elements = WebDriverWait(instance1, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.expertise-item > a')))
for element in sectors_elements:
    print(element.text)

instance1.close()
