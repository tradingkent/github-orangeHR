'''
list_1 = ['banana', 'kiwi', 'apple', 'mango', 'pineapple', 'guava', 'melon']

list_2 = ['banana', 'kiwi', 'apple', 'mango', 'pineapple', 'guava', 'melon']

assert list_1 == list_2
print('The same')

'''





import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from openpyxl import Workbook






#Get chromedriver and open the URL
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
time.sleep(3)

#Dictionary
Admin_Credential = {'User': 'Admin', 'Password': 'admin123'}

#Testdata
USER = 'Admin'
PASSWORD = 'admin123'
EMPLOYEE_NAME = 'Linda'
NEW_PASSWORD = 'Testing09*'
USERNAME_ENTRY = 'Linda_testeee'

#Testdata for Edit Functionality
CHANGE_PASSWORD = 'Testing10*'

class LoginAdmin():

    def Username(self):

        '''
        #Log in as Admin

        driver.find_element(By.XPATH, "//input[@placeholder='username']").send_keys(USER)
        driver.find_element(By.XPATH, "//input[@placeholder='password']").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//li[1]//a[1]//span[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//button[normalize-space()='Search'])[1]").click()
        #click asc and desc button
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-sort-alpha-down oxd-icon-button__icon oxd-table-header-sort-icon'])[1]").click()
        # click ascending option
        time.sleep(2)
        driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span'][normalize-space()='Ascending'])[1]").click()
        time.sleep(2)

        # get the total number of rows
        num_rows = driver.find_elements(By.XPATH, "//div[@class='orangehrm-container']/div/div[@class='oxd-table-body']/div[@class='oxd-table-card']")
        start = 0
        emp_list = []

        while start < len(num_rows):
            # locate the first column only
            start += 1
            sample = driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[{start}]/div/div[2]/div')
            emp_list.append(sample.text)

            sort_list_asc = emp_list.copy()

            sorted_list = sorted(sort_list_asc, key=str.casefold)


        #print(emp_list)
        #print(so)

        assert emp_list == sorted_list
        print('success')

        '''





        #Log in as Admin

        driver.find_element(By.XPATH, "//input[@placeholder='username']").send_keys(USER)
        driver.find_element(By.XPATH, "//input[@placeholder='password']").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//li[1]//a[1]//span[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//button[normalize-space()='Search'])[1]").click()
        #click asc and desc button
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-sort-alpha-down oxd-icon-button__icon oxd-table-header-sort-icon'])[1]").click()
        # click ascending option
        time.sleep(2)
        #driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span'][normalize-space()='Ascending'])[1]").click()
        driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span'][normalize-space()='Decending'])[1]").click()
        time.sleep(2)

        # get the total number of rows
        num_rows = driver.find_elements(By.XPATH, "//div[@class='orangehrm-container']/div/div[@class='oxd-table-body']/div[@class='oxd-table-card']")

        start = 0
        emp_list = []
        while start < len(num_rows):
            # locate the first column only
            start += 1
            sample = driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[{start}]/div/div[2]/div')
            emp_list.append(sample.text)

            sort_list_asc = emp_list.copy()

            sorted_list = sorted(sort_list_asc, reverse=True, key=str.casefold)


        print(emp_list)
        print(sorted_list)

        assert emp_list == sorted_list
        print('success')






        















la = LoginAdmin()
la.Username()






