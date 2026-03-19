from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:

    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage.
        Содержит локаторы всех элементов
        и методы для взаимодействия с ними.
        WebDriverWait- установка таймаута
        для ожидания появления указанного текста
        на экране калькулятора.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.XPATH, '//span[text()="7"]')
        self.button_plus = (By.XPATH, '//span[text()="+"]')
        self.button_8 = (By.XPATH, '//span[text()="8"]')
        self.button_equals = (By.XPATH, '//span[text()="="]')
        self.screen = (By.CSS_SELECTOR, "div.screen")

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки {seconds} секунд")
    def set_delay(self, seconds):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param seconds: int — время задержки в секундах.
        """
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(int(seconds))

    @allure.step("Нажатие кнопки '7'")
    def click_7(self):
        """
        Нажимает на кнопку калькулятора "7".
        """
        self.driver.find_element(*self.button_7).click()

    @allure.step("Нажатие кнопки '+'")
    def click_plus(self):
        """
        Нажимает на кнопку калькулятора "+".
        """
        self.driver.find_element(*self.button_plus).click()

    @allure.step("Нажатие кнопки '8'")
    def click_8(self):
        """
        Нажимает на кнопку калькулятора "8".
        """
        self.driver.find_element(*self.button_8).click()

    @allure.step("Нажатие кнопки '='")
    def click_equals(self):
        """
        Нажимает на кнопку калькулятора "=".
        """
        self.driver.find_element(*self.button_equals).click()

    @allure.step("Ожидание результата '{expected_result}'")
    def wait_for_result(self, expected_result):
        """
        Метод ожидает появления заданного текста.
        :param expected_result: str — ожидаемый результат.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.screen, expected_result)
        )

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.
        :return: str — текст результата на экране калькулятора.
        """
        return self.driver.find_element(*self.screen).text
