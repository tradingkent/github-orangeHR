import time
import pytest

from Utilities.data import admin_credential
from Utilities.config import ss_folder
from Utilities.config import timestamp

from Pages.orangeHR_admin_page import AddUser
from Pages.orangeHR_login_page import LoginPage
from Pages.orangeHR_ess_sort import SortUsernameESS


@pytest.mark.usefixtures("setup")
class TestSort():

    @pytest.mark.tags('All', 'TS1_TC14', 'sort')
    def test_login_admin_sort(self):

        # Login as Admin process
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(admin_credential.get('user'),
                               admin_credential.get('passw'))
        login_admin.click_button()

        sss_name = ss_folder + timestamp + '_ss_admin_login.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC15', 'sort')
    def test_sort_ascending(self):

        # Sort Ascending
        sort_ascending = AddUser(self.driver, self.wait)
        sort_username = SortUsernameESS(self.driver, self.wait)

        sort_ascending.click_admin_button()
        sort_username.click_search_button_sort()
        sort_username.click_sort_button()
        sort_username.click_ascending_button()

        sss_name = ss_folder + timestamp + '_ss_sort_ascending.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS1_TC16', 'sort')
    def test_sort_descending(self):

        # Sort Descending
        sort_ascending = AddUser(self.driver, self.wait)
        sort_username = SortUsernameESS(self.driver, self.wait)

        sort_ascending.click_admin_button()
        sort_username.click_search_button_sort()
        sort_username.click_sort_button()
        sort_username.click_descending_button()

        sss_name = ss_folder + timestamp + '_ss_sort_descending.png'
        self.driver.save_screenshot(sss_name)


# sample comment by Tester 1 for git push and Jenkins run setup