import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless")  # Для запуска без GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.implicitly_wait(10)
        yield driver
    except Exception as e:
        pytest.fail(f"Browser initialization failed: {str(e)}")
    finally:
        driver.quit()

@pytest.fixture
def login_page(browser):
    return LoginPage(browser, "https://example.com/login")
