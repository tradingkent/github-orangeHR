import time
import pytest

from Utilities.data import admin_credential
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


@pytest.mark.usefixtures("setup")
class TestLoginAdmin():

    @pytest.mark.tags('All', 'TS1_TC1', 'user_mngt')
    def test_login_admin(self):

        # Login as Admin process
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(admin_credential.get('user'),
                               admin_credential.get('passw'))
        login_admin.click_button()

        sss_name = ss_folder + timestamp + '_ss_admin_login.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC2', 'user_mngt')
    def test_add_admin(self):

        # Add User as an Admin
        add_user_admin = AddUser(self.driver, self.wait)
        add_user_admin.click_admin_button()
        add_user_admin.click_add_button()
        add_user_admin.click_user_role_admin()
        add_user_admin.click_admin()
        add_user_admin.click_drp_status()
        add_user_admin.click_enabled()
        add_user_admin.employee_entry(employee_entry_admin.get('employee_entry'))
        add_user_admin.click_empl_name_admin()
        add_user_admin.username_entry(username_entry_admin.get('username_entry'))
        add_user_admin.confirm_pass_one(password_entry.get('password_entry_one'))
        add_user_admin.confirm_pass_two(password_entry.get('password_entry_two'))
        add_user_admin.click_save_button()

        sss_name = ss_folder + timestamp + '_ss_add_admin.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC3', 'user_mngt')
    def test_add_admin_for_leave(self):

        # Add User as an Admin for leave
        add_user_admin = AddUser(self.driver, self.wait)
        add_user_admin.click_admin_button()
        add_user_admin.click_add_button()
        add_user_admin.click_user_role_admin()
        add_user_admin.click_admin()
        add_user_admin.click_drp_status()
        add_user_admin.click_enabled()
        add_user_admin.employee_entry(employee_entry_admin.get('employee_entry_leave'))
        add_user_admin.click_empl_name_admin_for_leave()
        add_user_admin.username_entry(username_entry_admin.get('username_entry_leave'))
        add_user_admin.confirm_pass_one(password_entry.get('password_entry_one'))
        add_user_admin.confirm_pass_two(password_entry.get('password_entry_two'))
        add_user_admin.click_save_button()

        sss_name = ss_folder + timestamp + '_ss_add_admin_for_leave.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC4', 'user_mngt')
    def test_add_ess(self):

        # Add User as an ESS
        add_user_ess = AddUser(self.driver, self.wait)
        add_user_ess.click_admin_button()
        add_user_ess.click_add_button()
        add_user_ess.click_user_role_admin()
        add_user_ess.click_ess()
        add_user_ess.click_drp_status()
        add_user_ess.click_enabled()
        add_user_ess.employee_entry(employee_entry_ess.get('employee_entry'))
        add_user_ess.click_empl_name_ess()
        add_user_ess.username_entry(username_entry_ess.get('username_entry'))
        add_user_ess.confirm_pass_one(password_entry.get('password_entry_one'))
        add_user_ess.confirm_pass_two(password_entry.get('password_entry_two'))
        add_user_ess.click_save_button()

        sss_name = ss_folder + timestamp + '_ss_add_ess.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC6', 'user_mngt')
    def test_add_admin_disabled(self):

        # Add User as an Admin with Disabled
        add_user_admin_disabled = AddUser(self.driver, self.wait)
        add_user_admin_disabled.click_admin_button()
        add_user_admin_disabled.click_add_button()
        add_user_admin_disabled.click_user_role_admin()
        add_user_admin_disabled.click_admin()
        add_user_admin_disabled.click_drp_status()
        add_user_admin_disabled.click_disabled()
        add_user_admin_disabled.employee_entry(employee_entry_admin.get('employee_entry_disabled'))
        add_user_admin_disabled.click_empl_name_admin_disabled()
        add_user_admin_disabled.username_entry(username_entry_admin.get('username_entry_disabled'))
        add_user_admin_disabled.confirm_pass_one(password_entry.get('password_entry_one'))
        add_user_admin_disabled.confirm_pass_two(password_entry.get('password_entry_two'))
        add_user_admin_disabled.click_save_button()

        sss_name = ss_folder + timestamp + '_ss_add_admin_disabled.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC7', 'user_mngt')
    def test_add_ess_disabled(self):

        # Add User as an ESS with Disabled
        add_user_ess_disabled = AddUser(self.driver, self.wait)
        add_user_ess_disabled.click_admin_button()
        add_user_ess_disabled.click_add_button()
        add_user_ess_disabled.click_user_role_admin()
        add_user_ess_disabled.click_ess()
        add_user_ess_disabled.click_drp_status()
        add_user_ess_disabled.click_disabled()
        add_user_ess_disabled.employee_entry(employee_entry_ess.get('employee_entry_disabled'))
        add_user_ess_disabled.click_empl_name_ess_disabled()
        add_user_ess_disabled.username_entry(username_entry_ess.get('username_entry_disabled'))
        add_user_ess_disabled.confirm_pass_one(password_entry.get('password_entry_one'))
        add_user_ess_disabled.confirm_pass_two(password_entry.get('password_entry_two'))
        add_user_ess_disabled.click_save_button()

        sss_name = ss_folder + timestamp + '_ss_add_ess_disabled.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC8', 'user_mngt')
    def test_search_admin(self):

        # Search Admin in the database
        search_admin = AddUser(self.driver, self.wait)
        search_admin.click_admin_button()
        search_admin.enter_search_username(username_entry_admin.get('username_entry'))
        search_admin.click_user_role_admin()
        search_admin.click_admin()
        search_admin.employee_entry(employee_entry_admin.get('employee_entry'))
        search_admin.click_empl_name_admin()
        search_admin.click_drp_status()
        search_admin.click_enabled()
        search_admin.click_search_button()

        sss_name = ss_folder + timestamp + '_ss_search_admin.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC9', 'user_mngt')
    def test_update_admin(self):

        # Update User (Admin)
        update_user_admin = AddUser(self.driver, self.wait)
        update_user_admin.click_edit_button()
        update_user_admin.click_user_role_admin()
        update_user_admin.click_ess()
        update_user_admin.click_drp_status()
        update_user_admin.click_disabled()
        update_user_admin.click_check_box()
        update_user_admin.confirm_pass_one(new_password_entry.get('new_password_entry_one'))
        update_user_admin.confirm_pass_two(new_password_entry.get('new_password_entry_two'))
        update_user_admin.click_save_button()
        update_user_admin.click_admin_button()
        update_user_admin.enter_search_username(username_entry_admin.get('username_entry'))
        update_user_admin.click_search_button_for_edit()

        sss_name = ss_folder + timestamp + '_ss_edit_admin.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC10', 'user_mngt')
    def test_delete_admin(self):

        # Delete Admin
        delete_user = AddUser(self.driver, self.wait)
        delete_user.click_admin_button()
        delete_user.enter_search_username(username_entry_admin.get('username_entry'))
        delete_user.click_search_button_for_delete()
        delete_user.click_delete_button()
        delete_user.click_delete_popup()
        delete_user.click_admin_button()
        delete_user.enter_search_username(username_entry_admin.get('username_entry'))
        delete_user.click_search_button_no_result_for_delete()

        sss_name = ss_folder + timestamp + '_ss_delete_admin.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC11', 'user_mngt')
    def test_search_ess(self):

        # Search ESS in the database
        search_ess = AddUser(self.driver, self.wait)
        search_ess.click_admin_button()
        search_ess.enter_search_username(username_entry_ess.get('username_entry'))
        search_ess.click_user_role_admin()
        search_ess.click_ess()
        search_ess.employee_entry(employee_entry_ess.get('employee_entry'))
        search_ess.click_empl_name_ess()
        search_ess.click_drp_status()
        search_ess.click_enabled()
        search_ess.click_search_button()

        sss_name = ss_folder + timestamp + '_ss_search_ess.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC12', 'user_mngt')
    def test_search_admin_disabled(self):

        # Search Admin in the database with Disabled status
        search_admin_disabled = AddUser(self.driver, self.wait)
        search_admin_disabled.click_admin_button()
        search_admin_disabled.enter_search_username(username_entry_admin.get('username_entry_disabled'))
        search_admin_disabled.click_user_role_admin()
        search_admin_disabled.click_admin()
        search_admin_disabled.employee_entry(employee_entry_admin.get('employee_entry_disabled'))
        search_admin_disabled.click_empl_name_admin_disabled()
        search_admin_disabled.click_drp_status()
        search_admin_disabled.click_disabled()
        search_admin_disabled.click_search_button()

        sss_name = ss_folder + timestamp + '_ss_search_admin_disabled.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC13', 'user_mngt')
    def test_search_ess_disabled(self):

        # Search ESS in the database with disabled status
        search_ess_disabled = AddUser(self.driver, self.wait)
        search_ess_disabled.click_admin_button()
        search_ess_disabled.enter_search_username(username_entry_ess.get('username_entry_disabled'))
        search_ess_disabled.click_user_role_admin()
        search_ess_disabled.click_ess()
        search_ess_disabled.employee_entry(employee_entry_ess.get('employee_entry_disabled'))
        search_ess_disabled.click_empl_name_ess_disabled()
        search_ess_disabled.click_drp_status()
        search_ess_disabled.click_disabled()
        search_ess_disabled.click_search_button()

        sss_name = ss_folder + timestamp + '_ss_search_ess_disabled.png'
        self.driver.save_screenshot(sss_name)
