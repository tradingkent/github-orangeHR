import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecHireCandidate():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    hire_button = (By.XPATH, "//button[normalize-space()='Hire']")
    save_button_hire = (By.XPATH, "//button[normalize-space()='Save']")
    hire_verif = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--subtitle-2']")

    ##Elements##

    def get_hire_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.hire_button))

    def get_save_button_hire(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_button_hire))

    def get_hire_verif(self):
        return self.driver.find_element(*self.hire_verif)

    ##Methods##

    def click_hire_button(self):
        self.get_hire_button().click()

    def click_save_button_hire(self):
        self.get_save_button_hire().click()
        time.sleep(5)
        hire_verif = self.get_hire_verif()
        assert hire_verif.text == 'Status: Hired'
        logger.info('Hire Success')






















