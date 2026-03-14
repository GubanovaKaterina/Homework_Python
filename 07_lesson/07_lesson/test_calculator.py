from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


def test_positive():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    try:
        calculator_page = CalculatorPage(driver)
        calculator_page.open()
        calculator_page.set_delay(45)
        calculator_page.click_7()
        calculator_page.click_plus()
        calculator_page.click_8()
        calculator_page.click_equals()
        calculator_page.wait_for_result("15")
        
        result = calculator_page.get_result()
        assert result == "15"
        
    finally:
        driver.quit()