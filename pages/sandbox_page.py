from selenium.webdriver.common.by import By
from .base_page import BasePage

class SandboxPage(BasePage):
    ENVIAR_BUTTON =(By.XPATH, "//button[Contains(text, 'Enviar')]")
    
    def click_enviar(self):
        self.click(self.ENVIAR_BUTTON)
        
    def navigate_sandbox(self):
        self.navigate_to("https://thefreerangetester.github.io/sandbox-automation-testing/")