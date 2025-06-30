import tempfile
import os
import pytest
from selenium import webdriver

@pytest.fixture
def chrome_driver():
    options = webdriver.ChromeOptions()
    
    # Создаём уникальную временную папку для user-data-dir
    user_data_dir = os.path.join(tempfile.gettempdir(), f"chrome_profile_{os.getpid()}")
    options.add_argument(f"--user-data-dir={user_data_dir}")
    
    # Другие настройки (если нужны)
    options.add_argument("--headless")  # Пример: запуск без GUI
    
    driver = webdriver.Chrome(options=options)
    yield driver
    
    # Важно: закрываем драйвер после теста
    driver.quit()
    
    # Очистка (опционально)
    try:
        os.rmdir(user_data_dir)
    except OSError:
        pass
