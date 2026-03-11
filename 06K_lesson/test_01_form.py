import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission():
    driver = webdriver.Edge()
    
    try:
        driver.implicitly_wait(0)
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="first-name"]')))
        
        first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
        first_name.send_keys("Иван")

        last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
        last_name.send_keys("Петров")

        address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
        address.send_keys("Ленина, 55-3")

        zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
        zip_code.send_keys("")  

        city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
        city.send_keys("Москва")

        country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
        country.send_keys("Россия")

        e_mail = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
        e_mail.send_keys("test@skypro.com")

        phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
        phone.send_keys("+7985899998787")

        job_position = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
        job_position.send_keys("QA")

        company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
        company.send_keys("SkyPro")
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3")
        submit_button.click()

        zip_code_div = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code"))
        )
        
        zip_code_class = zip_code_div.get_attribute("class")
        print(f"Zip code div class: {zip_code_class}")
        assert "alert-danger" in zip_code_class, f"Zip-code должен быть красным, получен класс: {zip_code_class}"
        

        success_fields = ["first-name", "last-name", "address", "city", "country", 
                         "e-mail", "phone", "job-position", "company"]
        
        for field_name in success_fields:
            element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f"#{field_name}"))
            )
            
            element_class = element.get_attribute("class")
            print(f"{field_name} class: {element_class}")
            assert "alert-success" in element_class, f"Поле {field_name} должно быть зеленым, получен класс: {element_class}"
        
     
    finally:
        driver.quit()