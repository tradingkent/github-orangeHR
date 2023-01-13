import time
import pytest

from Pages.orangeHR_login_page import LoginPage

from Utilities.config import ss_folder
from Utilities.config import timestamp
from Utilities.data import username_entry_admin
from Utilities.data import password_entry
from Utilities.data import username_entry_ess


@pytest.mark.usefixtures("setup")
class TestAccountDisabled():

    @pytest.mark.tags('All', 'TS1_TC17', 'disabled')
    def test_admin_account_disabled(self):

        # Admin account disabled
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(username_entry_admin.get('username_entry_disabled'),
                               password_entry.get('password_entry_one'))
        login_admin.click_button_account_disabled()

        sss_name = ss_folder + timestamp + '_ss_admin_acc_disabled.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC18', 'disabled')
    def test_ess_account_disabled(self):

        # ESS account disabled
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(username_entry_ess.get('username_entry_disabled'),
                               password_entry.get('password_entry_one'))
        login_admin.click_button_account_disabled()

        sss_name = ss_folder + timestamp + '_ss_ess_acc_disabled.png'
        self.driver.save_screenshot(sss_name)



