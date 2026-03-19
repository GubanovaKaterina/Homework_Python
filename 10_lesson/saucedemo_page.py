from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class SauceDemoPage:

    def __init__(self, driver):
        """
        Конструктор класса SauceDemoPage.
        Содержит локаторы всех элементов
        и методы для взаимодействия с ними.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username_input = (By.CSS_SELECTOR, '#user-name')
        self.password_input = (By.CSS_SELECTOR, '#password')
        self.login_button = (By.CSS_SELECTOR, '#login-button')

        self.backpack_add_button = (By.CSS_SELECTOR,
                                    '#add-to-cart-sauce-labs-backpack')
        self.bolt_tshirt_add_button = (By.CSS_SELECTOR,
                                       '#add-to-cart-sauce-labs-bolt-t-shirt')
        self.onesie_add_button = (By.CSS_SELECTOR,
                                  '#add-to-cart-sauce-labs-onesie')
        self.cart_link = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')

        self.checkout_button = (By.CSS_SELECTOR, '#checkout')

        self.first_name_input = (By.CSS_SELECTOR, '#first-name')
        self.last_name_input = (By.CSS_SELECTOR, '#last-name')
        self.postal_code_input = (By.CSS_SELECTOR, '#postal-code')
        self.continue_button = (By.CSS_SELECTOR, '#continue')

        self.total_label = (By.CSS_SELECTOR, '[class="summary_total_label"]')

    @allure.step("Открытие страницы магазина")
    def open(self):
        """
        Открывает страницу магазина.
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация '{username}', '{password}'")
    def login(self, username, password):
        """
        Вводит данные для авторизации, жмет кнопку Вход.
        :param username: str — логин.
        :param password: str — пароль.
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    @allure.step("Добавить рюкзак в корзину")
    def add_backpack_to_cart(self):
        """
        Добавляет рюкзак в корзину.
        """
        self.driver.find_element(*self.backpack_add_button).click()

    @allure.step("Добавить футболку в корзину")
    def add_bolt_tshirt_to_cart(self):
        """
        Добавляет футболку в корзину.
        """
        self.driver.find_element(*self.bolt_tshirt_add_button).click()

    @allure.step("Добавить боди в корзину")
    def add_onesie_to_cart(self):
        """
        Добавляет боди в корзину.
        """
        self.driver.find_element(*self.onesie_add_button).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """
        Переходит в корзину.
        """
        self.driver.find_element(*self.cart_link).click()

    @allure.step("Нажать кнопку Checkout")
    def proceed_to_checkout(self):
        """
        Жмет кнопку Checkout.
        """
        self.driver.find_element(*self.checkout_button).click()

    @allure.step(
                    "Заполнить данные заказа '{first_name}', "
                    "'{last_name}', '{postal_c}'")
    def fill_checkout_info(self, first_name, last_name, postal_c):
        """
        Заполняет данные для заказа.
        :param first_name: str — имя.
        :param last_name: str — фамилия.
        :param postal_c: str — индекс.
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_c)
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получить сумму заказа")
    def get_total_price(self):
        """
        Возвращает сумму заказа.
        :return: str — сумма заказа, отображенная на экране.
        """
        return self.driver.find_element(*self.total_label).text

    @allure.step("Форматировать сумму заказа '{price_text}'")
    def extract_price_value(self, price_text):
        """
        Возвращает сумму заказа в нужном виде, убирая всё, кроме цифр.
        :param price_text: str — сумма для обработки в виде строки.
        :return: float — сумма заказа, в виде нецелого числа.
        """
        price = ''.join(c for c in price_text if c.isdigit() or c == '.')
        return float(price)
