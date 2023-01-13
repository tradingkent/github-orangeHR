import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.orangeHR_ess_leave_entitlement import LeaveESSEntitlement
from Utilities.common import LogFunc
from Utilities.data import leave_balance_applied

lg = LogFunc()
logger = lg.get_log()

class AddEmplPIM():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    pim_button = (By.XPATH, "//span[normalize-space()='PIM']")
    add_button_pim = (By. XPATH, "//button[normalize-space()='Add']")
    first_name = (By.XPATH, "//input[@placeholder='First Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    save_button_pim = (By. XPATH, "//button[normalize-space()='Save']")
    add_empl_pim_verif = (By.XPATH, "//a[normalize-space()='Personal Details']")

    toggle_button = (By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    username_box = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")

    ##Elements##

    def get_pim_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.pim_button))

    def get_add_button_pim(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_button_pim))

    def get_first_name(self):
        return self.driver.find_element(*self.first_name)

    def get_last_name(self):
        return self.driver.find_element(*self.last_name)

    def get_save_button_pim(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_button_pim))

    def get_add_empl_pim_verif(self):
        return self.driver.find_element(*self.add_empl_pim_verif)

    def get_username_box(self):
        return self.driver.find_element(*self.username_box)

    def get_toggle_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.toggle_button))

    ##Methods##

    def click_pim_button(self):
        self.get_pim_button().click()

    def click_add_button_pim(self):
        self.get_add_button_pim().click()

    def click_entername(self, fname, lname):
        time.sleep(2)
        self.get_first_name().send_keys(fname)
        self.get_last_name().send_keys(lname)

    def click_save_button_pim(self):
        self.get_save_button_pim().click()
        time.sleep(7)
        empl_pim_verif = self.get_add_empl_pim_verif()
        assert empl_pim_verif.text == 'Personal Details'
        logger.info('Success Adding Employee without login details')

    def click_username_box(self, uname):
        self.get_username_box().send_keys(uname)

    def click_toggle_button(self):
        self.get_toggle_button().click()
















