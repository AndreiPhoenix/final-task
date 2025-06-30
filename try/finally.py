def test_example(chrome_driver):
    try:
        chrome_driver.get("https://example.com")
        assert "Example" in chrome_driver.title
    finally:
        chrome_driver.quit()  # Завершаем сессию, даже если тест упал
