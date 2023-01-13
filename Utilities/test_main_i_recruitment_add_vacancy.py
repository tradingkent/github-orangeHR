import time
import pytest

from Utilities.config import ss_folder
from Utilities.config import timestamp
from Utilities.data import password_entry
from Utilities.data import username_entry_admin
from Utilities.data import add_vacancy_data
from Utilities.data import employee_entry_admin

from Pages.orangeHR_login_page import LoginPage
from Pages.orangeHR_admin_page import AddUser
from Pages.orangeHR_recruitement_add_vacancy import RecAddVacancy



@pytest.mark.usefixtures("setup")
class TestRecruitment():

    @pytest.mark.tags('All', 'TS4_TC1', 'add_vac')
    def test_login_admin_recruitment(self):

        # Login as Admin for Recruitment
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(username_entry_admin.get('username_entry_leave'),
                               password_entry.get('password_entry_one'))
        login_admin.click_button()

        sss_name = ss_folder + timestamp + '_ss_admin_login.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC2', 'add_vac')
    def test_add_vacancy(self):

        # Verify Add Vacancy
        add_user_admin = AddUser(self.driver, self.wait)
        add_vacancy = RecAddVacancy(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        add_vacancy.click_vacancies_button()
        add_vacancy.click_add_button_rec()
        add_vacancy.click_vacancy_name_box(add_vacancy_data.get('vac_name'))
        add_vacancy.click_job_title_drp()
        add_vacancy.click_job_option()
        add_vacancy.click_description_box(add_vacancy_data.get('desc_box'))
        add_user_admin.employee_entry(employee_entry_admin.get('employee_entry_leave'))
        add_user_admin.click_empl_name_admin_for_leave()
        add_vacancy.click_number_pos_box(add_vacancy_data.get('pos_num'))
        add_vacancy.click_save_button_vacancies()

        add_vacancy.click_recruitment_button()
        add_vacancy.click_vacancies_button()
        add_user_admin.click_drp_status()
        add_vacancy.click_vacancy_enter()
        add_vacancy.click_search_button_vacancy()

        sss_name = ss_folder + timestamp + '_ss_add_vacancy.png'
        self.driver.save_screenshot(sss_name)

