import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from generation_ep import EmailPasswordGenerator
from data import main_site, profile_site, login_site, register_site
from curl import *
from data import Credantial


# ----------------- Тесты регистрации -----------------

@pytest.mark.usefixtures("start_from_main_not_login")
class TestRegistration:

    # Успешная регистрация нового пользователя
    @pytest.mark.usefixtures("register_new_account")
    def test_successful_registration(self, register_new_account):
        driver, email, password = register_new_account
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site

    # Попытка зарегистрировать уже существующего пользователя
    def test_registration_existing_user(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)
        driver.find_element(*Locators.field_password).send_keys(Credantial.password)
        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.inscription_error_account))

    # Проверка валидации пароля (короткий)
    def test_invalid_password(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        email = EmailPasswordGenerator().generate()[0]

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys("12345")
        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_error_password))

    # Регистрация без пароля
    def test_missing_password(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        email = EmailPasswordGenerator().generate()[0]

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.button_register).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site

    # Регистрация без email
    def test_missing_email(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        password = EmailPasswordGenerator().generate()[1]

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_register).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site

    # Регистрация без имени
    def test_missing_name(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        email, password = EmailPasswordGenerator().generate()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_register).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site


# ----------------- Тесты навигации -----------------

@pytest.mark.usefixtures("start_from_login_page")
class TestNavigation:

    # Переход на главную через кнопку «Конструктор»
    def test_go_to_main_by_constructor(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_constructor))
        driver.find_element(*Locators.button_constructor).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site

    # Переход на главную по логотипу
    def test_go_to_main_by_logo(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_personal_area))
        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_profile))
        driver.find_element(*Locators.logo).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site

    # Переход в личный кабинет
    def test_go_to_profile(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))
        driver.find_element(*Locators.button_personal_area).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(profile_site))
        assert driver.current_url == profile_site

    # Выход из аккаунта
    def test_logout(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.button_exit)).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))
        assert driver.current_url == login_site

