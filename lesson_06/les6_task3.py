from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 10)

for image_id in ['compass', 'calendar', 'award', 'landscape']:
    wait.until(
        EC.visibility_of_element_located((By.ID, image_id))
    )

award_element = driver.find_element(By.ID, 'award')
award_src = award_element.get_attribute("src")
print(award_src)

driver.quit()