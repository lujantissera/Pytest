import pytest
from pages.sandbox_page import SandboxPage

def test_click_enviar(sandbox_page):
    sandbox_page.click_enviar()