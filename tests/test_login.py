import pytest
from pages.login_page import LoginPage

@pytest.mark.login
class TestLogin:
    @pytest.mark.positive
    def test_valid_login(self, browser):
        try:
            login_page = LoginPage(browser, "https://example.com/login")
            login_page.open()
            login_page.enter_email("valid@example.com")
            login_page.enter_password("correct_password")
            login_page.click_login()
            
            assert "Dashboard" in browser.title, "Login failed"
        except Exception as e:
            pytest.fail(f"Test failed with exception: {str(e)}")

    @pytest.mark.negative
    def test_invalid_password(self, browser):
        try:
            login_page = LoginPage(browser, "https://example.com/login")
            login_page.open()
            login_page.enter_email("valid@example.com")
            login_page.enter_password("wrong_password")
            login_page.click_login()
            
            error_message = login_page.get_error_message()
            assert error_message == "Неверный пароль", f"Unexpected error message: {error_message}"
        except Exception as e:
            pytest.fail(f"Test failed with exception: {str(e)}")
