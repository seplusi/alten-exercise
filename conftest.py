import pytest
import csv

TEST_DATA_FOLDER = 'test_data'
FILE2TEST_COUNTRY_REPSONSES = 'countries.csv'

@pytest.fixture(scope="session")
def get_all_countries():
    yield ['blah', 'blah2']
    print('Tearing down get_all_countries')


@pytest.fixture(scope="session")
def get_all_countries_from_file():
    with open(f"{TEST_DATA_FOLDER}/{FILE2TEST_COUNTRY_REPSONSES}", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")

        yield data
