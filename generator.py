import time

def generate_unique_email():
    timestamp = int(time.time() * 1000)
    return f"testuser_{timestamp}@yandex.ru"
