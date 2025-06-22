from selenium.webdriver.common.by import By

class TestLocators:
    # Поля ввода
    EMAIL_LOCATOR = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_LOCATOR = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    NAME_LOCATOR = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    # Кнопки
    LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(), 'Войти')]")
    REGISTER_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//*[contains(@class, 'Account_button')]")

    # Ссылки
    LOGIN_LINK_LOCATOR = (By.XPATH, "//a[contains(text(), 'Войти')]")
    FORGOT_PASSWORD_LINK_LOCATOR = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")

    # Ошибки
    WRONG_PASS_MESSAGE_LOCATOR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, ".input__error.text_type_main-default")

    # Хэдер
    PERSONAL_ACCOUNT_BUTTON_LOCATOR = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]")
    CONSTRUCTOR_BUTTON_LOCATOR = (By.XPATH, "//*[contains(text(), 'Конструктор')]")
    LOGO_LOCATOR = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]")

