from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SauceDemoPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.username_input = (By.CSS_SELECTOR, '#user-name')
        self.password_input = (By.CSS_SELECTOR, '#password')
        self.login_button = (By.CSS_SELECTOR, '#login-button')
        
        self.backpack_add_button = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
        self.bolt_tshirt_add_button = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
        self.onesie_add_button = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
        self.cart_link = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        
        self.checkout_button = (By.CSS_SELECTOR, '#checkout')
        
        self.first_name_input = (By.CSS_SELECTOR, '#first-name')
        self.last_name_input = (By.CSS_SELECTOR, '#last-name')
        self.postal_code_input = (By.CSS_SELECTOR, '#postal-code')
        self.continue_button = (By.CSS_SELECTOR, '#continue')
        
        self.total_label = (By.CSS_SELECTOR, '[class="summary_total_label"]')
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
    
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    
    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack_add_button).click()
    
    def add_bolt_tshirt_to_cart(self):
        self.driver.find_element(*self.bolt_tshirt_add_button).click()
    
    def add_onesie_to_cart(self):
        self.driver.find_element(*self.onesie_add_button).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
    
    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
    
    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
    
    def get_total_price(self):
        return self.driver.find_element(*self.total_label).text
    
    def extract_price_value(self, price_text):
        price = ''.join(c for c in price_text if c.isdigit() or c == '.')
        return float(price)
    