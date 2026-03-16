from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.XPATH, '//span[text()="7"]')
        self.button_plus = (By.XPATH, '//span[text()="+"]')
        self.button_8 = (By.XPATH, '//span[text()="8"]')
        self.button_equals = (By.XPATH, '//span[text()="="]')
        self.screen = (By.CSS_SELECTOR, "div.screen")
    
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, seconds):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(seconds))
    
    def click_7(self):
        self.driver.find_element(*self.button_7).click()
    
    def click_plus(self):
        self.driver.find_element(*self.button_plus).click()
    
    def click_8(self):
        self.driver.find_element(*self.button_8).click()
    
    def click_equals(self):
        self.driver.find_element(*self.button_equals).click()
    
    def wait_for_result(self, expected_result):
        self.wait.until(
            EC.text_to_be_present_in_element(self.screen, expected_result)
        )
    
    def get_result(self):
        return self.driver.find_element(*self.screen).text