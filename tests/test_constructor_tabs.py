import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import TestLinks


class TestConstructorTabs:

    @pytest.mark.parametrize("tab_locator, active_tab_locator", [
        (TestLocators.CONSTRUCTOR_TAB_BUN_LOCATOR, TestLocators.ACTIVE_TAB_BUN_LOCATOR),
        (TestLocators.CONSTRUCTOR_TAB_SAUCE_LOCATOR, TestLocators.ACTIVE_TAB_SAUCE_LOCATOR),
        (TestLocators.CONSTRUCTOR_TAB_FILLING_LOCATOR, TestLocators.ACTIVE_TAB_FILLING_LOCATOR),
    ])
    def test_constructor_tabs(self, driver, tab_locator, active_tab_locator):
        driver.get(TestLinks.main_page_link)

        # Ждём, пока вкладка станет кликабельной (берём элемент <span>)
        tab_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(tab_locator))

        # Прокручиваем к элементу
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab_span)

        # Чтобы избежать ElementClickInterceptedException, кликаем через JS
        driver.execute_script("arguments[0].click();", tab_span)

        # Ждём, пока активная вкладка станет видимой
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(active_tab_locator))

        # Проверяем, что вкладка действительно активна (в её классе есть tab_tab_type_current)
        classes = active_tab.get_attribute("class")
        assert "tab_tab_type_current" in classes, f"Вкладка с локатором {tab_locator} не активна"
