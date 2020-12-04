import requests
import json
import pytest


@pytest.mark.parametrize('country', ['germany', 'portugal', 'marshall-islands'])
def test_existing_countries(country):
    response = requests.get('https://api.covid19api.com/total/country/%s' % country)
    assert response.status_code == 200

    for entry in json.loads(response.text):
        assert list(entry.keys()) == ['Country', 'CountryCode', 'Province', 'City', 'CityCode', 'Lat', 'Lon', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Date']
        for key in ['Country', 'CountryCode', 'Province', 'City', 'CityCode', 'Lat', 'Lon', 'Date']:
            assert isinstance(entry[key], str)
        for key in ['Confirmed', 'Deaths', 'Recovered', 'Active']:
            assert isinstance(entry[key], int)
        print('Fecha: %s   -    Num. Casos Activos: %d   Num. Muertes: %d' % (entry['Date'], entry['Active'], entry['Deaths']))


def test_non_existant_countries(get_all_countries):
    for country in get_all_countries:
        response = requests.get('https://api.covid19api.com/total/country/%s' % country)
        assert response.status_code == 404
        assert json.loads(response.text)['message'] == 'Not Found'


def test_mixed_responses(get_all_countries_from_file):
    for country, status_code in get_all_countries_from_file:
        response = requests.get('https://api.covid19api.com/total/country/%s' % country)
        print(f"{country}: {response.status_code}")
        assert response.status_code == int(status_code), 'https://api.covid19api.com/total/country/%s reported status_code = %s' % (country, status_code)
