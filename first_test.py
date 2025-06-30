import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_example(browser):
    """Тест проверки заголовка главной страницы"""
    browser.get("https://example.com")
    logger.info("Открыта страница example.com")
    assert "Example Domain" in browser.title, "Некорректный заголовок страницы"
    logger.info("Проверка заголовка прошла успешно")

def test_login_valid(browser):
    """Тест авторизации с валидными данными"""
    try:
        # Открытие страницы логина
        browser.get("https://example.com/login")
        logger.info("Открыта страница авторизации")

        # Ожидание и ввод email
        email_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "email")),
            message="Поле email не найдено"
        )
        email_field.send_keys("valid@example.com")
        logger.info("Введен email")

        # Ожидание и ввод пароля
        password_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "password")),
            message="Поле пароля не найдено"
        )
        password_field.send_keys("securepassword123")
        logger.info("Введен пароль")

        # Клик по кнопке входа
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")),
            message="Кнопка входа не найдена или не кликабельна"
        )
        login_button.click()
        logger.info("Нажата кнопка входа")

        # Проверка успешной авторизации
        WebDriverWait(browser, 10).until(
            EC.url_contains("/dashboard"),
            message="Не удалось перейти на страницу dashboard"
        )
        logger.info("Авторизация прошла успешно")

    except Exception as e:
        logger.error(f"Ошибка в тесте авторизации: {str(e)}")
        browser.save_screenshot("login_error.png")
        raise
