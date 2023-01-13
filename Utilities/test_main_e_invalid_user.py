import time
import pytest

from Utilities.config import ss_folder
from Utilities.config import timestamp
from Utilities.data import invalid_credentials
from Utilities.data import admin_credential

from Pages.orangeHR_login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestInvalidUser():

    @pytest.mark.tags('All', 'TS1_TC19', 'invalid')
    def test_invalid_user(self):

        # Invalid Username and Password
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(invalid_credentials.get('invalid_username'),
                               invalid_credentials.get('invalid_password'))
        login_admin.click_button_invalid_user()

        sss_name = ss_folder + timestamp + '_ss_invalid.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC20', 'invalid')
    def test_invalid_user_only(self):

        # Invalid Username only
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(invalid_credentials.get('invalid_username'),
                               admin_credential.get('passw'))
        login_admin.click_button_invalid_user()

        sss_name = ss_folder + timestamp + '_ss_invalid_useronly.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC21', 'invalid')
    def test_invalid_passw_only(self):

        # Invalid Password only
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(admin_credential.get('user'),
                               invalid_credentials.get('invalid_password'))
        login_admin.click_button_invalid_user()

        sss_name = ss_folder + timestamp + '_ss_invalid_passwonly.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC22', 'invalid')
    def test_invalid_blank(self):

        # Invalid Blank Login
        login_admin = LoginPage(self.driver)
        login_admin.click_button_blank()

        sss_name = ss_folder + timestamp + '_ss_invalid_blank.png'
        self.driver.save_screenshot(sss_name)


