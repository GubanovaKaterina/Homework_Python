from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com")

driver.get("https://vk.com")

#for x in range(1, 10):
    #driver.back()
    #driver.forward()

sleep(15)