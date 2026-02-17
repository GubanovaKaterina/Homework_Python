from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

search_box = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
search_box.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

button_text = button.text
print(button_text)

driver.quit()