from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestLinks
from locators import TestLocators


# Содаём класс для проверки перехода в личный кабинет
class TestNavigationToPersonalAccount:
    # Проверяем переход по клику на кнопку «Личный кабинет»
    def test_navigation_to_personal_account(self, driver, authorized_user):
        # Клик по кнопке «Личный кабинет»
        WebDriverWait(
            driver, 5).until(
            EC.element_to_be_clickable(
                TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()
        # Проверка перехода в личный кабинет
        WebDriverWait(
            driver, 10).until(
            EC.url_contains(
                TestLinks.personal_account_page_link))
        assert driver.current_url == TestLinks.personal_account_page_link, (
            "Ошибка перехода в личный кабинет."
        )
