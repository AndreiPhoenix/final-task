from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.ID, "error-message")

    def enter_email(self, email):
        try:
            self.get_element(*self.EMAIL_INPUT).send_keys(email)
        except Exception as e:
            raise Exception(f"Failed to enter email: {str(e)}")

    def enter_password(self, password):
        try:
            self.get_element(*self.PASSWORD_INPUT).send_keys(password)
        except Exception as e:
            raise Exception(f"Failed to enter password: {str(e)}")

    def click_login(self):
        try:
            self.get_element(*self.LOGIN_BUTTON).click()
        except Exception as e:
            raise Exception(f"Failed to click login button: {str(e)}")

    def get_error_message(self):
        try:
            return self.get_element(*self.ERROR_MESSAGE).text
        except Exception as e:
            raise Exception(f"Failed to get error message: {str(e)}")
