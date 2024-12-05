from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()
    assert modal_elements.btns_locator.check_count_elements(5)


def test_navigation_modal(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()
    modal_elements.refresh()
    modal_elements.btn_icon.click()
    modal_elements.back()
    browser.set_window_size(900, 400)
    modal_elements.forward()
    assert modal_elements.get_url() == 'https://demoqa.com/'
    assert modal_elements.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)