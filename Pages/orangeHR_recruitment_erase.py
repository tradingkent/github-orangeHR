import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.orangeHR_ess_leave_entitlement import LeaveESSEntitlement
from Utilities.data import leave_balance_applied


class RecDelCandidate():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    delete_button = (By.XPATH, "//i[@class='oxd-icon bi-trash']")
    confirm_delete = (By.XPATH, "//button[normalize-space()='Yes, Delete']")

    ##Elements##

    def get_delete_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.delete_button))

    def get_confirm_delete(self):
        return self.wait.until(EC.element_to_be_clickable(self.confirm_delete))

    ##Methods##

    def click_delete_button(self):
        self.get_delete_button().click()

    def click_confirm_delete(self):
        self.get_confirm_delete().click()





















