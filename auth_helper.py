from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import TestLinks

class AuthHelper:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.get(TestLinks.login_page_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(TestLocators.EMAIL_LOCATOR)).send_keys(email)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(TestLocators.PASSWORD_LOCATOR)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON_LOCATOR)).click()

    def logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON_LOCATOR)).click()

    def registration(self, email, password, name):
        self.driver.get(TestLinks.registration_page_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(TestLocators.EMAIL_LOCATOR)).send_keys(email)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(TestLocators.PASSWORD_LOCATOR)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(TestLocators.NAME_LOCATOR)).send_keys(name)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TestLocators.REGISTER_BUTTON_LOCATOR)).click()
