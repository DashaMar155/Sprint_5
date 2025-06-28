from selenium.webdriver.common.by import By


class Locators:


# Кнопки

    # Кнопка "Войти в аккаунт" на главной странице
    entrance_on_the_main = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка "Выход" в личном кабинете
    button_exit = (By.XPATH, ".//button[contains(text(),'Выход')]")

    # Кнопка "Войти" (общая для форм входа)
    button_entrance = (By.XPATH, ".//button[contains(text(),'Войти')]")

    # Кнопка "Зарегистрироваться"
    button_register = (By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]")

    # Кнопка "Оформить заказ" (в корзине или после сборки бургера)
    button_arrange_order = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")

    # Кнопка "Личный кабинет" (в шапке сайта)
    button_personal_area = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")

    # Кнопка "Конструктор" (в шапке сайта)
    button_constaction = (By.XPATH, ".//a[@href='/']")


# Ссылки, текстовые

    # Ссылка "войти" (на странице регистрации)
    inscription_button_entrance = (By.XPATH, './/a[@href="/login"]')

    # Ссылка "Зарегистрироваться" (на странице входа)
    inscription_login = (By.CLASS_NAME, "Auth_link__1fOlj")

    # Надпись "Профиль" (в личном кабинете)
    inscription_profile = (By.XPATH, ".//a[@href='/account/profile']")

    # Надпись "Булки" (в разделе ингредиентов)
    inscription_bread = (By.XPATH, ".//span[contains(text(),'Булки')]")

    # Надпись "Соусы"
    inscription_sause = (By.XPATH, ".//span[contains(text(),'Соусы')]")

    # Надпись "Начинки"
    inscription_fillings = (By.XPATH, ".//span[contains(text(),'Начинки')]")

    # Активный раздел ингредиентов
    active_section = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]')

# Сообщения об ошибках

    # Сообщение: "Такой пользователь уже существует"
    inscription_error_account = (By.XPATH, ".//*[contains(text(),'Такой пользователь уже существует')]")

    # Сообщение: "Некорректный пароль"
    inscription_error_password = (By.XPATH, '//div[contains(@class, "input_status_error")]')



# Поля ввода

    # Поле ввода "Имя"
    field_name = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")

    # Поле ввода "Email"
    field_email = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")

    # Поле ввода "Пароль"
    field_password = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")




# Дополнительные элементы

    # Логотип (для проверки перехода на главную)
    logo = (By.XPATH, '//header/nav/div')

    # Кнопка "восстановить пароль"
    button_restore_password = (By.XPATH, './/a[@href="/forgot-password"]')