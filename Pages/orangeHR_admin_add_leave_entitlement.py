import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class AddLeave():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    add_leave = (By.XPATH, "//a[normalize-space()='Add Entitlements']")
    entitlement_days = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    save_button_for_add_leave = (By.XPATH, "//button[normalize-space()='Save']")
    add_leave_popup = (By.XPATH, "//button[normalize-space()='Confirm']")
    add_leave_verif = (By.XPATH, "//span[normalize-space()='(1) Record Found']")

    ##Elements##

    def get_add_leave(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_leave))

    def get_entitlement_days(self):
        return self.driver.find_element(*self.entitlement_days)

    def get_save_button_for_add_leave(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_button_for_add_leave))

    def get_add_leave_popup(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_leave_popup))

    def get_add_leave_verif(self):
        return self.driver.find_element(*self.add_leave_verif)

    ##Methods##

    def click_get_add_leave(self):
        self.get_add_leave().click()

    def click_entitlement_days(self, days):
        self.get_entitlement_days().send_keys(days)

    def click_save_button_for_add_leave(self):
        self.get_save_button_for_add_leave().click()

    def click_add_leave_popup(self):
        self.get_add_leave_popup().click()
        time.sleep(6)
        add_verif = self.get_add_leave_verif()
        assert add_verif.text == '(1) Record Found'
        logger.info('Add Leave Success')
