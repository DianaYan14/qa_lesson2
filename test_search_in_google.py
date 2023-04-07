from selene import be, have
from selene import browser


def test_positive_case(browser_go):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_case(browser_go):
    browser.element('[name="q"]').clear()
    browser.element('[name="q"]').should(be.blank).type('zxcvbn4567').press_enter()
    browser.element('[class="card-section"]').should(have.text('Страницы, содержащие все слова запроса, не найдены.'))
