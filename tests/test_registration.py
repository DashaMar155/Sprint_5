from auth_helper import AuthHelper
from data import TestLinks


class TestRegistration:
    def test_successful_registration(self, driver, test_email, test_password):
        auth = AuthHelper(driver)
        auth.registration(test_email, test_password, "Дарья")

        # Можно добавить проверку успешной регистрации, например:
        # assert "Личный Кабинет" in driver.page_source
