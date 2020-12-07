from page_objects.home_page import homePage
import pytest

URL = 'https://www.alten.es'


@pytest.fixture(scope="function", name="alten_page")
def home_page(webdriver):
    webdriver.get(URL)
    yield homePage(webdriver)


def test_home_page(alten_page):
    assert alten_page.get_country_name() == "SPAIN"

def test_get_sectores(alten_page):
    assert alten_page.get_sectores() == ['AERO - ESPACIO - DEFENSA', 'TRANSPORTE', 'ENERGÍA - INDUSTRIA', 'Centros de excelencia TICC', 'LIFE SCIENCES', 'SERVICIOS FINANCIEROS – BANCA – SEGUROS – MEDIA', 'ALTEN ACADEMY', 'ADMINISTRACIONES PÚBLICAS', 'NUESTRAS ALIANZAS']
