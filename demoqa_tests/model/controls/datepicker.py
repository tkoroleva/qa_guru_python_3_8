from selene import have
from selene.support.shared import browser


def date_of_birth(selector, value):
    browser.element(selector).all('option').element_by(have.exact_text(value)).click()
