import time
from pages.tables import Tables


def test_add_webtables(browser):

    web_t = Tables(browser)
    web_t.visit()
    web_t.add_row.click()

    assert web_t.window_add.exist()
    web_t.bth_add.click()

    assert web_t.window_add.exist()
    time.sleep(2)

    web_t.modal_first_name.send_keys('Name1')
    web_t.modal_last_name.send_keys('LastN')
    web_t.modal_email.send_keys('nnnnn@yandex.ru')
    web_t.modal_age.send_keys('33')
    web_t.modal_salary.send_keys('100000')
    web_t.modal_dep.send_keys('Dep')
    web_t.bth_add.click()
    time.sleep(2)

    assert web_t.fn_row.get_text() == 'Name1'

    web_t.edit1.click()
    web_t.modal_first_name.clear()
    web_t.modal_first_name.send_keys('Name2')
    web_t.bth_add.click()
    time.sleep(2)

    assert web_t.fn_row.get_text() == 'Name2'
    web_t.delete1.click()
    assert web_t.fn_row.get_text() == ' '