import pytest
import csv
from selenium import webdriver

TEST_DATA_FOLDER = 'test_data'
FILE2TEST_COUNTRY_REPSONSES = 'countries.csv'
chromedriver_path = '/home/luis/Programs/chromedriver/chromedriver'


@pytest.fixture(scope="session")
def get_all_countries():
    yield ['blah', 'blah2']
    print('Tearing down get_all_countries')


@pytest.fixture(scope="session")
def get_all_countries_from_file():
    with open(f"{TEST_DATA_FOLDER}/{FILE2TEST_COUNTRY_REPSONSES}", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")

        yield data


@pytest.fixture(scope="function", name="webdriver")
def webdriver_create():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option('w3c', False)
    options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})

    # Instanciate webdriver
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
    yield driver

    print("Destroying webdriver")
    driver.stop_client()
    driver.close()
