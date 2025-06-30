import pytest
from selenium import webdriver
import tempfile
import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def kill_chrome_processes():
    """Завершает все процессы Chrome и chromedriver"""
    try:
        # Для Linux/MacOS
        subprocess.run(["pkill", "-f", "chrome"], stderr=subprocess.DEVNULL)
        subprocess.run(["pkill", "-f", "chromedriver"], stderr=subprocess.DEVNULL)
        # Для Windows (раскомментировать если нужно)
        # subprocess.run(["taskkill", "/f", "/im", "chrome.exe"], stderr=subprocess.DEVNULL)
        # subprocess.run(["taskkill", "/f", "/im", "chromedriver.exe"], stderr=subprocess.DEVNULL)
    except Exception as e:
        logger.warning(f"Failed to kill processes: {e}")

@pytest.fixture(scope="function")
def browser():
    """Фикстура для создания браузера с изолированным профилем"""
    kill_chrome_processes()
    
    # Создаем уникальный временный профиль
    profile_path = os.path.join(tempfile.gettempdir(), f"chrome_{os.getpid()}")
    os.makedirs(profile_path, exist_ok=True)
    
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Для CI-серверов (раскомментировать если нужно)
    # if os.getenv("CI"):
    #     options.add_argument("--headless")
    #     options.add_argument("--disable-gpu")
    
    logger.info(f"Starting Chrome with profile: {profile_path}")
    driver = webdriver.Chrome(options=options)
    
    yield driver
    
    logger.info("Closing browser...")
    driver.quit()
    
    # Очистка профиля
    try:
        os.rmdir(profile_path)
    except Exception as e:
        logger.warning(f"Failed to remove profile dir: {e}")
