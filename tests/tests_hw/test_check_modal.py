import time
import pytest
from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    modal = ModalDialogs(browser)
    modal.visit()

    modal.small.click()
    time.sleep(2)
    modal.close_small.click()
    time.sleep(2)

    modal.large.click()
    time.sleep(2)
    modal.close_large.click()
    time.sleep(2)