import time
from pages.alerts import Alerts


def test_check_alert(browser):

    al_page = Alerts(browser)
    al_page.visit()
    al_page.timer_alert.click()
    time.sleep(5)

    assert al_page.alert()