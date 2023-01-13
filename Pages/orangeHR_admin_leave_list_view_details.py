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


class AdminLeaveViewDetails():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    # view leave detail
    leave_detail_three_dots_detail_page = (By.XPATH, "(//i[@class='oxd-icon bi-three-dots-vertical'])[2]")
    view_leave_details = (By.XPATH, "(//p[normalize-space()='View Leave Details'])[1]")
    view_leave_details_verif = (By.XPATH, "//h6[normalize-space()='Leave Request Details']")
    approve_button_no_comment = (By.XPATH, "//button[normalize-space()='Approve']")
    status_taken = (By.XPATH, "//div[contains(text(),'Taken')]")
    status_approved_no_comm = (By.XPATH, "//div[contains(text(),'Scheduled')]")
    leave_detail_three_dots_comm_reject = (By.XPATH, "(//i[@class='oxd-icon bi-three-dots-vertical'])[3]")
    view_leave_details_comm_reject = (By.XPATH, "//p[normalize-space()='View Leave Details']")
    comment_button = (By.XPATH, "//button[normalize-space()='Comments']")
    status_rejected = (By.XPATH, "//div[contains(text(),'Rejected')]")
    save_button_reject_comment = (By.XPATH, "//button[normalize-space()='Save']")
    reject_button_comment = (By.XPATH, "//button[normalize-space()='Reject']")

    reject_comment_verif = (By.XPATH, "//div[contains(text(),'sample comment')]")
    rej_comm_dots_vertical = (By.XPATH, "//i[@class='oxd-icon bi-three-dots-vertical']")
    add_comment_button = (By.XPATH, "//p[normalize-space()='Add Comment']")

    ##Elements##

    # Detail Page
    def get_leave_detail_three_dots_detail_page(self):
        return self.wait.until(EC.element_to_be_clickable(self.leave_detail_three_dots_detail_page))

    def get_view_leave_details(self):
        return self.wait.until(EC.element_to_be_clickable(self.view_leave_details))

    def get_view_leave_details_verif(self):
        return self.driver.find_element(*self.view_leave_details_verif)

    def get_approve_button_no_comment(self):
        return self.wait.until(EC.element_to_be_clickable(self.approve_button_no_comment))

    def get_status_taken(self):
        return self.driver.find_element(*self.status_taken)

    def get_status_approved_no_comm(self):
        return self.driver.find_element(*self.status_approved_no_comm)

    def get_leave_detail_three_dots_comm_reject(self):
        return self.wait.until(EC.element_to_be_clickable(self.leave_detail_three_dots_comm_reject))

    def get_view_leave_details_comm_reject(self):
        return self.wait.until(EC.element_to_be_clickable(self.view_leave_details_comm_reject))

    def get_comment_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.comment_button))

    def get_save_button_reject_comment(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_button_reject_comment))

    def get_status_rejected(self):
        return self.driver.find_element(*self.status_rejected)

    def get_reject_button_comment(self):
        return self.wait.until(EC.element_to_be_clickable(self.reject_button_comment))

    def get_rej_comm_dots_vertical(self):
        return self.wait.until(EC.element_to_be_clickable(self.rej_comm_dots_vertical))

    def get_add_comment_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_comment_button))

    def get_reject_comment_verif(self):
        return self.driver.find_element(*self.reject_comment_verif)


    ##Methods##

    def click_leave_detail_three_dots_detail_page(self):
        self.get_leave_detail_three_dots_detail_page().click()

    def click_view_leave_details(self):
        self.get_view_leave_details().click()
        time.sleep(3)
        view_leave_verif = self.get_view_leave_details_verif()
        assert view_leave_verif.text == 'Leave Request Details'
        logger.info('Success View Leave Details')

    def click_approve_button_no_comment(self):
        time.sleep(2)
        self.get_approve_button_no_comment().click()
        time.sleep(3)
        approve_no_comment = self.get_status_approved_no_comm()
        assert approve_no_comment.text == 'Scheduled'
        logger.info('Success Approve with no comment')

    def click_leave_detail_three_dots_comm_reject(self):
        self.get_leave_detail_three_dots_comm_reject().click()

    def click_view_leave_details_comm_reject(self):
        self.get_view_leave_details_comm_reject().click()

    def click_comment_button(self):
        self.get_comment_button().click()

    def click_save_button_reject_comment(self):
        self.get_save_button_reject_comment().click()
        time.sleep(3)
        reject_comment_verif = self.get_reject_comment_verif()
        assert reject_comment_verif.text == comment.get('comment')
        logger.info('Reject Comment Success')

    def click_reject_button_comment(self):
        time.sleep(2)
        self.get_reject_button_comment().click()
        time.sleep(3)
        status_rej = self.get_status_rejected()
        assert status_rej.text == 'Rejected'
        logger.info('Reject with comment success')

    def click_rej_comm_dots_vertical(self):
        self.get_rej_comm_dots_vertical().click()

    def click_add_comment_button(self):
        self.get_add_comment_button().click()
















