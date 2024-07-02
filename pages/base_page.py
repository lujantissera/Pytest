from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui  import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        
    def navigate_to(self, url):
        self.driver.get(url)
        
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        
    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()
        
    def type_text (self,locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)      
        
    def select_dropdown(self,locator, option):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_visible_text(option)
        
    def select_dropdown_by_index(self, locator, index):
        dropdown=Select(self.wait_for_element(locator))
        dropdown.select_by_index(index)
        
    def selec_checkBox(self,locator,checkbox):
        checkbox= self.wait_for_element(locator)
        if not checkbox.is_selected():
            checkbox.click()
            
            
            
    def unselec_checkBox(self,locator,checkbox):
        checkbox= self.wait_for_element(locator)
        if checkbox.is_selected():
            checkbox.click()
    
        
        
        
    ##Vamos a ir agregando metodos como click, select , y demas 