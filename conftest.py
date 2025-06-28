import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from auth_helper import AuthHelper
from data import TestLinks, Credantial
from generation_ep import generate_unique_email


# Фикстура для WebDriver
@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# Фикстура: уникальный email (генератор)
@pytest.fixture
def test_email():
    return generate_unique_email()


# Фикстура: зарегистрированный пользователь
@pytest.fixture
def registered_user(driver, test_email):
    driver.get(TestLinks.registration_page_link)
    AuthHelper.register(driver, test_email, Credantial.password, Credantial.name)
    AuthHelper.confirm_successful_registration(driver)
    return test_email, Credantial.password


# Фикстура: авторизованный пользователь
@pytest.fixture
def authorized_user(driver, registered_user):
    email, password = registered_user
    driver.get(TestLinks.login_page_link)
    AuthHelper.login(driver, email, password)
    AuthHelper.confirm_successful_login(driver)
    return email, password
