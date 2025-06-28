import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import main_site, profile_site, login_site


class TestMainPageNavigation:

    # Переход на главную через кнопку «Конструктор»
    def test_transition_by_constructor_button(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_constructor))
        driver.find_element(*Locators.button_constructor).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

    # Переход на главную через логотип
    def test_transition_by_logo_click(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_personal_area))
        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.inscription_profile))
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

    # Переход в личный кабинет
    def test_transition_to_profile(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))
        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(profile_site))

        assert driver.current_url == profile_site

    # Выход из аккаунта
    def test_logout_from_profile(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        driver.find_element(*Locators.button_personal_area).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.button_exit)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))

        assert driver.current_url == login_site
