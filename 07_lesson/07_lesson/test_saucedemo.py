from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from saucedemo_page import SauceDemoPage


def test_positive():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    try:
        saucedemo_page = SauceDemoPage(driver)        
        saucedemo_page.open()
        saucedemo_page.login("standard_user", "secret_sauce")
        saucedemo_page.add_backpack_to_cart()
        saucedemo_page.add_bolt_tshirt_to_cart()
        saucedemo_page.add_onesie_to_cart()
        saucedemo_page.go_to_cart()
        saucedemo_page.proceed_to_checkout()
        saucedemo_page.fill_checkout_info("Katya", "Gubanova", "630027")
        
        total_text = saucedemo_page.get_total_price()
        print(f'{total_text}')
        
        total_price = saucedemo_page.extract_price_value(total_text)
        expected_price = 58.29
        assert total_price == expected_price
        
    finally:
        driver.quit()