import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_valid_login(driver):
    """Тест 1: Проверка входа с валидными данными"""
    driver.get("https://example.com/login")
    
    driver.find_element(By.ID, "email").send_keys("valid@example.com")
    driver.find_element(By.ID, "password").send_keys("correct_password")
    driver.find_element(By.ID, "login-btn").click()
    
    assert "Главная страница" in driver.title

def test_invalid_password(driver):
    """Тест 2: Проверка входа с неверным паролем"""
    driver.get("https://example.com/login")
    
    driver.find_element(By.ID, "email").send_keys("valid@example.com")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-btn").click()
    
    error = driver.find_element(By.CLASS_NAME, "error-message").text
    assert error == "Неверный пароль", f"Ожидалось 'Неверный пароль', получено '{error}'"

def test_empty_email(driver):
    """Тест 3: Проверка входа без email"""
    driver.get("https://example.com/login")
    
    driver.find_element(By.ID, "password").send_keys("some_password")
    driver.find_element(By.ID, "login-btn").click()
    
    error = driver.find_element(By.CLASS_NAME, "error-message").text
    assert "Email обязателен" in error

... остальные 2 теста для FIRST.md ...
