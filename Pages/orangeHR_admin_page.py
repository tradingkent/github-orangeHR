import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.common import LogFunc
from Utilities.data import add_user_validation

lg = LogFunc()
logger = lg.get_log()

class AddUser():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ##Locators##

    #Add User
    admin_button = (By.XPATH, "//li[1]//a[1]//span[1]")
    add_button = (By.XPATH, "//button[normalize-space()='Add']")
    drp_user_role = (By.XPATH, "(//div[contains(text(),'-- Select --')])[1]")
    select_admin = (By.XPATH, "//div/span[text()='Admin']")
    select_ess = (By.XPATH, "//div/span[text()='ESS']")
    drp_status = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
    select_enabled = (By.XPATH, "//div/span[text()='Enabled']")
    select_disabled = (By.XPATH, "//div/span[text()='Disabled']")
    select_emp_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    click_emp_name_admin = (By.XPATH, "//div/span[text()='Jon  Snow']")       # Admin
    click_emp_name_admin_for_leave = (By.XPATH, "//div/span[text()='Tyrion  Lannister']") # Admin for leave
    click_emp_name_admin_disabled = (By.XPATH, "//div/span[text()='Daenerys  Targaryen']")  # Admin with Disabled
    click_emp_name_ess = (By.XPATH, "//div/span[text()='Robert  Baratheon']")            # ESS
    click_emp_name_ess_disabled = (By.XPATH, "//div/span[text()='Ned  Stark']")  # ESS with Disabled
    select_username_entry = (By.XPATH, '//input[@autocomplete="off"]')
    confirm_password_one = (By.XPATH, "(//input[@type='password'])[1]")
    confirm_password_two = (By.XPATH, "(// input[@ type='password'])[2]")
    save_button = (By.XPATH, "(//button[normalize-space()='Save'])[1]")

    # Search (System Users)
    select_search_username = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']"
                                 "//div//input[@class='oxd-input oxd-input--active']")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    search_result_verify = (By.XPATH, "//span[normalize-space()='(1) Record Found']")

    # Edit User
    edit_button = (By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']")
    check_box = (By.XPATH, "//label[normalize-space()='Yes']")
    edit_role_verif = (By.XPATH, "//div[contains(text(),'ESS')]")
    edit_status_verif = (By.XPATH, "//div[contains(text(),'Disabled')]")

    # Delete
    delete_button = (By.XPATH, "(//i[@class='oxd-icon bi-trash'])[1]")
    delete_popup = (By.XPATH, "(//button[normalize-space()='Yes, Delete'])[1]")
    no_result_verify = (By.XPATH, "(//span[normalize-space()='No Records Found'])[1]")

    ##Elements##

    # Add User with waits

    def get_admin_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.admin_button))

    def get_add_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_button))

    def get_drp_user_role(self):
        return self.wait.until(EC.element_to_be_clickable(self.drp_user_role))

    def get_select_admin(self):
        return self.wait.until(EC.element_to_be_clickable(self.select_admin))

    def get_select_ess(self):
        return self.wait.until(EC.element_to_be_clickable(self.select_ess))

    def get_drp_status(self):
        return self.wait.until(EC.element_to_be_clickable(self.drp_status))

    def get_select_enabled(self):
        return self.wait.until(EC.element_to_be_clickable(self.select_enabled))

    def get_select_disabled(self):
        return self.wait.until(EC.element_to_be_clickable(self.select_disabled))

    def get_select_emp_name(self):
        return self.driver.find_element(*self.select_emp_name)

    def get_click_emp_name_admin(self):
        return self.wait.until(EC.element_to_be_clickable(self.click_emp_name_admin))

    def get_click_emp_name_admin_for_leave(self):
        return self.wait.until(EC.element_to_be_clickable(self.click_emp_name_admin_for_leave))

    def get_click_emp_name_ess(self):
        return self.wait.until(EC.element_to_be_clickable(self.click_emp_name_ess))

    def get_click_emp_name_admin_disabled(self):
        return self.wait.until(EC.element_to_be_clickable(self.click_emp_name_admin_disabled))

    def get_click_emp_name_ess_disabled(self):
        return self.wait.until(EC.element_to_be_clickable(self.click_emp_name_ess_disabled))

    def get_select_username_entry(self):
        return self.driver.find_element(*self.select_username_entry)

    def get_confirm_password_one(self):
        return self.driver.find_element(*self.confirm_password_one)

    def get_confirm_password_two(self):
        return self.driver.find_element(*self.confirm_password_two)

    def get_save_button(self):
        return self.driver.find_element(*self.save_button)

    def get_add_admin_verify(self):
        return self.driver.find_element(*self.add_button)

    # Search
    def get_select_search_username(self):
        return self.driver.find_element(*self.select_search_username)

    def get_search_button(self):
        return self.driver.find_element(*self.search_button)

    def get_search_result_verify(self):
        return self.driver.find_element(*self.search_result_verify)

    # Disabled and Delete Verification
    def get_no_result_verify(self):
        return self.driver.find_element(*self.no_result_verify)

    # Edit User
    def get_edit_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.edit_button))

    def get_check_box(self):
        return self.wait.until(EC.element_to_be_clickable(self.check_box))

    def get_edit_role_verif(self):
        return self.driver.find_element(*self.edit_role_verif)

    def get_edit_status_verif(self):
        return self.driver.find_element(*self.edit_status_verif)

    # Delete User
    def get_delete_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.delete_button))

    def get_delete_popup(self):
        return self.wait.until(EC.element_to_be_clickable(self.delete_popup))

    ##Methods##

    #Add User
    #Select the Admin button and Add Button
    def click_admin_button(self):
        self.get_admin_button().click()

    def click_add_button(self):
        self.get_add_button().click()

    def click_user_role_admin(self):
        self.get_drp_user_role().click()

    def click_admin(self):
        self.get_select_admin().click()

    def click_ess(self):
        self.get_select_ess().click()

    # Select Enable
    def click_drp_status(self):
        self.get_drp_status().click()

    def click_enabled(self):
        self.get_select_enabled().click()

    def click_disabled(self):
        self.get_select_disabled().click()

    # Select Employee name
    def employee_entry(self, empEntry):
        time.sleep(2)
        self.get_select_emp_name().send_keys(empEntry)

    def click_empl_name_admin(self):
        self.get_click_emp_name_admin().click()

    def click_empl_name_admin_for_leave(self):
        self.get_click_emp_name_admin_for_leave().click()

    def click_empl_name_ess(self):
        self.get_click_emp_name_ess().click()

    def click_empl_name_admin_disabled(self):
        self.get_click_emp_name_admin_disabled().click()

    def click_empl_name_ess_disabled(self):
        self.get_click_emp_name_ess_disabled().click()

    # Username entry
    def username_entry(self, userEntry):
        self.get_select_username_entry().send_keys(userEntry)

        # Enter New and Confirm Password
    def confirm_pass_one(self, confPassOne):
        self.get_confirm_password_one().send_keys(confPassOne)

    def confirm_pass_two(self, confPassTwo):
        self.get_confirm_password_two().send_keys(confPassTwo)

    # Save
    def click_save_button(self):
        time.sleep(2)
        self.get_save_button().click()
        time.sleep(6)
        add_login_verify = self.get_add_admin_verify()
        assert add_login_verify.text == add_user_validation.get('add_user')
        logger.info('Add Success')

    # Search
    def enter_search_username(self, search_username):
        time.sleep(2)
        self.get_select_search_username().send_keys(search_username)

    def click_search_button(self):
        time.sleep(2)
        self.get_search_button().click()
        time.sleep(3)
        search_result = self.get_search_result_verify()
        assert search_result.text == '(1) Record Found'
        logger.info('Add user and search successful')

    # Edit User
    def click_edit_button(self):
        self.get_edit_button().click()

    def click_check_box(self):
        self.get_check_box().click()

    def click_save_button_for_edit(self):
        time.sleep(2)
        self.get_save_button().click()

    def click_search_button_for_edit(self):
        time.sleep(2)
        self.get_search_button().click()
        time.sleep(3)
        search_result = self.get_search_result_verify()
        edit_role_verif = self.get_edit_role_verif()
        edit_status_verif = self.get_edit_status_verif()

        if search_result.text == '(1) Record Found':
            assert ((edit_role_verif.text == 'ESS') and (edit_status_verif.text == 'Disabled'))
            logger.info('Success Edit')

        else:
            logger.info('something went wrong')

    # Delete
    def click_delete_button(self):
        self.get_delete_button().click()

    def click_delete_popup(self):
        self.get_delete_popup().click()

    def click_search_button_for_delete(self):
        time.sleep(2)
        self.get_search_button().click()

    def click_search_button_no_result_for_delete(self):
        time.sleep(2)
        self.get_search_button().click()
        time.sleep(3)
        search_no_result = self.get_no_result_verify()
        assert search_no_result.text == 'No Records Found'
        logger.info('Success Deletion')
