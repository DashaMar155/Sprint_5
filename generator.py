import random
import string


# Класс для генерации тестовых данных
class Generator:
    name = 'nika'
    surname = 'isaeva'
    cogort_number = '06'
    domain = 'mail.ru'

    @staticmethod
    def random_digits(length=3):
        return ''.join(random.choices(string.digits, k=length))

    @classmethod
    def generate_email(cls):
        test_email = f"{cls.name}_{cls.surname}_{cls.cogort_number}_{cls.random_digits()}@{cls.domain}"
        return test_email

    @staticmethod
    def generate_password(length=6):
        test_pass = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return test_pass
