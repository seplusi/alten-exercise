from page_objects.home_page import homePage
from page_objects.eventos_page import EventosPage
import pytest

URL = 'https://www.alten.es'


@pytest.fixture(scope="function", name="alten_page")
def home_page(webdriver):
    webdriver.get(URL)
    yield homePage(webdriver)


#@pytest.mark.skip("")
def test_home_page(alten_page):
    assert alten_page.get_country_name() == "SPAIN"


#@pytest.mark.skip("")
def test_get_sectores(alten_page):
    assert alten_page.get_sectores() == ['AERO - ESPACIO - DEFENSA', 'TRANSPORTE', 'ENERGÍA - INDUSTRIA', 'Centros de excelencia TICC', 'LIFE SCIENCES', 'SERVICIOS FINANCIEROS – BANCA – SEGUROS – MEDIA', 'ALTEN ACADEMY', 'ADMINISTRACIONES PÚBLICAS', 'NUESTRAS ALIANZAS']


#@pytest.mark.skip("")
def test_events_link(alten_page, webdriver):
    alten_page.click_events_link()
    eventos = EventosPage(webdriver)
    assert eventos.get_footer_menu() == ['Nuestra oferta', 'Empleo', 'ALTEN’s Life', 'Eventos', 'Contacta', 'Políticas de Calidad y Medio Ambiente']


#@pytest.mark.skip("")
def test_languages(alten_page):
    assert alten_page.get_header_elements() == ['CONÓCENOS', 'SECTORES', 'EMPLEO', 'ALTEN’S LIFE', 'WOMEN@ALTEN', 'EVENTOS', 'MÁS']
    assert alten_page.select_language() == ('ES', 'EN')
    alten_page.get_header_elements('en') == ['ABOUT', 'KEY FIGURES', 'EXPERTISE', 'JOIN US', 'EVENTS', 'CONTACT US']
