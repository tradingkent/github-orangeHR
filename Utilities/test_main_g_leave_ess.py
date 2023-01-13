import time
import pytest

from Pages.orangeHR_admin_empl_leave_entitlement import EmplLeaveEntitlement
from Utilities.config import ss_folder, timestamp
from Utilities.data import ess_fullday_leave
from Utilities.data import username_entry_ess
from Utilities.data import password_entry
from Pages.orangeHR_login_page import LoginPage
from Pages.orangeHR_ess_leave_entitlement import LeaveESSEntitlement
from Pages.orangeHR_ess_leave_via_report import LeaveESSViaReport
from Pages.orangeHR_ess_leave_apply import LeaveESSApply
from Pages.orangeHR_ess_leave_cancel import LeaveESSCancel

@pytest.mark.usefixtures("setup")
class TestLeaveESS():

    @pytest.mark.tags('All', 'TS3_TC1', 'leave_ess')
    def test_login_ess(self):

        # Login as ESS process
        login_ess = LoginPage(self.driver)
        leave_ess = LeaveESSEntitlement(self.driver, self.wait)

        login_ess.user_entry(username_entry_ess.get('username_entry'),
                             password_entry.get('password_entry_one'))
        leave_ess.click_button_ess()

        sss_name = ss_folder + timestamp + '_ss_ess_login.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS3_TC2', 'leave_ess')
    def test_leave_entitlement_ess(self):

        # Verify Leave Entitlement ESS
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        admin_leave_entitlement = EmplLeaveEntitlement(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_entitlement_ess.click_entitlements_button()
        leave_entitlement_ess.click_my_entitlements_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        admin_leave_entitlement.click_get_search_button_for_empl_entitlement()

        sss_name = ss_folder + timestamp + '_ss_ess_leave_entitlement.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS3_TC3', 'leave_ess')
    def test_leaves_via_leave_report_ess(self):

        # Verify ESS Leave via Report
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        leave_report_ess = LeaveESSViaReport(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_report_ess.click_reports_button()
        leave_report_ess.click_usage_reports()
        leave_report_ess.click_generate_reports_button_ess()

        sss_name = ss_folder + timestamp + '_ss_ess_leaves_via_leave_report.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS3_TC4', 'leave_ess')
    def test_apply_fullday_leave_ess(self):

        # Verify Apply Fullday Leave for ESS
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        leave_apply = LeaveESSApply(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_apply.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        leave_apply.click_from_date(ess_fullday_leave.get('fromdate'))
        leave_apply.click_to_date(ess_fullday_leave.get('todate'))
        leave_apply.click_apply_leave_for_fullday()

        sss_name = ss_folder + timestamp + '_ss_ess_apply_fullday_leave.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS3_TC5', 'leave_ess')
    def test_apply_halfday_morning_leave_ess(self):

        # Verify Apply Halfday Morning Leave for ESS
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

        sss_name = ss_folder + timestamp + '_ss_ess_apply_halfday_morning.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS3_TC6', 'leave_ess')
    def test_apply_halfday_afternoon_leave_ess(self):

        # Verify Apply Halfday Afternoon Leave for ESS
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

        sss_name = ss_folder + timestamp + '_ss_ess_apply_halfday_afternoon.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS3_TC7', 'leave_ess')
    def test_apply_specify_time_leave_ess(self):

        # Verify Apply for Specify Time Leave for ESS
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
        leave_apply.click_apply_leave_for_specify_time_ess()

        sss_name = ss_folder + timestamp + '_ss_ess_apply_specify_time_leave.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS3_TC8', 'leave_ess')
    def test_apply_specify_time_leave_ess_again(self):

        # Verify Apply for Specify Time Leave for ESS
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        leave_apply = LeaveESSApply(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_apply.click_apply_button()
        leave_entitlement_ess.click_drp_leave_type()
        leave_entitlement_ess.click_leave_type_bereavement()
        leave_apply.click_from_date(ess_fullday_leave.get('spe_ag_time_fromdate'))
        leave_apply.click_to_date(ess_fullday_leave.get('spe_ag_time_todate'))
        leave_apply.click_drp_duration()
        leave_apply.click_specify_time()
        leave_apply.click_specify_time_clock_one()
        leave_apply.click_specify_time_hhmm_one(ess_fullday_leave.get('start_time'))
        leave_apply.click_specify_time_clock_two()
        leave_apply.click_specify_time_hhmm_two(ess_fullday_leave.get('end_time'))
        leave_apply.click_apply_leave_for_specify_time_again()

        sss_name = ss_folder + timestamp + '_ss_ess_apply_specify_time_leave.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS3_TC9', 'leave_ess')
    def test_cancel_leave_for_ess(self):

        # Verify Cancel Leave for ESS
        leave_entitlement_ess = LeaveESSEntitlement(self.driver, self.wait)
        leave_cancel = LeaveESSCancel(self.driver, self.wait)

        leave_entitlement_ess.click_leave_button()
        leave_cancel.click_my_leave_button()
        leave_cancel.click_search_button()
        leave_cancel.scroll_page_end()
        leave_cancel.click_cancel_button()
        leave_cancel.cancel_verify_ess()

        sss_name = ss_folder + timestamp + '_ss_ess_cancel_leave.png'
        self.driver.save_screenshot(sss_name)









