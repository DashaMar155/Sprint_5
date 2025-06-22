from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from auth_helper import AuthHelper
from data import TestLinks
from locators import TestLocators


class TestRegistration:
    # Проверяем успешную регистрацию
    def test_successful_registration(self, driver, test_email, test_password, test_name):
        # Переход на страницу регистрации
        driver.get(TestLinks.registration_page_link)

        # Используем функцию для регистрации
        AuthHelper.registration(driver, test_email, test_password, test_name)

        # Проверяем перенаправление на страницу логина после регистрации
        AuthHelper.confirm_registration_success(driver)

        # Проверка URL
        current_url = driver.current_url
        expected_url = TestLinks.login_page_link
        assert current_url == expected_url, (
            f"Ожидался переход на {expected_url}, но сейчас {current_url}"
        )

    # Проверяем ошибку при вводе некорректного пароля
    def test_invalid_password_registration(self, driver, test_email):
        driver.get(TestLinks.registration_page_link)

        invalid_pass = "123"
        name = "Тест"

        # Ввод данных
        driver.find_element(*TestLocators.NAME_LOCATOR).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_LOCATOR).send_keys(test_email)
        driver.find_element(*TestLocators.PASSWORD_LOCATOR).send_keys(invalid_pass)

        # Клик по кнопке регистрации
        driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()

        # Проверка сообщения об ошибке
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.WRONG_PASS_MESSAGE_LOCATOR)
        ).text

        expected_message = "Некорректный пароль"
        assert expected_message in error_message, (
            f"Ожидалось сообщение '{expected_message}', но получили: '{error_message}'"
        )
