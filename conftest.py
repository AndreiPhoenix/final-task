import pytest
from selenium import webdriver
import tempfile
import os
import subprocess

def kill_chrome_processes():
    """Убивает все процессы Chrome/chromedriver"""
    try:
        subprocess.run(["pkill", "-f", "chrome"], stderr=subprocess.DEVNULL)
        subprocess.run(["pkill", "-f", "chromedriver"], stderr=subprocess.DEVNULL)
    except:
        pass

@pytest.fixture(scope="function")
def browser():
    # Убиваем старые процессы перед запуском
    kill_chrome_processes()

    # Создаем уникальную папку для профиля
    profile_dir = os.path.join(tempfile.gettempdir(), f"chrome_profile_{os.getpid()}")
    
    # Настройки Chrome
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={profile_dir}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Инициализация драйвера
    driver = webdriver.Chrome(options=options)
    
    yield driver
    
    # Завершение работы
    driver.quit()
    
    # Очистка профиля
    try:
        os.rmdir(profile_dir)
    except:
        pass

if os.getenv("CI"):  # Для GitHub Actions и подобных
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
