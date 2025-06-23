from auth_helper import AuthHelper
from data import TestLinks
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNavigationToAccount:
    def test_account_button_after_login(self, driver, test_email, test_password):
        # Авторизация
        auth = AuthHelper(driver)
        auth.login(test_email, test_password)

        # Проверяем, что кнопка "Личный Кабинет" появилась
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        )

        # Переход в личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR).click()

        # Проверка: находимся на странице профиля
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )
        assert "/account" in driver.current_url
