from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Ждем, пока элемент появится
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# Не закрывай сразу, дай посмотреть
input("Нажми Enter для закрытия...")
driver.quit()