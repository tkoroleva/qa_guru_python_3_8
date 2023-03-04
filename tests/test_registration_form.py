from demoqa_tests.model.pages import practice_form


def test_registration_form():
    practice_form.open_page()

    practice_form.input_personal_data(name='QA',
                                      surname='GURU',
                                      email='test@qa.guru',
                                      phone_number='7999123456',
                                      address='Russia, Moscow'
                                      )

    practice_form.select_gender('Other')

    practice_form.click_on_datepicker()
    practice_form.pick_year('2022')
    practice_form.pick_month('November')
    practice_form.pick_day(16)

    practice_form.input_subjects('Computer Science')

    practice_form.select_hobbies('Reading')

    practice_form.upload_picture('res/logo.png')

    practice_form.scroll_to_address()

    practice_form.select_state('Haryana')

    practice_form.select_city('Panipat')

    practice_form.submit()

    practice_form.check_fields('QA GURU',
                               'test@qa.guru',
                               'Other',
                               '7999123456',
                               '16 November,2022',
                               'Computer Science',
                               'Reading',
                               'logo.png',
                               'Russia, Moscow',
                               'Haryana Panipat'
                               )
