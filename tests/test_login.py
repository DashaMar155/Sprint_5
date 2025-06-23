from auth_helper import AuthHelper
from data import TestLinks
from locators import TestLocators

class TestLogin:
    def test_login_from_main_page(self, driver, test_email, test_password):
        driver.get(TestLinks.main_page_link)
        auth = AuthHelper(driver)
        auth.login(test_email, test_password)
        # Проверка успешного входа
        assert driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR).is_displayed()
