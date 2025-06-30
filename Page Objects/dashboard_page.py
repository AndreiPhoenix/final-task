from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    # Локаторы элементов
    USER_MENU = (By.CSS_SELECTOR, ".user-menu")
    LOGOUT_BUTTON = (By.ID, "logout-btn")
    WELCOME_MESSAGE = (By.CLASS_NAME, "welcome-msg")
    NOTIFICATIONS_BELL = (By.ID, "notifications-bell")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-btn")
    
    def __init__(self, browser):
        super().__init__(browser, browser.current_url)  # Используем текущий URL

    def is_user_menu_visible(self):
        """Проверяет видимость меню пользователя"""
        try:
            return self.is_element_present(*self.USER_MENU)
        except Exception as e:
            raise Exception(f"Error checking user menu visibility: {str(e)}")

    def get_welcome_message(self):
        """Получает текст приветственного сообщения"""
        try:
            return self.get_element(*self.WELCOME_MESSAGE).text
        except Exception as e:
            raise Exception(f"Failed to get welcome message: {str(e)}")

    def click_logout(self):
        """Выполняет выход из системы"""
        try:
            self.get_element(*self.USER_MENU).click()
            self.get_element(*self.LOGOUT_BUTTON).click()
        except Exception as e:
            raise Exception(f"Logout failed: {str(e)}")

    def search(self, query):
        """Выполняет поиск по dashboard"""
        try:
            search_input = self.get_element(*self.SEARCH_INPUT)
            search_input.clear()
            search_input.send_keys(query)
            self.get_element(*self.SEARCH_BUTTON).click()
        except Exception as e:
            raise Exception(f"Search failed: {str(e)}")

    def open_notifications(self):
        """Открывает панель уведомлений"""
        try:
            self.get_element(*self.NOTIFICATIONS_BELL).click()
        except Exception as e:
            raise Exception(f"Failed to open notifications: {str(e)}")

    def is_notification_count_equal(self, expected_count):
        """Проверяет количество уведомлений"""
        try:
            badge = self.get_element(By.CSS_SELECTOR, f"{self.NOTIFICATIONS_BELL[1]} .badge")
            return int(badge.text) == expected_count
        except:
            return False
