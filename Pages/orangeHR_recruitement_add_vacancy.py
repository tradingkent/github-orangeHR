import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc

lg = LogFunc()
logger = lg.get_log()


class RecAddVacancy():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    recruitment_button = (By.XPATH, "//span[normalize-space()='Recruitment']")
    vacancies_button = (By.XPATH, "//a[normalize-space()='Vacancies']")
    add_button_rec = (By.XPATH, "//button[normalize-space()='Add']")
    vacancy_name_box = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    job_title_drp = (By. XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
    job_option = (By.XPATH, "//div/span[text()='Software Engineer']")
    description_box = (By.XPATH, "//textarea[@placeholder='Type description here']")
    number_pos_box = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
    save_button_vacancies = (By.XPATH, "//button[normalize-space()='Save']")
    search_button_vacancy = (By.XPATH, "//button[normalize-space()='Search']")

    vacancy_enter = (By.XPATH, "//div/span[text()='AT']")
    vacancy_verif = (By.XPATH, "//span[normalize-space()='(1) Record Found']")

    ##Elements##

    def get_recruitment_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.recruitment_button))

    def get_vacancies_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.vacancies_button))

    def get_add_button_rec(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_button_rec))

    def get_vacancy_name_box(self):
        return self.driver.find_element(*self.vacancy_name_box)

    def get_job_title_drp(self):
        return self.wait.until(EC.element_to_be_clickable(self.job_title_drp))

    def get_job_option(self):
        return self.wait.until(EC.element_to_be_clickable(self.job_option))

    def get_description_box(self):
        return self.driver.find_element(*self.description_box)

    def get_number_pos_box(self):
        return self.driver.find_element(*self.number_pos_box)

    def get_save_button_vacancies(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_button_vacancies))

    def get_search_button_vacancy(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_button_vacancy))

    def get_vacancy_enter(self):
        return self.wait.until(EC.element_to_be_clickable(self.vacancy_enter))

    def get_vacancy_verif(self):
        return self.driver.find_element(*self.vacancy_verif)

    ##Methods##

    def click_recruitment_button(self):
        self.get_recruitment_button().click()

    def click_vacancies_button(self):
        self.get_vacancies_button().click()

    def click_add_button_rec(self):
        self.get_add_button_rec().click()

    def click_vacancy_name_box(self, vacancy):
        time.sleep(2)
        self.get_vacancy_name_box().send_keys(vacancy)

    def click_job_title_drp(self):
        self.get_job_title_drp().click()

    def click_job_option(self):
        self.get_job_option().click()

    def click_description_box(self, desc_box):
        self.get_description_box().send_keys(desc_box)

    def click_number_pos_box(self, pos_box):
        self.get_number_pos_box().send_keys(pos_box)

    def click_save_button_vacancies(self):
        self.get_save_button_vacancies().click()
        time.sleep(2)

    def click_vacancy_enter(self):
        self.get_vacancy_enter().click()

    def click_search_button_vacancy(self):
        self.get_search_button_vacancy().click()
        time.sleep(3)
        vac_verif = self.get_vacancy_verif()
        assert vac_verif.text == '(1) Record Found'
        logger.info('Success Vacancy Addition')
















