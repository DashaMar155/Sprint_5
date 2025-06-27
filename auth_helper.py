from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthPageLocators


class AuthHelper:

    @staticmethod
    def register(driver, email, password, name):
        name_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthPageLocators.input_name)
        )
        name_input.clear()
        name_input.send_keys(name)

        email_input = driver.find_element(*AuthPageLocators.input_email)
        email_input.clear()
        email_input.send_keys(email)

        password_input = driver.find_element(*AuthPageLocators.input_password)
        password_input.clear()
        password_input.send_keys(password)

        register_button = driver.find_element(*AuthPageLocators.button_register)
        register_button.click()

    @staticmethod
    def confirm_successful_registration(driver):
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))

    @staticmethod
    def login(driver, email, password):
        email_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthPageLocators.input_email)
        )
        email_input.clear()
        email_input.send_keys(email)

        password_input = driver.find_element(*AuthPageLocators.input_password)
        password_input.clear()
        password_input.send_keys(password)

        login_button = driver.find_element(*AuthPageLocators.button_login)
        login_button.click()

    @staticmethod
    def confirm_successful_login(driver):
        WebDriverWait(driver, 5).until(EC.url_contains("/"))
