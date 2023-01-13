import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecSearchCandidate():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    select_candidate_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    candidate_name = (By.XPATH, "//div/span[text()='Euron  Greyjoy']")
    search_for_candidate = (By.XPATH, "//button[normalize-space()='Search']")

    search_cand_verif = (By.XPATH, "//span[normalize-space()='(1) Record Found']")

    ##Elements##

    def get_select_candidate_name(self):
        return self.driver.find_element(*self.select_candidate_name)

    def get_candidate_name(self):
        return self.wait.until(EC.element_to_be_clickable(self.candidate_name))

    def get_search_for_candidate(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_for_candidate))

    def get_search_cand_verif(self):
        return self.driver.find_element(*self.search_cand_verif)

    ##Methods##

    def click_select_candidate_name(self, cand_name):
        time.sleep(2)
        self.get_select_candidate_name().send_keys(cand_name)

    def click_candidate_name(self):
        self.get_candidate_name().click()

    def click_search_for_candidate(self):
        self.get_search_for_candidate().click()
        time.sleep(3)
        search_cand_verif = self.get_search_cand_verif()
        assert search_cand_verif.text == '(1) Record Found'
        logger.info('Search Candidate Successful')





















