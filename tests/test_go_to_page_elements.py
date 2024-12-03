from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_go_to_page_elements(browser):
    demoqa_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demoqa_qa_page.visit()
    assert demoqa_qa_page.equal_url()
    demoqa_qa_page.btn_elements.click()
    assert elements_page.equal_url()