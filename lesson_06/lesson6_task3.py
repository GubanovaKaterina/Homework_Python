from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Done")
)

ff = driver.find_element(By.CSS_SELECTOR, '#award')
ff2 = ff.get_attribute("src")
print(ff2)

driver.quit()