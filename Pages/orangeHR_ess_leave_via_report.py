import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()

class LeaveESSViaReport():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    reports_button = (By.XPATH, "//span[normalize-space()='Reports']//i[@class='oxd-icon bi-chevron-down']")
    usage_reports = (By.XPATH, "//a[normalize-space()='My Leave Entitlements and Usage Report']")
    generate_report_button = (By.XPATH, "//button[normalize-space()='Generate']")
    report_verify = (By.XPATH, "//div[@class='col-alt rgCell'][normalize-space()='14.00']")

    report_verify_ess = (By.XPATH, "//div[@class='col-alt rgCell'][normalize-space()='13.00']")

    ##Elements##

    def get_reports_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.reports_button))

    def get_usage_reports(self):
        return self.wait.until(EC.element_to_be_clickable(self.usage_reports))

    def get_generate_report_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.generate_report_button))

    def get_report_verify(self):
        return self.driver.find_elements(*self.report_verify)

    def get_report_verify_ess(self):
        return self.driver.find_elements(*self.report_verify_ess)

    ##Methods##

    def click_reports_button(self):
        self.get_reports_button().click()

    def click_usage_reports(self):
        self.get_usage_reports().click()

    def click_generate_reports_button(self):
        time.sleep(2)
        self.get_generate_report_button().click()
        time.sleep(3)
        report_verify = self.get_report_verify()
        for leave_bal in report_verify:
            assert leave_bal.text == '14.00'
            logger.info('Success Check Leave Balance via Report')

    def click_generate_reports_button_ess(self):
        self.get_generate_report_button().click()
        time.sleep(4)
        report_verify = self.get_report_verify()
        for leave_bal in report_verify:
            assert leave_bal.text == '14.00'
            logger.info('Success ESS Check Leave Balance via Report')
