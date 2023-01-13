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
USER = 'Paul_testyyy'
PASSWORD = 'Testing08*'
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
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)


        # Select the Leave for fullday
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Leave']"))).click() # click leave
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Apply']"))).click() # click apply for leave
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill "
                                                         "oxd-select-text--arrow']"))).click() # click leave type
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='US - Personal']"))).click() #Click leave type personal
        time.sleep(3)
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]").send_keys('2022-12-27') #from date
        time.sleep(3)

        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").click()
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").send_keys(Keys.BACKSPACE*10)  # to date
        time.sleep(3)
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").send_keys('2022-12-27')  # to date

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Apply']"))).click() #click save


        # Leave Halfday-Morning
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Leave']"))).click()  # click leave
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Apply']"))).click()  # click apply for leave
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill "
        "oxd-select-text--arrow']"))).click()  # click leave type
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='US - Personal']"))).click()  # Click leave type personal
        time.sleep(3)
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]").send_keys('2022-12-29')  # from date
        time.sleep(3)

        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").click()
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").send_keys(Keys.BACKSPACE * 10)  # to date
        time.sleep(3)
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").send_keys('2022-12-29')  # to date

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"))).click()  # click leave type
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/span[text()='Half Day - Morning']"))).click()  # Click leave type personal

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Apply']"))).click()  # click save

        # Leave Halfday- Afternoon
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Leave']"))).click()  # click leave
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Apply']"))).click()  # click apply for leave
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill "
                                                         "oxd-select-text--arrow']"))).click()  # click leave type
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div/span[text()='US - Personal']"))).click()  # Click leave type personal
        time.sleep(3)
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]").send_keys('2022-12-30')  # from date
        time.sleep(3)

        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").click()
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").send_keys(
            Keys.BACKSPACE * 10)  # to date
        time.sleep(3)
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").send_keys('2022-12-30')  # to date

        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"))).click()  # click leave type
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div/span[text()='Half Day - Afternoon']"))).click()  # Click leave type personal

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Apply']"))).click()  # click save

        # Leave Specify Time
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Leave']"))).click()  # click leave
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Apply']"))).click()  # click apply for leave
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill "
                                                         "oxd-select-text--arrow']"))).click()  # click leave type
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div/span[text()='US - Personal']"))).click()  # Click leave type personal
        time.sleep(3)
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]").send_keys('2022-12-08')  # from date
        time.sleep(3)

        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").click()
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").send_keys(
            Keys.BACKSPACE * 10)  # to date
        time.sleep(3)
        driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]").send_keys('2022-12-08')  # to date

        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"))).click()  # click leave type
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div/span[text()='Specify Time']"))).click()  # Click leave type personal

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//i[@class='oxd-icon bi-clock oxd-time-input--clock'])[1]"))).click()    # click first clock

        driver.find_element(By.XPATH, "(// input[@ placeholder='hh:mm'])[1]").send_keys(
            Keys.BACKSPACE * 10)  # delete clock one value

        driver.find_element(By.XPATH, "(// input[@ placeholder='hh:mm'])[1]").send_keys('08:00 AM')

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//i[@class='oxd-icon bi-clock oxd-time-input--clock'])[2]"))).click()  # click second clock

        driver.find_element(By.XPATH, "(// input[@ placeholder='hh:mm'])[2]").send_keys(
            Keys.BACKSPACE * 10)  # delete clock one value

        driver.find_element(By.XPATH, "(// input[@ placeholder='hh:mm'])[2]").send_keys('03:00 PM')
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Apply']"))).click()  # click save




    # Leave Entitlement

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Leave']"))).click()  # click leave
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Entitlements']"
                                                         "//i[@class='oxd-icon bi-chevron-down']"))).click() # click entitlements
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='My Entitlements']"))).click() # click my entitlements
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill "
                                                         "oxd-select-text--arrow']"))).click()  # click leave type
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div/span[text()='US - Personal']"))).click()  # Click leave type personal

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Search']"))).click()  # Click search









        time.sleep(4)


LogAdmin = LoginAdmin()
LogAdmin.Username()