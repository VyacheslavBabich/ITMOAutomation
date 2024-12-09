import time
import pytest
from pages.tables import Tables

def test_sort(browser):
    web_t = Tables(browser)
    web_t.visit()

    web_t.first_name_column.click()
    time.sleep(2)

    assert web_t.first_name_column.get_dom_attribute('class') == 'rt-resizable-header-content'
    time.sleep(2)

    web_t.first_name_column.click()
    time.sleep(2)

    assert web_t.first_name_column.get_dom_attribute('class') == 'rt-resizable-header-content'
    time.sleep(2)

    web_t.last_name_column.click()
    time.sleep(2)

    assert web_t.last_name_column.get_dom_attribute('class') == 'rt-resizable-header-content'
    time.sleep(2)

    web_t.last_name_column.click()
    time.sleep(2)

    assert web_t.last_name_column.get_dom_attribute('class') == 'rt-resizable-header-content'