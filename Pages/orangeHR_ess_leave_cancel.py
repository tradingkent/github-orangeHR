import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.orangeHR_ess_leave_entitlement import LeaveESSEntitlement
from Pages.orangeHR_ess_leave_apply import LeaveESSApply
from Utilities.common import LogFunc
from Utilities.data import leave_balance_applied

lg = LogFunc()
logger = lg.get_log()


class LeaveESSCancel():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    cancel_leave_one = (By.XPATH, "(//button[@type='button'][normalize-space()='Cancel'])[1]")
    my_leave_button = (By.XPATH, "//a[normalize-space()='My Leave']")

    leave_balance = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-leave-balance-text']")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    page = (By.XPATH, "(//html)[1]")

    ##Elements##

    def get_cancel_leave_one(self):
        return self.driver.find_element(*self.cancel_leave_one)

    def get_page_end(self):
        return self.driver.find_element(*self.page)

    def get_my_leave_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.my_leave_button))

    def get_search_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_button))

    def get_leave_balance(self):
        return self.driver.find_element(*self.leave_balance)

    ##Methods##

    def click_my_leave_button(self):
        self.get_my_leave_button().click()

    def click_search_button(self):
        self.get_search_button().click()

    def scroll_page_end(self):
        self.get_page_end().send_keys(Keys.PAGE_DOWN * 5)

    def click_cancel_button(self):
        time.sleep(2)
        self.get_cancel_leave_one().click()

    def cancel_verify(self):

        leave_ess_apply = LeaveESSApply(self.driver, self.wait)
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        time.sleep(2)
        leave_ess_apply.get_apply_button().click()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        time.sleep(4)
        leave_balance = self.get_leave_balance()
        assert leave_balance.text == leave_balance_applied.get('cancel_leave')
        logger.info('Cancel Leave Success')


    def cancel_verify_ess(self):

        leave_ess_apply = LeaveESSApply(self.driver, self.wait)
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        time.sleep(2)
        leave_ess_apply.get_apply_button().click()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        time.sleep(4)
        leave_balance = self.get_leave_balance()
        assert leave_balance.text == leave_balance_applied.get('cancel_leave_ess')
        logger.info('Cancel Leave Success')

