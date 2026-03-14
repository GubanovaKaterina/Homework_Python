import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
def test_positive():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()
    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Katya")
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Gubanova")
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("630027")
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    result = driver.find_element(By.CSS_SELECTOR, '[class="summary_total_label"]').text

    price = ''.join(c for c in result if c.isdigit() or c == '.')
    print(f'{price}')

    price_float = float(price)
    assert price_float == 58.29


    assert price_float == 58.29

    driver.quit()