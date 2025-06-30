from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        try:
            self.browser.get(self.url)
        except Exception as e:
            raise Exception(f"Failed to open page {self.url}: {str(e)}")

    def is_element_present(self, by, locator):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((by, locator))
            return True
        except:
            return False

    def get_element(self, by, locator, timeout=10):
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((by, locator)))
        except Exception as e:
            raise Exception(f"Element not found: {locator}. Error: {str(e)}")
