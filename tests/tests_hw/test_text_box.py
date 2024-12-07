from pages.text_box import TextBox

def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    name = "Tester"
    text_box_page.name.send_keys(name)
    text_box_page.current_address.send_keys('Adr')
    text_box_page.submit_btn.click_force()
    assert text_box_page.output_elements.check_count_elements(2)
    assert text_box_page.output_name.get_text() == f'Name:{name}'
    assert text_box_page.output_address.get_text() == 'Current Address :Adr'