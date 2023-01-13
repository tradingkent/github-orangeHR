import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecPassCandidate():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    cand_pass_button = (By.XPATH, "//button[normalize-space()='Mark Interview Passed']")
    save_cand_pass = (By.XPATH, "//button[normalize-space()='Save']")

    cand_pass_verif = (By.XPATH, "//button[normalize-space()='Offer Job']")

    ##Elements##

    def get_cand_pass_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.cand_pass_button))

    def get_save_cand_pass(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_cand_pass))

    def get_cand_pass_verif(self):
        return self.driver.find_element(*self.cand_pass_verif)

    ##Methods##

    def click_cand_pass_button(self):
        self.get_cand_pass_button().click()

    def click_save_cand_pass(self):
        self.get_save_cand_pass().click()
        time.sleep(6)
        cand_pass_verif = self.get_cand_pass_verif()
        assert cand_pass_verif.text == 'Offer Job'
        logger.info('Candidate Pass')





















