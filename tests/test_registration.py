import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from generation_ep import EmailPasswordGenerator
from locators import Locators
from conftest import driver, register_new_account, start_from_main_not_login
from data import Credantial
from curl import *


# успешная регистрация нового пользователя
@pytest.mark.usefixtures("register_new_account")
class TestRegistrationNewUser:
    def test_registration(self, register_new_account):

        driver, email, password = register_new_account
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site


# попытка зарегистрировать существующего пользователя
@pytest.mark.usefixtures("start_from_main_not_login")
class TestExistingAccount:
    def test_existing_account(self, start_from_main_not_login):

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


# проверка валидации поля "Пароль"
@pytest.mark.usefixtures("start_from_main_not_login")
class TestInvalidPassword:
    def test_invalid_password(self, start_from_main_not_login):

        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()

        email = EmailPasswordGenerator().generate()[0]

        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)
        driver.find_element(*Locators.field_password).send_keys("12345")  # Невалидный пароль
        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_error_password))


# проверка регистрации без пароля
@pytest.mark.usefixtures("start_from_main_not_login")
class TestMissingPassword:
    def test_missing_password(self, start_from_main_not_login):

        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()

        email = EmailPasswordGenerator().generate()[0]

        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.button_register).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site


# проверка регистрации без email
@pytest.mark.usefixtures("start_from_main_not_login")
class TestMissingEmail:
    def test_missing_email(self, start_from_main_not_login):

        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()

        generator = EmailPasswordGenerator()
        password = generator.generate()
        driver.find_element(*Locators.field_name).send_keys(Credantial.name)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_register).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site


# проверка регистрации без имени
@pytest.mark.usefixtures("start_from_main_not_login")
class TestMissingName:
    def test_missing_name(self, start_from_main_not_login):

        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        driver.find_element(*Locators.inscription_login).click()

        generator = EmailPasswordGenerator()
        email, password = generator.generate()

        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_register).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site


