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

class UpdateEmplPIM():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    first_name = (By.XPATH, "//input[@placeholder='First Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")

    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    non_existing_verif = (By.XPATH, "//span[normalize-space()='No Records Found']")

    emp_name_pim_edit = (By.XPATH, "//div/span[text()='Night  King']")
    emp_name_pim_after_edit = (By.XPATH, "//div/span[text()='White  Walker']")
    search_edit_verif = (By.XPATH, "//span[normalize-space()='(1) Record Found']")

    save_button_edit_one = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]")

    ##Elements##

    def get_search_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_button))

    def get_non_existing_verif(self):
        return self.driver.find_element(*self.non_existing_verif)

    def get_emp_name_pim_edit(self):
        return self.wait.until(EC.element_to_be_clickable(self.emp_name_pim_edit))

    def get_emp_name_pim_after_edit(self):
        return self.wait.until(EC.element_to_be_clickable(self.emp_name_pim_after_edit))

    def get_search_edit_verif(self):
        return self.driver.find_element(*self.search_edit_verif)

    def get_first_name(self):
        return self.driver.find_element(*self.first_name)

    def get_last_name(self):
        return self.driver.find_element(*self.last_name)

    def get_save_button_edit_one(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_button_edit_one))

    ##Methods##

    def click_search_button_non_existing(self):
        self.get_search_button().click()
        time.sleep(4)
        non_existing_verify = self.get_non_existing_verif()
        assert non_existing_verify.text == 'No Records Found'
        logger.info('Search of Non Existing Employee Success')

    def click_emp_name_pim_edit(self):
        self.get_emp_name_pim_edit().click()
        time.sleep(4)

    def click_emp_name_pim_after_edit(self):
        self.get_emp_name_pim_after_edit().click()

    def click_search_button_for_edit(self):
        self.get_search_button().click()

    def click_search_button_after_edit(self):
        self.get_search_button().click()
        time.sleep(4)
        search_after_edit = self.get_search_edit_verif()
        assert search_after_edit.text == '(1) Record Found'
        logger.info('PIM Edit Success')

    def click_entername_for_edit(self, fname, lname):
        time.sleep(4)
        self.get_first_name().send_keys(Keys.BACKSPACE*10)
        self.get_first_name().send_keys(fname)
        self.get_last_name().send_keys(Keys.BACKSPACE*10)
        self.get_last_name().send_keys(lname)
        #time.sleep(4)

    def click_save_button_edit_one(self):
        self.get_save_button_edit_one().click()
        time.sleep(4)

















