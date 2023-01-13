import time
import pytest

from Utilities.data import admin_credential
from Utilities.data import first_empl
from Utilities.data import fifth_empl
from Utilities.config import ss_folder
from Utilities.config import timestamp
from Utilities.data import password_entry

from Pages.orangeHR_admin_page import AddUser
from Pages.orangeHR_login_page import LoginPage
from Pages.orangeHR_admin_PIM_add_empl import AddEmplPIM
from Pages.orangeHR_admin_PIM_update_nonexisting_details import UpdateEmplPIM

@pytest.mark.usefixtures("setup")
class TestPIM():

    @pytest.mark.tags('All', 'TS0_TC1', 'PIM')
    def test_login_admin_pim(self):

        # Add employees w/o login details
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(admin_credential.get('user'),
                               admin_credential.get('passw'))
        login_admin.click_button()

        sss_name = ss_folder + timestamp + '_ss_admin_login.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS0_TC2', 'PIM')
    def test_pim_add_first_empl(self):

        # Add PIM first empl
        add_pim = AddEmplPIM(self.driver, self.wait)
        add_pim.click_pim_button()
        add_pim.click_add_button_pim()
        add_pim.click_entername(first_empl.get('firstname'),
                               first_empl.get('lastname'))
        add_pim.click_save_button_pim()

        sss_name = ss_folder + timestamp + '_ss_add_pim_1.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS0_TC3', 'PIM')
    def test_pim_add_fifth_empl_with_login(self):

        # Add PIM fifth empl with login details
        add_pim = AddEmplPIM(self.driver, self.wait)
        add_user_admin = AddUser(self.driver, self.wait)

        add_pim.click_pim_button()
        add_pim.click_add_button_pim()
        add_pim.click_entername(fifth_empl.get('firstname'),
                               fifth_empl.get('lastname'))
        add_pim.click_toggle_button()
        add_pim.click_username_box(fifth_empl.get('uname'))
        add_user_admin.confirm_pass_one(password_entry.get('password_entry_one'))
        add_user_admin.confirm_pass_two(password_entry.get('password_entry_two'))
        add_pim.click_save_button_pim()

        sss_name = ss_folder + timestamp + '_ss_add_pim_5.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS0_TC4', 'PIM')
    def test_update_pim(self):

        # Update PIM employeee details
        add_pim = AddEmplPIM(self.driver, self.wait)
        add_user_admin = AddUser(self.driver, self.wait)
        upd_pim = UpdateEmplPIM(self.driver, self.wait)

        add_pim.click_pim_button()
        add_user_admin.employee_entry(fifth_empl.get('firstname'))
        upd_pim.click_emp_name_pim_edit()
        upd_pim.click_search_button_for_edit()
        add_user_admin.click_edit_button()
        upd_pim.click_entername_for_edit(fifth_empl.get('newfname'),
                                         fifth_empl.get('newlname'))
        upd_pim.click_save_button_edit_one()
        add_pim.click_pim_button()
        add_user_admin.employee_entry(fifth_empl.get('newfname'))
        upd_pim.click_emp_name_pim_after_edit()
        upd_pim.click_search_button_after_edit()

        sss_name = ss_folder + timestamp + '_ss_pim_after_edit.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS0_TC5', 'PIM')
    def test_search_non_existing_empl(self):

        # Search non-existing employee
        add_pim = AddEmplPIM(self.driver, self.wait)
        add_user_admin = AddUser(self.driver, self.wait)
        upd_pim = UpdateEmplPIM(self.driver, self.wait)

        add_pim.click_pim_button()
        add_user_admin.employee_entry(fifth_empl.get('firstname'))
        upd_pim.click_search_button_non_existing()

        sss_name = ss_folder + timestamp + '_ss_pim_search_non_existing.png'
        self.driver.save_screenshot(sss_name)


# sample comment












