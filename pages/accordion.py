from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.section1_content = WebElement(driver, locator='#section1Content > p')
        self.section1_heading = WebElement(driver, locator='#section1Heading')
        self.section2_content1= WebElement(driver, locator='#section2Content > p:nth-child(1)')
        self.section2_content2 = WebElement(driver, locator='#section2Content > p:nth-child(2)')
        self.section3_content= WebElement(driver, locator='#section3Content > p')