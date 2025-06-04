import pytest
from selenium import webdriver

def test_login_valid_credentials():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    
    email = driver.find_element("id", "email")
    email.send_keys("valid@example.com")
    
    password = driver.find_element("id", "password")
    password.send_keys("correct_password")
    
    login_button = driver.find_element("id", "login-btn")
    login_button.click()
    
    assert "Dashboard" in driver.title
    driver.quit()

def test_login_wrong_password():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    
    email = driver.find_element("id", "email")
    email.send_keys("valid@example.com")
    
    password = driver.find_element("id", "password")
    password.send_keys("wrong_password")
    
    login_button = driver.find_element("id", "login-btn")
    login_button.click()
    
    error_message = driver.find_element("id", "error-message").text
    assert error_message == "Неверный пароль"
    driver.quit()

... остальные 3 теста ...
