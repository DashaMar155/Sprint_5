from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from auth_helper import AuthHelper
from data import TestLinks
from locators import TestLocators


class TestLogin:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page(self, driver, registered_user):
        test_mail, test_pass = registered_user
        driver.get(TestLinks.main_page_link)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON_LOCATOR)
        ).click()
        AuthHelper.login(driver, test_mail, test_pass)
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, \
            "Ошибка перехода на главную страницу после логина."

    # Вход через кнопку «Личный кабинет»
    def test_login_from_personal_account_button(self, driver, registered_user):
        test_mail, test_pass = registered_user
        driver.get(TestLinks.main_page_link)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        ).click()
        AuthHelper.login(driver, test_mail, test_pass)
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, \
            "Ошибка перехода на главную страницу после логина."

    # Вход через кнопку в форме регистрации
    def test_login_from_registration_link(self, driver, registered_user):
        test_mail, test_pass = registered_user
        driver.get(TestLinks.registration_page_link)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)
        ).click()
        AuthHelper.login(driver, test_mail, test_pass)
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, \
            "Ошибка перехода на главную страницу после логина."

    # Вход через кнопку в форме восстановления пароля
    def test_login_from_forgot_password_link(self, driver, registered_user):
        test_mail, test_pass = registered_user
        driver.get(TestLinks.login_page_link)
        # Клик на ссылку "Восстановить пароль"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(TestLocators.FORGOT_PASSWORD_LINK_LOCATOR)
        ).click()
        # На странице восстановления пароля кликаем по ссылке "Войти"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)
        ).click()
        AuthHelper.login(driver, test_mail, test_pass)
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, \
            "Ошибка перехода на главную страницу после логина."
