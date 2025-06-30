from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def enter_credentials(self, email, password):
        self.get_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.get_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        return self  # Для fluent-интерфейса

    def click_login(self):
        self.get_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.get_element(LoginPageLocators.ERROR_MESSAGE).text
