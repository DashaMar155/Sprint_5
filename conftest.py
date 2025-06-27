import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from auth_helper import AuthHelper
from data import TestLinks, Credantial
from generation_ep import generate_unique_email


# Фикстура WebDriver
@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# Фикстура: уникальный email
@pytest.fixture
def test_email():
    return generate_unique_email()


# Фикстура: фиксированный пароль (из data.py)
@pytest.fixture
def test_password():
    return Credantial.password


# Фикстура: имя пользователя (из data.py)
@pytest.fixture
def test_name():
    return Credantial.name


# Фикстура для регистрации пользователя
@pytest.fixture
def registered_user(driver, test_email, test_password, test_name):
    driver.get(TestLinks.registration_page_link)
    AuthHelper.register(driver, test_email, test_password, test_name)
    AuthHelper.confirm_successful_registration(driver)
    return test_email, test_password


# Фикстура для авторизованного пользователя
@pytest.fixture
def authorized_user(driver, registered_user):
    email, password = registered_user
    driver.get(TestLinks.login_page_link)
    AuthHelper.login(driver, email, password)
    AuthHelper.confirm_successful_login(driver)
    return email, password



