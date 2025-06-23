import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def test_email():
    return "testuser_1750667081974@yandex.ru"

@pytest.fixture(scope="function")
def test_password():
    return "111111"
