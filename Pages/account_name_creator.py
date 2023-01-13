

from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.orangeHR_admin_PIM_add_empl import AddEmplPIM
from Pages.orangeHR_admin_PIM_update_nonexisting_details import UpdateEmplPIM
from Utilities.data import admin_credential, first_empl, sec_empl, third_empl, fourth_empl, fifth_empl, sixth_empl
from Utilities.config import ss_folder
from Utilities.config import timestamp
from Utilities.data import employee_entry_admin
from Utilities.data import employee_entry_ess
from Utilities.data import username_entry_admin
from Utilities.data import username_entry_ess
from Utilities.data import password_entry
from Utilities.data import new_password_entry

from Pages.orangeHR_admin_page import AddUser
from Pages.orangeHR_login_page import LoginPage
from Pages.orangeHR_ess_sort import SortUsernameESS

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Get chromedriver and open the URL
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://opensource-demo.orangehrmlive.com/')
wait = WebDriverWait(driver, 20)
driver.maximize_window()
time.sleep(2)


class AddUserPIM():

    def login_admin_pim(self):

        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(admin_credential.get('user'))
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(admin_credential.get('passw'))
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)

        # Add PIM sec empl
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='PIM']"))).click()
        wait.until(EC.element_to_be_clickable((By. XPATH, "//button[normalize-space()='Add']"))).click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys(sec_empl.get('firstname'))
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(sec_empl.get('lastname'))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()
        time.sleep(5)

        # Add PIM third empl
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='PIM']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys(third_empl.get('firstname'))
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(third_empl.get('lastname'))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()
        time.sleep(5)

        # Add PIM fourth empl
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='PIM']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys(fourth_empl.get('firstname'))
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(fourth_empl.get('lastname'))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()
        time.sleep(5)

        # Add PIM sixth empl
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='PIM']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys(sixth_empl.get('firstname'))
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(sixth_empl.get('lastname'))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()
        time.sleep(3)

au = AddUserPIM()
au.login_admin_pim()













