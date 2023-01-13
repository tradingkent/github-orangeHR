import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utilities.data import validation_login
from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    ##Locators##

    username = (By.XPATH, "//input[@placeholder='Username']")
    password = (By.XPATH, "//input[@placeholder='Password']")
    login_button = (By.XPATH, "//button[normalize-space()='Login']")
    admin_verify = (By.XPATH, "//li[1]//a[1]//span[1]")
    invalid_credentials = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    blank_credentials = (By.XPATH, "//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]")
    account_disabled = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    ##Elements##

    def get_username(self):
        return self.driver.find_element(*self.username)

    def get_password(self):
        return self.driver.find_element(*self.password)

    def get_login_button(self):
        return self.driver.find_element(*self.login_button)

    def get_admin_verify(self):
        return self.driver.find_element(*self.admin_verify)

    def get_invalid_user_verify(self):
        return self.driver.find_element(*self.invalid_credentials)

    def get_invalid_blank_verify(self):
        return self.driver.find_element(*self.blank_credentials)

    def get_account_disabled(self):
        return self.driver.find_element(*self.account_disabled)

    ##Methods##

    def user_entry(self, user, passw):
        time.sleep(2)
        self.get_username().send_keys(user)
        self.get_password().send_keys(passw)

        logger.info('Username: ' + user)
        logger.info('Password: ' + passw)

    def click_button(self):
        self.get_login_button().click()
        time.sleep(3)
        login_verify = self.get_admin_verify()
        assert login_verify.text == validation_login.get('Verif')
        logger.info('Success')

    def click_button_invalid_user(self):
        self.get_login_button().click()
        time.sleep(3)
        invalid_user_verify = self.get_invalid_user_verify()
        assert invalid_user_verify.text == validation_login.get('Invalid')
        logger.info('Invalid credentials')

    def click_button_blank(self):
        self.get_login_button().click()
        time.sleep(3)
        invalid_blank_verify = self.get_invalid_blank_verify()
        assert invalid_blank_verify.text == validation_login.get('Blank')
        logger.info('Blank credentials')

    def click_button_account_disabled(self):
        self.get_login_button().click()
        time.sleep(3)
        account_disabled_verify = self.get_account_disabled()
        assert account_disabled_verify.text == validation_login.get('Acc Disabled')
        logger.info('Account Disabled')
