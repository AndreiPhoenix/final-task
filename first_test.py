import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Неявное ожидание
    yield driver
    driver.quit()

def test_example(browser):
    browser.get("https://example.com")
    assert "Example Domain" in browser.title

def test_login_valid(browser):
    browser.get("https://example.com/login")
    
    email = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email.send_keys("valid@example.com")
    
    # ... остальные шаги теста ...
