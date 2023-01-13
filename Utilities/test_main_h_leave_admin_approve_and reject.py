import time
import pytest

from Utilities.data import comment
from Utilities.data import username_entry_admin
from Utilities.data import password_entry
from Utilities.config import ss_folder
from Utilities.config import timestamp

from Pages.orangeHR_login_page import LoginPage
from Pages.orangeHR_admin_leave_list_page_access import AdminApproveReject
from Pages.orangeHR_admin_leave_list_view_details import AdminLeaveViewDetails
from Pages.orangeHR_ess_leave_entitlement import LeaveESSEntitlement


@pytest.mark.usefixtures("setup")
class TestApproveRejectLeave():

    @pytest.mark.tags('All', 'TS2_TC12', 'approve_reject')
    def test_login_admin_leave_access(self):

        # Login as Admin process
        login_admin = LoginPage(self.driver)

        login_admin.user_entry(username_entry_admin.get('username_entry_leave'),
                               password_entry.get('password_entry_one'))
        login_admin.click_button()

        sss_name = ss_folder + timestamp + '_ss_admin_login.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC13', 'approve_reject')
    def test_admin_approve_leave_comment(self):

        # Approve leave with comment
        admin_leave_page_access = AdminApproveReject(self.driver, self.wait)
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        admin_leave_page_access.click_leave_list()
        admin_leave_page_access.click_three_dots_vertical()
        admin_leave_page_access.click_add_comment()
        admin_leave_page_access.click_comment_box(comment.get('comment'))
        admin_leave_page_access.click_save_button_for_leave_comment()
        admin_leave_page_access.click_approve_button_with_comment()

        sss_name = ss_folder + timestamp + '_ss_admin_approve_leave_comment.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC14', 'approve_reject')
    def test_admin_reject_leave_no_comment(self):

        # Reject leave with no comment
        admin_leave_page_access = AdminApproveReject(self.driver, self.wait)
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        admin_leave_page_access.click_search_button()
        admin_leave_page_access.click_reject_button_no_comment()

        sss_name = ss_folder + timestamp + '_ss_admin_reject_leave_no_comment.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC15', 'approve_reject')
    def test_detail_page_access(self):

        # Check detail page access
        admin_leave_page_access = AdminApproveReject(self.driver, self.wait)
        admin_leave_view_details = AdminLeaveViewDetails(self.driver, self.wait)
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        admin_leave_page_access.click_search_button()
        admin_leave_view_details.click_leave_detail_three_dots_detail_page()
        admin_leave_view_details.click_view_leave_details()

        sss_name = ss_folder + timestamp + '_ss_admin_detail_page_access.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC16', 'approve_reject')
    def test_detail_page_approve_no_comm(self):

        # Approve leave with no comment in detail page
        admin_leave_view_details = AdminLeaveViewDetails(self.driver, self.wait)

        admin_leave_view_details.click_approve_button_no_comment()

        sss_name = ss_folder + timestamp + '_ss_admin_detail_page_approve_no_comm.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC17', 'approve_reject')
    def test_detail_page_reject_w_comm(self):

        # Reject leave with comment in detail page
        admin_leave_page_access = AdminApproveReject(self.driver, self.wait)
        admin_leave_view_details = AdminLeaveViewDetails(self.driver, self.wait)
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        admin_leave_page_access.click_search_button()
        admin_leave_view_details.click_leave_detail_three_dots_comm_reject()
        admin_leave_view_details.click_view_leave_details_comm_reject()
        admin_leave_view_details.click_rej_comm_dots_vertical()
        admin_leave_view_details.click_add_comment_button()
        admin_leave_page_access.click_comment_box(comment.get('comment'))
        admin_leave_view_details.click_save_button_reject_comment()
        admin_leave_view_details.click_reject_button_comment()

        sss_name = ss_folder + timestamp + '_ss_admin_detail_page_reject_w_comm.png'
        self.driver.save_screenshot(sss_name)








