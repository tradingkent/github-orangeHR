import time
import logging

from Utilities.common import LogFunc

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

lg = LogFunc()
logger = lg.get_log()

class SortUsernameESS():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    sort_button = (By.XPATH, "(//i[@class='oxd-icon bi-sort-alpha-down oxd-icon-button__icon "
                             "oxd-table-header-sort-icon'])[1]")
    ascending_button = (By.XPATH, "(//span[@class='oxd-text oxd-text--span'][normalize-space()='Ascending'])[1]")
    descending_button = (By.XPATH, "(//span[@class='oxd-text oxd-text--span'][normalize-space()='Decending'])[1]")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    num_of_rows = (By.XPATH, "//div[@class='orangehrm-container']/div/div[@class='oxd-table-body']"
                             "/div[@class='oxd-table-card']")

    ##Elements##

    def get_sort_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.sort_button))

    def get_ascending_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.ascending_button))

    def get_descending_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.descending_button))

    def get_search_button_for_sort(self):
        return self.driver.find_element(*self.search_button)

    def get_num_of_rows(self):
        return self.driver.find_elements(*self.num_of_rows)

    #def get_iterate_username(self, start):
        #return self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['+start+']/div/div[2]/div')

    ##Methods##

    def click_sort_button(self):
        self.get_sort_button().click()

    def click_ascending_button(self):
        self.get_ascending_button().click()
        time.sleep(2)

        start = 0
        emp_list = []
        while start < len(self.get_num_of_rows()):
            start += 1
            sample = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]'
                                                        f'/div/div[2]/div[{start}]/div/div[2]/div')
            emp_list.append(sample.text.lower())

        sort_list_asc = emp_list.copy()
        sort_list_asc.sort()
        logger.info(emp_list)
        logger.info(sort_list_asc)

        assert emp_list == sort_list_asc
        logger.info('Ascending Success')

    def click_descending_button(self):
        self.get_descending_button().click()
        time.sleep(2)

        start = 0
        emp_list = []
        while start < len(self.get_num_of_rows()):
            start += 1
            sample = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]'
                                                        f'/div/div[2]/div[{start}]/div/div[2]/div')
            emp_list.append(sample.text.lower())

        sort_list_desc = emp_list.copy()
        sorted_list = sorted(sort_list_desc, reverse=True)   #, key=str.casefold
        logger.info(emp_list)
        logger.info(sorted_list)

        assert emp_list == sorted_list
        logger.info('Descending Success')

    def click_search_button_sort(self):
        time.sleep(2)
        self.get_search_button_for_sort().click()

