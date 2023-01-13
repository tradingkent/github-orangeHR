import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.orangeHR_ess_leave_entitlement import LeaveESSEntitlement
from Utilities.data import leave_balance_applied


class AdminLeaveAccess():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    view_detail = (By.XPATH, "//p[normalize-space()='View Leave Details']")
    record_found = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")
    leave_details_verif = (By.XPATH, "//h6[normalize-space()='Leave Request Details']")

    ##Elements##

    def get_view_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.view_detail))

    def get_leave_details_verif(self):
        return self.driver.find_element(*self.leave_details_verif)

    ##Methods##

    def click_apply_button(self):
        self.get_apply_button().click()






