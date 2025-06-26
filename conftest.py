import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *
from data import Credantial
from generation_ep import EmailPasswordGenerator


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def start_from_login_page(driver):

    driver.get(login_site)
    driver.find_element(*Locators.field_email).send_keys(Credantial.email)
    driver.find_element(*Locators.field_password).send_keys(Credantial.password)
    driver.find_element(*Locators.button_entrance).click()
    return driver


@pytest.fixture
def start_from_recovery_page(driver):

    driver.get(login_site)
    driver.find_element(*Locators.button_restore_password).click()

    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.inscription_button_entrance))

    driver.find_element(*Locators.inscription_button_entrance).click()
    driver.find_element(*Locators.field_email).send_keys(Credantial.email)
    driver.find_element(*Locators.field_password).send_keys(Credantial.password)
    driver.find_element(*Locators.button_entrance).click()
    return driver


@pytest.fixture
def start_from_main_not_login(driver):

    driver.get(main_site)
    return driver


@pytest.fixture
def register_new_account(driver):

    driver.get(login_site)
    driver.find_element(*Locators.inscription_login).click()

    generator = EmailPasswordGenerator()
    email, password = generator.generate()

    driver.find_element(*Locators.field_name).send_keys(Credantial.name)
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_register).click()

    WebDriverWait(driver, 4).until(EC.visibility_of_element_located(Locators.button_entrance)).click()

    return driver, email, password


