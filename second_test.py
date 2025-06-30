import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_login_valid_credentials(browser):
    """Тест авторизации с валидными учетными данными"""
    try:
        # 1. Открытие страницы логина
        browser.get("https://example.com/login")
        logger.info("Открыта страница авторизации")
        
        # 2. Ввод email
        email_field = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "email")),
            message="Поле email не найдено или не видимо"
        )
        email_field.clear()
        email_field.send_keys("valid@example.com")
        logger.info("Введен валидный email")
        
        # 3. Ввод пароля
        password_field = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "password")),
            message="Поле пароля не найдено или не видимо"
        )
        password_field.clear()
        password_field.send_keys("securepassword123")
        logger.info("Введен пароль")
        
        # 4. Клик по кнопке входа
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")),
            message="Кнопка входа не кликабельна"
        )
        login_button.click()
        logger.info("Нажата кнопка входа")
        
        # 5. Проверка успешной авторизации
        WebDriverWait(browser, 15).until(
            EC.title_contains("Dashboard"),
            message="Не удалось перейти в личный кабинет"
        )
        logger.info("Успешная авторизация, отображен Dashboard")
        
        # 6. Дополнительная проверка элемента на новой странице
        welcome_message = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome')]")),
            message="Приветственное сообщение не найдено"
        )
        assert welcome_message.is_displayed(), "Приветственное сообщение не отображается"
        
    except Exception as e:
        browser.save_screenshot("login_error.png")
        logger.error(f"Ошибка в тесте авторизации: {str(e)}")
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")

def test_login_invalid_password(browser):
    """Тест авторизации с неверным паролем"""
    try:
        browser.get("https://example.com/login")
        
        # Заполнение формы
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        ).send_keys("valid@example.com")
        
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        ).send_keys("wrongpassword")
        
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        ).click()
        
        # Проверка сообщения об ошибке
        error_message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message")),
            message="Сообщение об ошибке не появилось"
        )
        assert "Invalid credentials" in error_message.text, "Неверное сообщение об ошибке"
        
    except Exception as e:
        browser.save_screenshot("invalid_login_error.png")
        logger.error(f"Ошибка в тесте невалидной авторизации: {str(e)}")
        raise

def test_password_recovery(browser):
    """Тест восстановления пароля"""
    try:
        browser.get("https://example.com/login")
        
        # Клик по ссылке "Забыли пароль?"
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Forgot password?"))
        ).click()
        
        # Проверка перехода на страницу восстановления
        WebDriverWait(browser, 10).until(
            EC.url_contains("/password-recovery"),
            message="Не удалось перейти на страницу восстановления пароля"
        )
        
        # Заполнение email для восстановления
        recovery_email = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "recovery-email"))
        )
        recovery_email.send_keys("user@example.com")
        
        # Отправка формы
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Send Link')]"))
        ).click()
        
        # Проверка сообщения об успехе
        success_message = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")),
            message="Сообщение об успешной отправке не появилось"
        )
        assert "recovery link has been sent" in success_message.text.lower()
        
    except Exception as e:
        browser.save_screenshot("password_recovery_error.png")
        logger.error(f"Ошибка в тесте восстановления пароля: {str(e)}")
        raise
