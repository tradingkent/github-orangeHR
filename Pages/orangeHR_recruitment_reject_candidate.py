import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecRejCandidate():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    reject_button = (By.XPATH, "//button[normalize-space()='Reject']")
    save_reject = (By.XPATH, "//button[normalize-space()='Save']")
    reject_verif = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--subtitle-2']")

    ##Elements##

    def get_reject_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.reject_button))

    def get_save_reject(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_reject))

    def get_reject_verif(self):
        return self.driver.find_element(*self.reject_verif)

    ##Methods##

    def click_reject_button(self):
        self.get_reject_button().click()
        time.sleep(4)

    def click_save_reject(self):
        self.get_save_reject().click()
        time.sleep(6)
        cand_reject_verif = self.get_reject_verif()
        assert cand_reject_verif.text == 'Status: Rejected'
        logger.info('Candidate Rejected')
        time.sleep(3)





















