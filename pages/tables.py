from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.btn_delete_row = WebElement(driver, "//*[contains(text(), 'delete']", 'xpath')

        self.first_record_delete = WebElement(driver, '//*[contains(@id, "delete")]', 'xpath')
        self.no_rows = WebElement(driver, 'div.rt-noData')
        self.add_row = WebElement(driver, '#addNewRecordButton')
        self.window_add = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.bth_add = WebElement(driver, '#submit')
        self.modal_first_name = WebElement(driver, '#firstName')
        self.modal_last_name = WebElement(driver, '#lastName')
        self.modal_email = WebElement(driver, '#userEmail')
        self.modal_age = WebElement(driver, '#age')
        self.modal_salary = WebElement(driver, '#salary')
        self.modal_dep = WebElement(driver, '#department')
        self.fn_row = WebElement(driver,'#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.edit1 = WebElement(driver, '#edit-record-4')
        self.delete1 = WebElement(driver, '#delete-record-4')
