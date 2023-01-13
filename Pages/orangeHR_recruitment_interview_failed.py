import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecFailCandidate():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    cand_fail_button = (By.XPATH, "//button[normalize-space()='Mark Interview Failed']")
    save_cand_fail = (By.XPATH, "//button[normalize-space()='Save']")
    cand_fail_verif = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--subtitle-2']")

    ##Elements##

    def get_cand_fail_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.cand_fail_button))

    def get_save_cand_fail(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_cand_fail))

    def get_cand_fail_verif(self):
        return self.driver.find_element(*self.cand_fail_verif)

    ##Methods##

    def click_cand_fail_button(self):
        self.get_cand_fail_button().click()
        time.sleep(4)

    def click_save_cand_fail(self):
        self.get_save_cand_fail().click()
        time.sleep(6)
        cand_fail_verif = self.get_cand_fail_verif()
        assert cand_fail_verif.text == 'Status: Interview Failed'
        logger.info('Candidate Failed')
        time.sleep(3)





















