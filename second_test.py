import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_valid_credentials(browser):
    browser.get("https://example.com/login")
    
    try:
        email = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email.send_keys("valid@example.com")
        
        # ... остальные шаги теста ...
        
        assert "Dashboard" in browser.title
    except Exception as e:
        pytest.fail(f"Test failed with exception: {str(e)}")

# ... остальные тесты ...
