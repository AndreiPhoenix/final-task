import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class TestDashboard:
    def test_successful_login_logout(self, browser):
        try:
            # Логинимся
            login_page = LoginPage(browser, "https://example.com/login")
            login_page.open()
            login_page.enter_email("valid@example.com")
            login_page.enter_password("correct_password")
            login_page.click_login()
            
            # Работаем с dashboard
            dashboard_page = DashboardPage(browser)
            assert dashboard_page.is_user_menu_visible(), "User menu not visible after login"
            
            # Выходим
            dashboard_page.click_logout()
            assert "Login" in browser.title, "Logout failed"
            
        except Exception as e:
            pytest.fail(f"Test failed with exception: {str(e)}")

    def test_welcome_message(self, browser):
        try:
            # Предполагаем, что мы уже залогинены (можно использовать фикстуру)
            dashboard_page = DashboardPage(browser)
            welcome_text = dashboard_page.get_welcome_message()
            assert "Welcome" in welcome_text, f"Unexpected welcome message: {welcome_text}"
            
        except Exception as e:
            pytest.fail(f"Test failed with exception: {str(e)}")
