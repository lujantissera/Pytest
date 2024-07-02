import pytest
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# @pytest.fixture(scope="module")
# def driver():
#     chrome_options = Options()
#     # Desactivar pop-ups y notificaciones
#     chrome_options.add_argument("--disable-popup-blocking")
#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_argument("--disable-infobars")
#     chrome_options.add_experimental_option("useAutomationExtension", False)
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

#     service = ChromeService(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     yield driver
#     driver.quit()
    
@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    yield driver
    driver.quit()

#Funcion para leer los terminos del CSV
def read_terms():
    with open('../testData/terminos.csv', newline= '') as csvfile:
        data = list (csv.reader(csvfile))
#devolver los terminos de busqueda excluyendo el titulo de la columna
        return [row[0] for row in data [1:]]
    
#fixture para parametrizar los terminos de busqueda leisod desde el csv
@pytest.fixture(params=[read_terms()])
def termino_de_busqueda (request):
    return request.param
        

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    yield driver
    driver.quit()
# Test que utiliza los datos que vienen del CSV
def test_google_busqueda(browser, termino_de_busqueda):
    browser()
    # search_box = browser.find_element("name", "q")
    # search_box.send_keys(termino_de_busqueda + Keys.RETURN)

    # results = browser.find_element("id", "search")
    # assert (
    #     len(results.find_elements("xpath", ".//div")) > 0
    # ), "Hay resultados de búsqueda"