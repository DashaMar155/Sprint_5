from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import TestLinks
from locators import TestLocators
from auth_helper import AuthHelper


class TestNavigationToConstructor:

    def test_constructor_button_from_account(self, driver, test_email, test_password):
        auth = AuthHelper(driver)
        auth.login(test_email, test_password)

        # Нажимаем кнопку "Конструктор"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUTTON_LOCATOR)
        ).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link

    def test_logo_click_from_account(self, driver, test_email, test_password):
        auth = AuthHelper(driver)
        auth.login(test_email, test_password)

        # Нажимаем на логотип
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(TestLocators.LOGO_LOCATOR)
        ).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link
