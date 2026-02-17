from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка опций Chrome
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

try:
    driver.get("https://www.labirint.ru")
    
    # Ждем поле поиска
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#search-field"))
    )
    
    search_input.send_keys("Python")
    search_input.send_keys(Keys.RETURN)
    
    # Ждем загрузки результатов
    books = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-card, .products-row__item"))
    )
    
    print(f"Найдено книг: {len(books)}")
    
    # Разные варианты селекторов для автора на labirint.ru
    author_selectors = [
        ".product-card__author",  # основной селектор
        ".product-author",        # альтернативный
        ".product-author a",      # если автор - ссылка
        ".author",                # другой вариант
        ".product-info__author",  # еще вариант
        ".product__author"        # и еще
    ]
    
    for i, book in enumerate(books):
        author_text = "Автор не указан"
        
        # Пробуем найти автора разными селекторами
        for selector in author_selectors:
            try:
                author_element = book.find_element(By.CSS_SELECTOR, selector)
                author_text = author_element.text.strip()
                if author_text:  # Если текст не пустой
                    break
            except:
                continue
        
        # Также можно попробовать получить название книги
        try:
            title = book.find_element(By.CSS_SELECTOR, ".product-card__title, .product-title").text
            print(f"Книга {i+1}: {title[:50]}... | Автор: {author_text}")
        except:
            print(f"Книга {i+1}: автор {author_text}")
            
finally:
    driver.quit()