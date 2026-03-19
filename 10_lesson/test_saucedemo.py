from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from saucedemo_page import SauceDemoPage
import allure


@allure.title("Тестирование корзины магазина")
@allure.description("Тест проверяет корректность оборажаемой суммы в корзине")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_positive():
    """
    Тест проверяет правильность оборажаемой суммы в корзине,
    при оформлении заказа.

    :param driver: WebDriver — объект драйвера Selenium.
    :param username: str — логин.
    :param password: str — пароль.
    :param first_name: str — имя.
    :param last_name: str — фамилия.
    :param postal_c: str — индекс.
    :param price_text: str — сумма для обработки в виде строки.
    """
    gecko_driver_path = GeckoDriverManager().install()
    firefox_service = FirefoxService(gecko_driver_path)
    driver = webdriver.Firefox(service=firefox_service)
    try:
        saucedemo_page = SauceDemoPage(driver)
        with allure.step("Открытие страницы магазина"):
            saucedemo_page.open()
        with allure.step("Авторизация '{username}', '{password}'"):
            saucedemo_page.login("standard_user", "secret_sauce")
        with allure.step("Добавить рюкзак в корзину"):
            saucedemo_page.add_backpack_to_cart()
        with allure.step("Добавить футболку в корзину"):
            saucedemo_page.add_bolt_tshirt_to_cart()
        with allure.step("Добавить боди в корзину"):
            saucedemo_page.add_onesie_to_cart()
        with allure.step("Перейти в корзину"):
            saucedemo_page.go_to_cart()
        with allure.step("Нажать кнопку Checkout"):
            saucedemo_page.proceed_to_checkout()
        with allure.step(
                            "Заполнить данные заказа '{first_name}', "
                            "'{last_name}', '{postal_c}'"
                            ):
            saucedemo_page.fill_checkout_info("Katya", "Gubanova", "630027")
        with allure.step("Получить сумму заказа '{price_text}'"):
            total_text = saucedemo_page.get_total_price()
        print(f'{total_text}')

        with allure.step("Форматировать сумму заказа"):
            total_price = saucedemo_page.extract_price_value(total_text)
            expected_price = 58.29
        assert total_price == expected_price

    finally:
        driver.quit()
