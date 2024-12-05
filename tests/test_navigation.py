from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    demoq_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demoq_qa_page.visit()
    demoq_qa_page.btn_elements.click()

    demoq_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert elements_page.equal_url()