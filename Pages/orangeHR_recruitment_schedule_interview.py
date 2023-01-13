import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecSchedInt():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    sched_button = (By.XPATH, "//button[normalize-space()='Schedule Interview']")
    interview_title = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[6]")
    save_sched_int = (By.XPATH, "//button[normalize-space()='Save']")

    save_sched_verif = (By.XPATH, "//button[normalize-space()='Mark Interview Passed']")

    ##Elements##

    def get_sched_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.sched_button))

    def get_interview_title(self):
        return self.driver.find_element(*self.interview_title)

    def get_save_sched_int(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_sched_int))

    def get_save_sched_verif(self):
        return self.driver.find_element(*self.save_sched_verif)

    ##Methods##

    def click_sched_button(self):
        self.get_sched_button().click()

    def click_interview_title(self, int_title):
        time.sleep(2)
        self.get_interview_title().send_keys(int_title)

    def click_save_sched_int(self):
        self.get_save_sched_int().click()
        time.sleep(6)
        sched_verif = self.get_save_sched_verif()
        assert sched_verif.text == 'Mark Interview Passed'
        logger.info('Scheduled Candidate Success')






















