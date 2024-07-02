import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service
from pages.sandbox_page import SandboxPage

@pytest.fixture(scope="session")
def browser():
    service = service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.freerangetesters.com/")
    yield driver
    driver.quit()
    
@pytest.fixture
def sandbox_page(browser):
    return SandboxPage(browser)
