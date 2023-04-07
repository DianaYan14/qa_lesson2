import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_go():
    browser.open('https://google.com')
    browser.driver.maximize_window()
    # открытие браузера
    yield
    # закрытие браузера
    browser.quit()
