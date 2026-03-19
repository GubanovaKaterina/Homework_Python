from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage
import allure


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работу калькулятора"
                    "с различными операциями.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_positive():
    """
    Тест проверяет работу калькулятора с различными операциями.

    :param driver: WebDriver — объект драйвера Selenium.
    :param delay: int — задержка в секундах для выполнения операции.
    :param expected_result: str — ожидаемый результат операции.
    """
    chrome_driver_path = ChromeDriverManager().install()
    chrome_service = ChromeService(chrome_driver_path)

    driver = webdriver.Chrome(service=chrome_service)
    try:
        calculator_page = CalculatorPage(driver)
        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()

        with allure.step("Установка задержки {seconds} секунд"):
            calculator_page.set_delay(45)

        with allure.step("Нажатие кнопки '7'"):
            calculator_page.click_7()

        with allure.step("Нажатие кнопки '+'"):
            calculator_page.click_plus()

        with allure.step("Нажатие кнопки '8'"):
            calculator_page.click_8()

        with allure.step("Нажатие кнопки '='"):
            calculator_page.click_equals()

        with allure.step("Ожидание результата '{expected_result}'"):
            calculator_page.wait_for_result("15")

        with allure.step("Получение результата с экрана калькулятора"):
            result = calculator_page.get_result()
        assert result == "15"

    finally:
        driver.quit()
