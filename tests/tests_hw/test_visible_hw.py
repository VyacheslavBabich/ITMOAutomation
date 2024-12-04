from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    demo_page = Accordion(browser)
    demo_page.visit()
    assert demo_page.section1_content.visible()
    demo_page.section1_heading.click()
    time.sleep(2)
    assert not demo_page.section1_content.visible()

def test_visible_accordion_default(browser):
    demo_page_next = Accordion(browser)
    demo_page_next.visit()
    assert not demo_page_next.section2_content1.visible()
    assert not demo_page_next.section2_content2.visible()
    assert not demo_page_next.section3_content.visible()