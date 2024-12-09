from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btns_locator = WebElement(driver, ' div:nth-child(3) > div > ul > li')
        self.btn_icon = WebElement(driver, '#app > header > a')

        self.small = WebElement(driver, '#showSmallModal')
        self.large = WebElement(driver, '#showLargeModal')
        self.close_small = WebElement(driver, '#closeSmallModal')
        self.close_large = WebElement(driver, '#closeLargeModal')