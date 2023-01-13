import time
import pytest

from Utilities.data import assign_leave
from Utilities.data import entitlement_days
from Utilities.data import ess_fullday_leave
from Utilities.config import ss_folder
from Utilities.config import timestamp
from Utilities.data import employee_entry_admin
from Utilities.data import employee_entry_ess
from Utilities.data import username_entry_admin
from Utilities.data import password_entry

from Pages.orangeHR_admin_page import AddUser
from Pages.orangeHR_login_page import LoginPage
from Pages.orangeHR_admin_empl_leave_entitlement import EmplLeaveEntitlement
from Pages.orangeHR_ess_leave_cancel import LeaveESSCancel
from Pages.orangeHR_ess_leave_entitlement import LeaveESSEntitlement
from Pages.orangeHR_ess_leave_via_report import LeaveESSViaReport
from Pages.orangeHR_ess_leave_apply import LeaveESSApply
from Pages.orangeHR_admin_assign_leave import AdminLeaveAccess
from Pages.orangeHR_admin_add_leave_entitlement import AddLeave

@pytest.mark.usefixtures("setup")
class TestLeaveAccess():

    @pytest.mark.tags('All', 'TS2_TC1', 'leave_admin')
    def test_login_admin_leave_access(self):

        # Login as Admin process
        login_admin = LoginPage(self.driver)

        login_admin.user_entry(username_entry_admin.get('username_entry_leave'),
                               password_entry.get('password_entry_one'))
        login_admin.click_button()

        sss_name = ss_folder + timestamp + '_ss_admin_login.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC2', 'leave_admin')
    def test_add_self_leave_admin(self):

        # Add leave to self as an Admin
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        add_user_ess = AddUser(self.driver, self.wait)
        add_leave = AddLeave(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_entitlement_ess.click_entitlements_button()
        add_leave.click_get_add_leave()
        add_user_ess.employee_entry(employee_entry_admin.get('employee_entry_leave'))
        add_user_ess.click_empl_name_admin_for_leave()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        add_leave.click_entitlement_days(entitlement_days.get('days'))
        add_leave.click_save_button_for_add_leave()
        add_leave.click_add_leave_popup()

        sss_name = ss_folder + timestamp + '_ss_admin_add_self_leave.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC3', 'leave_admin')
    def test_leavebal_via_report(self):

        # Check Leave Balance via Report
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        leave_report_ess = LeaveESSViaReport(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_report_ess.click_reports_button()
        leave_report_ess.click_usage_reports()
        leave_report_ess.click_generate_reports_button()

        sss_name = ss_folder + timestamp + '_ss_admin_leavebal_via_report.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC4', 'leave_admin')
    def test_add_leave_entitlement_to_ess(self):

        # Add leave entitlement to ESS
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        add_user_ess = AddUser(self.driver, self.wait)
        add_leave = AddLeave(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_entitlement_ess.click_entitlements_button()
        add_leave.click_get_add_leave()
        add_user_ess.employee_entry(employee_entry_ess.get('employee_entry'))
        add_user_ess.click_empl_name_ess()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        add_leave.click_entitlement_days(entitlement_days.get('days_ess'))
        add_leave.click_save_button_for_add_leave()
        add_leave.click_add_leave_popup()

        sss_name = ss_folder + timestamp + '_ss_admin_add_leave_entitlement_to_ess.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC5', 'leave_admin')
    def test_empl_leave_entitlement(self):

        # Check employee leave entitlement
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        add_user_ess = AddUser(self.driver, self.wait)
        empl_entitlement = EmplLeaveEntitlement(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_entitlement_ess.click_entitlements_button()
        empl_entitlement.click_employee_entitlements()
        add_user_ess.employee_entry(employee_entry_ess.get('employee_entry'))
        add_user_ess.click_empl_name_ess()
        empl_entitlement.click_get_search_button_for_empl_entitlement()

        sss_name = ss_folder + timestamp + '_ss_admin_empl_leave_entitlement.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC6', 'leave_admin')
    def test_assign_leave(self):

        # Assign leave to other employee
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        add_user_ess = AddUser(self.driver, self.wait)
        leave_apply = LeaveESSApply(self.driver, self.wait)
        leave_assign = AdminLeaveAccess(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_assign.click_assign_leave_button()
        add_user_ess.employee_entry(employee_entry_ess.get('employee_entry'))
        add_user_ess.click_empl_name_ess()

        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        leave_apply.click_from_date(assign_leave.get('fromdate'))
        leave_apply.click_to_date(assign_leave.get('todate'))
        leave_assign.click_assign_button()

        sss_name = ss_folder + timestamp + '_ss_admin_assign_leave.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC7', 'leave_admin')
    def test_apply_fullday_leave_admin(self):

        # Verify Apply Full day Leave
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        leave_apply = LeaveESSApply(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_apply.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        leave_apply.click_from_date(ess_fullday_leave.get('fromdate'))
        leave_apply.click_to_date(ess_fullday_leave.get('todate'))
        leave_apply.click_apply_leave_for_fullday()

        sss_name = ss_folder + timestamp + '_ss_admin_apply_fullday_leave.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC8', 'leave_admin')
    def test_apply_halfday_morning_leave_admin(self):

        # Verify Apply Half day Morning Leave
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        leave_apply = LeaveESSApply(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_apply.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        leave_apply.click_from_date(ess_fullday_leave.get('half_mor_fromdate'))
        leave_apply.click_to_date(ess_fullday_leave.get('half_mor_todate'))
        leave_apply.click_drp_duration()
        leave_apply.click_halfday_morning()
        leave_apply.click_apply_leave_for_halfday_morning()

        sss_name = ss_folder + timestamp + '_ss_admin_halfday_morning_leave.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC9', 'leave_admin')
    def test_apply_halfday_afternoon_leave_admin(self):

        # Verify Apply Half day Afternoon Leave
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        leave_apply = LeaveESSApply(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_apply.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        leave_apply.click_from_date(ess_fullday_leave.get('half_aft_fromdate'))
        leave_apply.click_to_date(ess_fullday_leave.get('half_aft_todate'))
        leave_apply.click_drp_duration()
        leave_apply.click_halfday_afternoon()
        leave_apply.click_apply_leave_for_halfday_afternoon()

        sss_name = ss_folder + timestamp + '_ss_admin_apply_halfday_afternoon_leave.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC10', 'leave_admin')
    def test_apply_specify_time_leave_admin(self):

        # Verify Apply for Specify Time Leave
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        leave_apply = LeaveESSApply(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_apply.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        leave_apply.click_from_date(ess_fullday_leave.get('spe_time_fromdate'))
        leave_apply.click_to_date(ess_fullday_leave.get('spe_time_todate'))
        leave_apply.click_drp_duration()
        leave_apply.click_specify_time()
        leave_apply.click_specify_time_clock_one()
        leave_apply.click_specify_time_hhmm_one(ess_fullday_leave.get('start_time'))
        leave_apply.click_specify_time_clock_two()
        leave_apply.click_specify_time_hhmm_two(ess_fullday_leave.get('end_time'))
        leave_apply.click_apply_leave_for_specify_time()

        sss_name = ss_folder + timestamp + '_ss_admin_specify_time_leave.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS2_TC11', 'leave_admin')
    def test_cancel_leave_admin(self):

        # Verify Cancel Leave
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        leave_cancel = LeaveESSCancel(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_cancel.click_my_leave_button()
        leave_cancel.click_search_button()
        leave_cancel.scroll_page_end()
        leave_cancel.click_cancel_button()
        leave_cancel.cancel_verify()

        sss_name = ss_folder + timestamp + '_ss_admin_cancel_leave.png'
        self.driver.save_screenshot(sss_name)




