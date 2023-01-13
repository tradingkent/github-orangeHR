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
driver.maximize_window()
time.sleep(2)

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

        #Log in as Admin
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(USER)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(PASSWORD)

        #Validate Admin Test Data
        if (Admin_Credential.get('User') == USER) and (Admin_Credential.get('Password') == PASSWORD):
            driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
            print('Admin Detected')

        else:
            print('Not Admin')
            driver.close()

        time.sleep(3)
        # Validate Admin Successful Login
        login_verify = driver.find_element(By.XPATH, "//li[1]//a[1]//span[1]")

        if login_verify.text == 'Admin':
            print('Admin Login Successful')

        else:
            print('Something is wrong please check dashboard')

        #Select the Admin button and Add Button
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[1]//a[1]//span[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()
        #time.sleep(5)

        #Select Admin
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'-- Select --')])[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='Admin']"))).click()

        #Select Enable
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='Enabled']"))).click()
        time.sleep(2)

        #Select Employee name
        driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys(EMPLOYEE_NAME)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='Linda Jane Anderson']"))).click()
        time.sleep(2)

        #Username entry
        driver.find_element(By.XPATH, '//input[@autocomplete="off"]').send_keys(USERNAME_ENTRY)

        #Enter New and Confirm Password
        driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys(NEW_PASSWORD)
        driver.find_element(By.XPATH, "(// input[@ type='password'])[2]").send_keys(NEW_PASSWORD)

        # Save
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()

        time.sleep(5)

        #System Users check for Added User Admin and Search Result


        #Fillout Search box parameters (need to cleanup)

        #Click Admin button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[1]//a[1]//span[1]"))).click()
        time.sleep(3)
        # Fillout Username
        driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys(USERNAME_ENTRY)

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'-- Select --')])[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='Admin']"))).click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys(EMPLOYEE_NAME)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='Linda Jane Anderson']"))).click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='Enabled']"))).click()
        time.sleep(2)

        #Click Search
        driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(3)
        search_result = driver.find_element(By.XPATH, "//span[normalize-space()='(1) Record Found']")
        print(search_result.text)

        #Validation of Added User as Admin and Search Result with (1) Record Found
        if search_result.text == '(1) Record Found':
            print('Add user and search successful')

        else:
            print('There is an issue searching the unique username, please check')
            driver.close()

        #Update Created User

        #Click Edit button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']"))).click()

        #Click Yes check box for changing password
        wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Yes']"))).click()

        #Click box for changing to ESS
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Admin')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='ESS']"))).click()

        # Click box for changing to Disabled
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Enabled')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='Disabled']"))).click()

        #Input change new password
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@ type='password'])[1]"))).send_keys(CHANGE_PASSWORD)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@ type='password'])[2]"))).send_keys(CHANGE_PASSWORD)

        #Save Button
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()

        #Validation for Edit

        '''
        #Click Admin button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[1]//a[1]//span[1]"))).click()
        time.sleep(3)
        #Fillout Username
        driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys(USERNAME_ENTRY)

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'-- Select --')])[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='ESS']"))).click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys(EMPLOYEE_NAME)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='Linda Jane Anderson']"))).click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='Disabled']"))).click()
        time.sleep(2)

        #Click Search
        driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(3)
        '''



        #Delete User
        # Click Admin button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[1]//a[1]//span[1]"))).click()
        time.sleep(3)

        # Fillout Username
        driver.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys(USERNAME_ENTRY)

        #Click Search Button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']"))).click()

        # Delete
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='oxd-icon bi-trash'])[1]"))).click()

        # Delete Pop up
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Yes, Delete'])[1]"))).click()

        #Delete Validation
        time.sleep(5)
        delete_result = driver.find_element(By.XPATH, "(//span[normalize-space()='No Records Found'])[1]")
        print(delete_result.text)

        # Validation of Delete User and should be No Records Found
        if delete_result.text == 'No Records Found':
            print('Successfully Deleted')

        else:
            print('There is an issue with deleting, please check')
            driver.close()




















        time.sleep(10)


LogAdmin = LoginAdmin()
LogAdmin.Username()