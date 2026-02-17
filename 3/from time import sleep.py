python

from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def create_edge_driver():
    """Создание драйвера Edge с правильными настройками"""
    try:
        # Опции для Edge
        edge_options = Options()
        edge_options.add_argument("--start-maximized")
        # edge_options.add_argument("--headless")  # Раскомментируй для фонового режима
        
        # Автоматическая установка драйвера
        driver_path = EdgeChromiumDriverManager().install()
        service = Service(driver_path)
        
        # Создание драйвера
        driver = webdriver.Edge(service=service, options=edge_options)
        return driver
    except Exception as e:
        print(f"Ошибка при создании драйвера Edge: {e}")
        return None

def make_screenshot(browser: WebDriver, url: str = "https://ya.ru/"):
    """Делает скриншот страницы"""
    try:
        print(f"Открываю {url} в {browser.name}...")
        browser.get(url)
        sleep(3)
        
        filename = f"./ya_{browser.name}.png"
        browser.save_screenshot(filename)
        print(f"Скриншот сохранен: {filename}")
        
        return True
    except Exception as e:
        print(f"Ошибка при создании скриншота в {browser.name}: {e}")
        return False
    finally:
        browser.quit()

# Создаем и используем драйвер Edge
edge_driver = create_edge_driver()
if edge_driver:
    make_screenshot(edge_driver)