from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthHelper:

    @staticmethod
    def registration(driver, email, password, name):
        # Заполняем имя
        name_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ".//*[text()='Имя']/following-sibling::input"))
        )
        name_input.clear()
        name_input.send_keys(name)

        # Заполняем email
        email_input = driver.find_element(By.XPATH, ".//*[text()='Email']/following-sibling::input")
        email_input.clear()
        email_input.send_keys(email)

        # Заполняем пароль
        password_input = driver.find_element(By.XPATH, ".//*[text()='Пароль']/following-sibling::input")
        password_input.clear()
        password_input.send_keys(password)

        # Нажимаем кнопку "Зарегистрироваться"
        register_button = driver.find_element(By.XPATH, '//*[contains(@class, "button_button_type_primary")]')
        register_button.click()

    @staticmethod
    def confirm_registration_success(driver):
        # Можно проверять, что URL сменился на страницу логина
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))

    @staticmethod
    def login(driver, email, password):
        email_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ".//*[text()='Email']/following-sibling::input"))
        )
        email_input.clear()
        email_input.send_keys(email)

        password_input = driver.find_element(By.XPATH, ".//*[text()='Пароль']/following-sibling::input")
        password_input.clear()
        password_input.send_keys(password)

        login_button = driver.find_element(By.XPATH, '//*[contains(@class, "button_button_type_primary")]')
        login_button.click()

    @staticmethod
    def confirm_login_success(driver):
        # Проверяем, что после входа URL стал главным
        WebDriverWait(driver, 5).until(EC.url_contains("/"))

