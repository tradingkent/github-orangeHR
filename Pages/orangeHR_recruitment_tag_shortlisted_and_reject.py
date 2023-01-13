import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecShortlistCandidate():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    eye_button = (By.XPATH, "//i[@class='oxd-icon bi-eye-fill']")
    shortlist_button = (By.XPATH, "//button[normalize-space()='Shortlist']")
    shortlist_note = (By.XPATH, "//textarea[@placeholder='Type here']")
    save_shortlist = (By.XPATH, "//button[normalize-space()='Save']")
    shortlist_verif = (By.XPATH, "//button[normalize-space()='Schedule Interview']")

    reject_button = (By.XPATH, "//button[normalize-space()='Reject']")

    ##Elements##

    def get_eye_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.eye_button))

    def get_shortlist_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.shortlist_button))

    def get_shortlist_note(self):
        return self.driver.find_element(*self.shortlist_note)

    def get_save_shortlist(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_shortlist))

    def get_shortlist_verif(self):
        return self.driver.find_element(*self.shortlist_verif)

    def get_reject_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.reject_button))

    ##Methods##

    def click_eye_button(self):
        self.get_eye_button().click()

    def click_shortlist_button(self):
        self.get_shortlist_button().click()

    def click_shortlist_note(self, sh_note):
        time.sleep(2)
        self.get_shortlist_note().send_keys(sh_note)

    def click_save_shortlist(self):
        self.get_save_shortlist().click()
        time.sleep(8)
        sh_verif = self.get_shortlist_verif()
        assert sh_verif.text == 'Schedule Interview'
        logger.info('Shorlist Success')

    def click_reject_button(self):
        self.get_reject_button().click()
