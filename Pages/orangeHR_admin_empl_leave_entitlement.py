import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()

class EmplLeaveEntitlement():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    employee_entitlements = (By.XPATH, "//a[normalize-space()='Employee Entitlements']")
    search_button_for_empl_entitlement = (By.XPATH, "//button[normalize-space()='Search']")
    empl_entitlements_verif = (By.XPATH, "//span[normalize-space()='Total 15.00 Day(s)']")

    ##Elements##

    def get_employee_entitlements(self):
        return self.wait.until(EC.element_to_be_clickable(self.employee_entitlements))

    def get_search_button_for_empl_entitlement(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_button_for_empl_entitlement))

    def get_empl_entitlements_verif(self):
        return self.driver.find_element(*self.empl_entitlements_verif)

    ##Methods##

    def click_employee_entitlements(self):
        self.get_employee_entitlements().click()

    def click_get_search_button_for_empl_entitlement(self):
        self.get_search_button_for_empl_entitlement().click()
        time.sleep(4)
        empl_entitl_verif = self.get_empl_entitlements_verif()
        assert empl_entitl_verif.text == 'Total 15.00 Day(s)'
        logger.info('Success Check of Employee Entitlement')











