import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc
from Utilities.data import comment

lg = LogFunc()
logger = lg.get_log()


class AdminApproveReject():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    leave_button = (By.XPATH, "//span[normalize-space()='Leave']")
    leave_admin_verif = (By.XPATH, "//a[normalize-space()='Apply']")
    approve_button = (By.XPATH, "(//button[@type='button'][normalize-space()='Approve'])[1]")
    reject_button = (By.XPATH, "(//button[@type='button'][normalize-space()='Reject'])[1]")
    three_dots_vertical = (By.XPATH, "(//i[@class='oxd-icon bi-three-dots-vertical'])[1]")
    add_comment = (By.XPATH, "//p[normalize-space()='Add Comment']")
    comment_box = (By.XPATH, "//textarea[@placeholder='Comment here']")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")

    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    leave_list = (By.XPATH, "(//a[normalize-space()='Leave List'])[1]")
    leave_detail_verif = (By.XPATH, "//h6[normalize-space()='Leave Request Details']")

    comment_verif = (By.XPATH, "//div[contains(text(),'sample comment')]")
    app_leave_comm_verif = (By.XPATH, "//span[normalize-space()='(6) Records Found']")
    rej_leave_no_comm_verif = (By.XPATH, "//span[normalize-space()='(5) Records Found']")

    ##Elements##

    def get_leave_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.leave_button))

    def get_leave_admin_verif(self):
        return self.driver.find_element(*self.leave_admin_verif)

    def get_approve_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.approve_button))

    def get_reject_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.reject_button))

    def get_three_dots_vertical(self):
        return self.wait.until(EC.element_to_be_clickable(self.three_dots_vertical))

    def get_add_comment(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_comment))

    def get_comment_box(self):
        return self.driver.find_element(*self.comment_box)

    def get_save_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_button))

    def get_leave_list(self):
        return self.wait.until(EC.element_to_be_clickable(self.leave_list))

    def get_search_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_button))

    def get_comment_verif(self):
        return self.driver.find_element(*self.comment_verif)

    def get_app_leave_comm_verif(self):
        return self.driver.find_element(*self.app_leave_comm_verif)

    def get_rej_leave_no_comm_verif(self):
        return self.driver.find_element(*self.rej_leave_no_comm_verif)

    ##Methods##

    def click_leave_button(self):
        self.get_leave_button().click()

    def click_approve_button(self):
        self.get_approve_button().click()

    def click_reject_button(self):
        self.get_reject_button().click()

    def click_three_dots_vertical(self):
        self.get_three_dots_vertical().click()

    def click_add_comment(self):
        self.get_add_comment().click()

    def click_comment_box(self, comment):
        time.sleep(2)
        self.get_comment_box().send_keys(comment)

    def click_save_button_for_leave_comment(self):
        self.get_save_button().click()
        time.sleep(3)
        comment_verif = self.get_comment_verif()
        assert comment_verif.text == comment.get('comment')
        logger.info('Comment Success')

    def click_approve_button_with_comment(self):
        time.sleep(2)
        self.get_approve_button().click()
        time.sleep(3)
        leave_comment = self.get_app_leave_comm_verif()
        assert leave_comment.text == '(6) Records Found'
        logger.info('Success Leave with comment')

    def click_reject_button_no_comment(self):
        time.sleep(2)
        self.get_reject_button().click()
        time.sleep(3)
        reject_no_comment = self.get_rej_leave_no_comm_verif()
        assert reject_no_comment.text == '(5) Records Found'
        logger.info('Success Reject with no comment')

    def click_leave_list(self):
        self.get_leave_list().click()

    def click_search_button(self):
        self.get_search_button().click()

    def click_leave_admin_verif(self):
        time.sleep(3)
        self.get_leave_button().click()
        time.sleep(4)
        leave_verif = self.get_leave_list()
        assert leave_verif.text == 'Leave List'
        logger.info('Success Access on Leave Page')
        time.sleep(4)
