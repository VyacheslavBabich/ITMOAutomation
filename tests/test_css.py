from pages.text_box import TextBox


def test_text_box_submit(browser):
    text_box = TextBox(browser)
    text_box.visit()

    assert text_box.submit_btn.check_css('color', 'rgba(255, 255, 255, 1')
    assert text_box.submit_btn.check_css('backgroundColor', 'rgba(73, 80, 87, 1')
    assert text_box.submit_btn.check_css('borderColor', 'rgb(0, 123, 255')