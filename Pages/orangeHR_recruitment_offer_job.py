import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecOfferCandidate():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    offer_job_button = (By.XPATH, "//button[normalize-space()='Offer Job']")
    save_button_offer_job = (By.XPATH, "//button[normalize-space()='Save']")
    offer_job_verif = (By.XPATH, "//button[normalize-space()='Hire']")

    ##Elements##

    def get_offer_job_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.offer_job_button))

    def get_save_button_offer_job(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_button_offer_job))

    def get_offer_job_verif(self):
        return self.driver.find_element(*self.offer_job_verif)

    ##Methods##

    def click_offer_job_button(self):
        self.get_offer_job_button().click()

    def click_save_button_offer_job(self):
        self.get_save_button_offer_job().click()
        time.sleep(6)
        offer_job_verif = self.get_offer_job_verif()
        assert offer_job_verif.text == 'Hire'
        logger.info('Candidate Offer Job Success')






















