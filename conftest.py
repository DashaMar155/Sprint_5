import pytest
import time
from selenium import webdriver
from auth_helper import AuthHelper
from data import TestLinks

# Функция генерации уникального email с таймстампом
def generate_unique_email():
    timestamp = int(time.time() * 1000)
    return f"testuser_{timestamp}@yandex.ru"

# Фикстура драйвера
@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

# Фикстура с уникальным email
@pytest.fixture
def test_email():
    return generate_unique_email()

# Фикстура с фиксированным паролем
@pytest.fixture
def test_password():
    return "111111"

# Фикстура с именем пользователя
@pytest.fixture
def test_name():
    return "Дарья"

# Фикстура предварительной регистрации пользователя
@pytest.fixture
def registered_user(driver, test_email, test_password, test_name):
    driver.get(TestLinks.registration_page_link)
    AuthHelper.registration(driver, test_email, test_password, test_name)  # Важно: передаём имя
    AuthHelper.confirm_registration_success(driver)
    return test_email, test_password

# Фикстура авторизованного пользователя, использует уже зарегистрированного
@pytest.fixture
def authorized_user(driver, registered_user):
    email, password = registered_user
    driver.get(TestLinks.login_page_link)
    AuthHelper.login(driver, email, password)
    AuthHelper.confirm_login_success(driver)
    return email, password

