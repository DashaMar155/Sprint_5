import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Тест на активацию раздела 'Булки' в конструкторе
class TestCheckChapterBread:
    def test_check_chapter_bread(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Кликаем сначала по Соусам, чтобы уйти с вкладки Булки
        sause = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.inscription_sause))
        driver.execute_script("arguments[0].scrollIntoView();", sause)
        sause.click()

        # Кликаем по вкладке Булки
        bread = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.inscription_bread))
        driver.execute_script("arguments[0].scrollIntoView();", bread)
        bread.click()

        # Ждём, когда "Булки" станут активными
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.active_section, "Булки")
        )

        active_section = driver.find_element(*Locators.active_section)
        assert "Булки" in active_section.text



# Тест на активацию раздела 'Начинки' в конструкторе
class TestCheckChapterFillings:
    def test_check_chapter_fillings(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Клик по "Соусы" через JS, чтобы убрать возможные перекрытия
        sause = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.inscription_sause))
        driver.execute_script("arguments[0].click();", sause)

        # Клик по "Начинки" с прокруткой и через JS
        fillings = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.inscription_fillings))
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings)
        driver.execute_script("arguments[0].click();", fillings)

        # Ждем появления нужного текста
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.active_section, "Начинки")
        )

        active_section = driver.find_element(*Locators.active_section)
        assert "Начинки" in active_section.text



# Тест на активацию раздела 'Соусы' в конструкторе
class TestCheckChapterSauce:
    def test_check_chapter_sauce(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Клик по вкладке "Начинки"
        fillings = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.inscription_fillings))
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings)
        driver.execute_script("arguments[0].click();", fillings)

        # Клик по вкладке "Соусы"
        sause = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.inscription_sause))
        driver.execute_script("arguments[0].scrollIntoView(true);", sause)
        driver.execute_script("arguments[0].click();", sause)

        # Ждём, что в элементе active_section появится текст "Соусы"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(Locators.active_section, "Соусы")
        )

        active_section = driver.find_element(*Locators.active_section)
        assert "Соусы" in active_section.text

