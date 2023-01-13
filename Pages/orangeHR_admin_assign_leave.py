import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class AdminLeaveAccess():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    assign_leave_button = (By.XPATH, "//a[normalize-space()='Assign Leave']")
    assign_button = (By.XPATH, "//button[normalize-space()='Assign']")

    ##Elements##

    def get_assign_leave_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.assign_leave_button))

    def get_assign_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.assign_button))

    ##Methods##

    def click_assign_leave_button(self):
        self.get_assign_leave_button().click()

    def click_assign_button(self):
        self.get_assign_button().click()
        time.sleep(4)
        assign_leave_verif = self.get_assign_button()
        assert assign_leave_verif.text == 'Assign'
        logger.info('Assign Success')
