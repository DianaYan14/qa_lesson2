import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_go():
    browser.open('https://google.com')
    browser.driver.set_window_size(1920, 1080)
    # открытие браузера
    yield
    # закрытие браузера
    browser.quit()
