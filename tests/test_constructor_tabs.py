import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestConstructorTabs:
    def test_check_chapter_bread(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Клик по вкладке "Соусы", чтобы уйти с "Булки"
        sause = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.inscription_sause)
        )
        driver.execute_script("arguments[0].scrollIntoView();", sause)
        sause.click()

        # Клик по вкладке "Булки"
        bread = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.inscription_bread)
        )
        driver.execute_script("arguments[0].scrollIntoView();", bread)
        bread.click()

        # Проверка, что вкладка "Булки" активна
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.active_section, "Булки")
        )
        active_section = driver.find_element(*Locators.active_section)
        assert "Булки" in active_section.text

    def test_check_chapter_fillings(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Клик по вкладке "Соусы" через JS
        sause = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.inscription_sause)
        )
        driver.execute_script("arguments[0].click();", sause)

        # Клик по вкладке "Начинки"
        fillings = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.inscription_fillings)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings)
        driver.execute_script("arguments[0].click();", fillings)

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.active_section, "Начинки")
        )
        active_section = driver.find_element(*Locators.active_section)
        assert "Начинки" in active_section.text

    def test_check_chapter_sauce(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Клик по вкладке "Начинки"
        fillings = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.inscription_fillings)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings)
        driver.execute_script("arguments[0].click();", fillings)

        # Клик по вкладке "Соусы"
        sause = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.inscription_sause)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", sause)
        driver.execute_script("arguments[0].click();", sause)

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(Locators.active_section, "Соусы")
        )
        active_section = driver.find_element(*Locators.active_section)
        assert "Соусы" in active_section.text

