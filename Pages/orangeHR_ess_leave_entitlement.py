import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc
from Utilities.data import validation_login, leave_entitlement_verif

lg = LogFunc()
logger = lg.get_log()

class LeaveESSEntitlement():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    ess_verif = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    ess_login_button = (By.XPATH, "//button[normalize-space()='Login']")
    leave_button = (By.XPATH, "//span[normalize-space()='Leave']")
    entitlements_button = (By.XPATH, "//span[normalize-space()='Entitlements']")
    my_entitlements_button = (By.XPATH, "//a[normalize-space()='My Entitlements']")
    drp_leave_type = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
    leave_type_bereavement = (By.XPATH, "//div/span[text()='CAN - Bereavement']")
    leave_type_personal = (By.XPATH, "//div/span[text()='US - Personal']")
    leave_type_vacation = (By.XPATH, "//div/span[text()='US - Vacation']")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")

    ##Elements##

    def get_login_button_ess(self):
        return self.driver.find_element(*self.ess_login_button)

    def get_ess_verif(self):
        return self.driver.find_element(*self.ess_verif)

    def get_leave_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.leave_button))

    def get_entitlements_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.entitlements_button))

    def get_my_entitlements_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.my_entitlements_button))

    def get_drp_leave_type(self):
        return self.wait.until(EC.element_to_be_clickable(self.drp_leave_type))

    def get_leave_type_bereavement(self):
        return self.wait.until(EC.element_to_be_clickable(self.leave_type_bereavement))

    def get_search_button(self):
        return self.driver.find_element(*self.search_button)


    ##Methods##

    def click_button_ess(self):
        self.get_login_button_ess().click()
        time.sleep(3)
        ess_login_verify = self.get_ess_verif()
        assert ess_login_verify.text == validation_login.get('ESS_Verif')
        logger.info('Success')

    def click_leave_button(self):
        self.get_leave_button().click()

    def click_entitlements_button(self):
        self.get_entitlements_button().click()

    def click_my_entitlements_button(self):
        self.get_my_entitlements_button().click()

    def click_drp_leave_type(self):
        self.get_drp_leave_type().click()

    def click_leave_type_bereavement(self):
        self.get_leave_type_bereavement().click()

