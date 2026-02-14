from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

search_box = driver.find_element(By.CSS_SELECTOR, "#username")
search_box.send_keys("tomsmith")
search_box2 = driver.find_element(By.CSS_SELECTOR, "#password")
search_box2.send_keys("SuperSecretPassword!")
search_box3 = driver.find_element(By.CSS_SELECTOR, "i.fa").click()
search_box4 = driver.find_element(By.CSS_SELECTOR, "div#flash.flash.success")
print(search_box4.text)

sleep(2)
driver.quit()