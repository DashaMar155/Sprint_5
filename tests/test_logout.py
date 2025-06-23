from auth_helper import AuthHelper
from data import TestLinks
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogout:
    def test_logout_from_account(self, driver, test_email, test_password):
        auth = AuthHelper(driver)
        auth.login(test_email, test_password)

        # Проверим, что мы успешно вошли и находимся на главной
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        )

        # Нажимаем кнопку "Личный кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        ).click
