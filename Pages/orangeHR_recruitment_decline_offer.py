import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecDeclineCandidate():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    offer_declined_button = (By.XPATH, "//button[normalize-space()='Offer Declined']")
    save_decline = (By.XPATH, "//button[normalize-space()='Save']")

    decline_verif = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--subtitle-2']")


    ##Elements##

    def get_offer_declined_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.offer_declined_button))

    def get_save_decline(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_decline))

    def get_decline_verif(self):
        return self.driver.find_element(*self.decline_verif)

    ##Methods##

    def click_offer_declined_button(self):
        self.get_offer_declined_button().click()
        time.sleep(4)

    def click_save_decline(self):
        self.get_save_decline().click()
        time.sleep(6)
        cand_decline_verif = self.get_decline_verif()
        assert cand_decline_verif.text == 'Status: Offer Declined'
        logger.info('Candidate Declined the Offer')
        time.sleep(3)





















