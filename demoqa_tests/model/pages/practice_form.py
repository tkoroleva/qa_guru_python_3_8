from selene import have
from selene.support.shared import browser
from demoqa_tests.model.controls import checkbox, datepicker, dropdown, radiobutton
from demoqa_tests.utils.path_to_file import define_path
from demoqa_tests.utils.scroll import scroll_to


def open_page():
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.7)"')


def input_personal_data(name, surname, email, phone_number, address):
    browser.element('#firstName').type(name)
    browser.element('#lastName').type(surname)
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').type(phone_number)
    browser.element('#currentAddress').type(address)


def select_gender(gender):
    radiobutton.gender('[name=gender]', gender)


def click_on_datepicker():
    browser.element('#dateOfBirthInput').click()


def pick_year(year):
    browser.element('.react-datepicker__year-select').click()
    datepicker.date_of_birth('.react-datepicker__year-select', year)


def pick_month(month):
    browser.element('.react-datepicker__month-select').click()
    datepicker.date_of_birth('.react-datepicker__month-select', month)


def pick_day(day):
    browser.element(f'.react-datepicker__day--0{day}').click()


def input_subjects(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def select_hobbies(*texts):
    checkbox.select(browser.all('[for^=hobbies-checkbox-2]'), *texts)


def scroll_to_address():
    scroll_to('#currentAddress')


def upload_picture(file):
    browser.element('#uploadPicture').set_value(define_path(file))


def select_state(value):
    dropdown.select('#state', by_text=value)


def select_city(value):
    dropdown.select('#city', by_text=value)


def submit():
    browser.element('#submit').press_enter()


def check_fields(*args):
    browser.element('.table').all('td').even.should(have.texts(args))
