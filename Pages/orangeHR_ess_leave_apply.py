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


class LeaveESSApply():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    apply_button = (By.XPATH, "//a[normalize-space()='Apply']")
    from_date = (By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")
    to_date = (By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")

    drp_duration = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
    halfday_morning = (By.XPATH, "//div/span[text()='Half Day - Morning']")
    halfday_afternoon = (By.XPATH, "//div/span[text()='Half Day - Afternoon']")
    specify_time = (By.XPATH, "//div/span[text()='Specify Time']")

    specify_time_clock_one = (By.XPATH, "(//i[@class='oxd-icon bi-clock oxd-time-input--clock'])[1]")
    specify_time_hhmm_one = (By.XPATH, "(// input[@ placeholder='hh:mm'])[1]")
    specify_time_clock_two = (By.XPATH, "(//i[@class='oxd-icon bi-clock oxd-time-input--clock'])[2]")
    specify_time_hhmm_two = (By.XPATH, "(// input[@ placeholder='hh:mm'])[2]")

    apply_leave = (By.XPATH, "//button[normalize-space()='Apply']")
    leave_balance = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-leave-balance-text']")

    ##Elements##

    def get_apply_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.apply_button))

    def get_from_date(self):
        return self.driver.find_element(*self.from_date)

    def get_to_date(self):
        return self.driver.find_element(*self.to_date)

    def get_drp_duration(self):
        return self.wait.until(EC.element_to_be_clickable(self.drp_duration))

    def get_halfday_morning(self):
        return self.wait.until(EC.element_to_be_clickable(self.halfday_morning))

    def get_halfday_afternoon(self):
        return self.wait.until(EC.element_to_be_clickable(self.halfday_afternoon))

    def get_specify_time(self):
        return self.wait.until(EC.element_to_be_clickable(self.specify_time))

    def get_specify_time_clock_one(self):
        return self.wait.until(EC.element_to_be_clickable(self.specify_time_clock_one))

    def get_specify_time_clock_two(self):
        return self.wait.until(EC.element_to_be_clickable(self.specify_time_clock_two))

    def get_specify_time_hhmm_one(self):
        return self.driver.find_element(*self.specify_time_hhmm_one)

    def get_specify_time_hhmm_two(self):
        return self.driver.find_element(*self.specify_time_hhmm_two)

    def get_apply_leave(self):
        return self.driver.find_element(*self.apply_leave)

    def get_leave_balance(self):
        return self.driver.find_element(*self.leave_balance)

    ##Methods##

    def click_apply_button(self):
        self.get_apply_button().click()

    def click_from_date(self, fromdate):
        self.get_from_date().send_keys(fromdate)

    def click_to_date(self, todate):
        time.sleep(2)
        self.get_to_date().click()
        self.get_to_date().send_keys(Keys.BACKSPACE * 10)
        self.get_to_date().send_keys(todate)

    def click_drp_duration(self):
        self.get_drp_duration().click()

    def click_halfday_morning(self):
        self.get_halfday_morning().click()

    def click_halfday_afternoon(self):
        self.get_halfday_afternoon().click()

    def click_specify_time(self):
        self.get_specify_time().click()

    def click_specify_time_clock_one(self):
        self.get_specify_time_clock_one().click()

    def click_specify_time_clock_two(self):
        self.get_specify_time_clock_two().click()

    def click_specify_time_hhmm_one(self, start_time):
        self.get_specify_time_hhmm_one().send_keys(Keys.BACKSPACE * 10)
        self.get_specify_time_hhmm_one().send_keys(start_time)

    def click_specify_time_hhmm_two(self, end_time):
        self.get_specify_time_hhmm_two().send_keys(Keys.BACKSPACE * 10)
        self.get_specify_time_hhmm_two().send_keys(end_time)

    def click_apply_leave_for_fullday(self):

        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        self.get_apply_leave().click()
        time.sleep(2)
        self.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        time.sleep(4)
        leave_balance = self.get_leave_balance()
        assert leave_balance.text == leave_balance_applied.get('fullday')
        logger.info('Leave Fullday Success')

    def click_apply_leave_for_halfday_morning(self):

        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        self.get_apply_leave().click()
        time.sleep(2)
        self.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        time.sleep(4)
        leave_balance = self.get_leave_balance()
        assert leave_balance.text == leave_balance_applied.get('halfday_morning')
        logger.info('Leave Halfday Morning Success')

    def click_apply_leave_for_halfday_afternoon(self):

        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        self.get_apply_leave().click()
        time.sleep(2)
        self.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        time.sleep(4)
        leave_balance = self.get_leave_balance()
        assert leave_balance.text == leave_balance_applied.get('halfday_afternoon')
        logger.info('Leave Halfday Afternoon Success')

    def click_apply_leave_for_specify_time(self):

        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        self.get_apply_leave().click()
        time.sleep(2)
        self.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        time.sleep(4)
        leave_balance = self.get_leave_balance()
        assert leave_balance.text == leave_balance_applied.get('specify_time')
        logger.info('Leave Specify Time Success')

    def click_apply_leave_for_specify_time_ess(self):

        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        self.get_apply_leave().click()
        time.sleep(2)
        self.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        time.sleep(4)
        leave_balance = self.get_leave_balance()
        assert leave_balance.text == leave_balance_applied.get('specify_time')
        logger.info('Leave Specify Time Success')

    def click_apply_leave_for_specify_time_again(self):
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        self.get_apply_leave().click()
        time.sleep(2)
        self.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        time.sleep(4)
        leave_balance = self.get_leave_balance()
        assert leave_balance.text == leave_balance_applied.get('specify_ag_time')
        logger.info('Leave Specify Time Success')


