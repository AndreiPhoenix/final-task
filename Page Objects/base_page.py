from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, timeout)
        self.log = get_logger(self.__class__.__name__)

    def open(self):
        try:
            self.browser.get(self.url)
            self.log.info(f"Opened page: {self.url}")
        except Exception as e:
            self.log.error(f"Failed to open {self.url}: {e}")
            raise

    def get_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            self.log.error(f"Element not found: {locator}")
            raise

def save_cookies(self, path="cookies.pkl"):
    with open(path, 'wb') as file:
        pickle.dump(self.browser.get_cookies(), file)

def load_cookies(self, path="cookies.pkl"):
    with open(path, 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            self.browser.add_cookie(cookie)
