import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecAddCandidate():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    candidate_button = (By.XPATH, "//a[normalize-space()='Candidates']")
    email_box = (By.XPATH, "(//input[@placeholder='Type here'])[1]")
    contact_box = (By.XPATH, "(//input[@placeholder='Type here'])[2]")
    upload_resume = (By.XPATH, "//div[@class='oxd-file-input-div']")
    keyword_box = (By.XPATH, "//input[@placeholder='Enter comma seperated words...']")
    notes_box = (By.XPATH, "(//textarea[@placeholder='Type here'])[1]")
    check_box = (By.XPATH, "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']")
    save_button_add_candidate = (By.XPATH, "//button[normalize-space()='Save']")
    add_candidate_verif = (By.XPATH, "//button[normalize-space()='Shortlist']")

    drp_vacancy = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
    page_down = (By.XPATH, "//html")

    ##Elements##

    def get_candidate_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.candidate_button))

    def get_email_box(self):
        return self.driver.find_element(*self.email_box)

    def get_contact_box(self):
        return self.driver.find_element(*self.contact_box)

    def get_upload_resume(self):
        return self.driver.find_element(*self.upload_resume)

    def get_keyword_box(self):
        return self.driver.find_element(*self.keyword_box)

    def get_notes_box(self):
        return self.driver.find_element(*self.notes_box)

    def get_check_box(self):
        return self.wait.until(EC.element_to_be_clickable(self.check_box))

    def get_save_button_add_candidate(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_button_add_candidate))

    def get_add_candidate_verif(self):
        return self.driver.find_element(*self.add_candidate_verif)

    def get_drp_vacancy(self):
        return self.wait.until(EC.element_to_be_clickable(self.drp_vacancy))

    def get_page_down(self):
        return self.driver.find_element(*self.page_down)

    ##Methods##

    def click_candidate_button(self):
        self.get_candidate_button().click()

    def click_email_box(self, email_box):
        self.get_email_box().send_keys(email_box)

    def click_contact_box(self, contact_box):
        self.get_contact_box().send_keys(contact_box)

    def click_upload_resume(self, upload):
        self.get_upload_resume().send_keys(upload)

    def click_keyword_box(self, keyword):
        self.get_keyword_box().send_keys(keyword)

    def click_notes_box(self, notes):
        self.get_notes_box().send_keys(notes)

    def click_check_box(self):
        self.get_check_box().click()

    def click_save_button_add_candidate(self):
        self.get_save_button_add_candidate().click()
        time.sleep(6)
        hire_candidate_verif = self.get_add_candidate_verif()
        assert hire_candidate_verif.text == 'Shortlist'
        logger.info('Add Candidate Success')

    def click_drp_vacancy(self):
        self.get_drp_vacancy().click()

    def click_page_down(self):
        self.get_page_down().send_keys(Keys.PAGE_DOWN*4)




















