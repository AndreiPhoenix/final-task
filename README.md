# UI Automation Framework

## Запуск тестов
```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск всех тестов
pytest

# Запуск с генерацией отчета Allure
pytest --alluredir=allure-results
allure serve allure-results
