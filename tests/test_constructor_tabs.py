import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestConstructorTabs:
    def test_switch_to_bread_tab(self, start_from_login_page):
        driver = start_from_login_page

        # Переключение на вкладку "Соусы", чтобы уйти с "Булки"
        sauce = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.inscription_sause)
        )
        driver.execute_script("arguments[0].scrollIntoView();", sauce)
        sauce.click()

        # Клик по вкладке "Булки"
        bread = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.inscription_bread)
        )
        bread.click()

        # Проверка, что "Булки" активны
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.active_section, "Булки")
        )
        active_section = driver.find_element(*Locators.active_section)
        assert "Булки" in active_section.text

    def test_switch_to_fillings_tab(self, start_from_login_page):
        driver = start_from_login_page

        # Клик по вкладке "Соусы"
        sauce = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.inscription_sause)
        )
        driver.execute_script("arguments[0].click();", sauce)

        # Клик по вкладке "Начинки"
        fillings = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.inscription_fillings)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings)
        driver.execute_script("arguments[0].click();", fillings)

        # Проверка, что "Начинки" активны
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.active_section, "Начинки")
        )
        active_section = driver.find_element(*Locators.active_section)
        assert "Начинки" in active_section.text

    def test_switch_to_sauce_tab(self, start_from_login_page):
        driver = start_from_login_page

        # Клик по вкладке "Начинки"
        fillings = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.inscription_fillings)
        )
        driver.execute_script("arguments[0].click();", fillings)

        # Клик по вкладке "Соусы"
        sauce = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.inscription_sause)
        )
        driver.execute_script("arguments[0].click();", sauce)

        # Проверка, что "Соусы" активны
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.active_section, "Соусы")
        )
        active_section = driver.find_element(*Locators.active_section)
        assert "Соусы" in active_section.text

