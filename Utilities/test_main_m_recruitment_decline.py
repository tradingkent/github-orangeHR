import time
import pytest

from Utilities.config import ss_folder
from Utilities.config import timestamp
from Utilities.data import ess_fullday_leave
from Utilities.data import username_entry_admin
from Utilities.data import employee_entry_admin
from Utilities.data import add_candidate_data
from Utilities.data import add_candidate_details
from Utilities.data import search_cand_data
from Utilities.data import password_entry

from Pages.orangeHR_login_page import LoginPage
from Pages.orangeHR_ess_leave_apply import LeaveESSApply
from Pages.orangeHR_admin_PIM_add_empl import AddEmplPIM
from Pages.orangeHR_admin_page import AddUser
from Pages.orangeHR_recruitement_add_vacancy import RecAddVacancy
from Pages.orangeHR_recruitment_decline_offer import RecDeclineCandidate
from Pages.orangeHR_recruitment_erase import RecDelCandidate
from Pages.orangeHR_recruitment_interview_passed import RecPassCandidate
from Pages.orangeHR_recruitment_offer_job import RecOfferCandidate
from Pages.orangeHR_recruitment_schedule_interview import RecSchedInt
from Pages.orangeHR_recruitment_search_candidate import RecSearchCandidate
from Pages.orangeHR_recruitment_tag_shortlisted_and_reject import RecShortlistCandidate
from Pages.orangeHR_recuitment_hire_candidate import RecAddCandidate


@pytest.mark.usefixtures("setup")
class TestRecruitmentDecline():

    @pytest.mark.tags('All', 'TS4_TC21', 'rec_decline')
    def test_login_admin_recruitment(self):

        # Login as Admin for Recruitment
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(username_entry_admin.get('username_entry_leave'),
                               password_entry.get('password_entry_one'))
        login_admin.click_button()

        sss_name = ss_folder + timestamp + '_ss_admin_login.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC22', 'rec_decline')
    def test_dec_add_candidate(self):

        # Verify Hire Add Candidate
        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        add_pim = AddEmplPIM(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        add_vacancy.click_add_button_rec()
        add_pim.click_entername(add_candidate_data.get('hire_cand_fname'),
                                add_candidate_data.get('hire_cand_lname'))
        hire_add_cand.click_drp_vacancy()
        add_vacancy.click_vacancy_enter()
        hire_add_cand.click_email_box(add_candidate_details.get('email'))
        hire_add_cand.click_contact_box(add_candidate_details.get('number'))
        hire_add_cand.click_page_down()
        hire_add_cand.click_keyword_box(add_candidate_details.get('keyword'))
        hire_add_cand.click_notes_box(add_candidate_details.get('notes'))
        hire_add_cand.click_save_button_add_candidate()

        sss_name = ss_folder + timestamp + '_ss_dec_add_candidate.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC23', 'rec_decline')
    def test_dec_search_candidate(self):

        # Verify Search Candidate
        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        sss_name = ss_folder + timestamp + '_ss_dec_search_candidate.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC24', 'rec_decline')
    def test_dec_tag_shortlist(self):

        # Verify Search Candidate
        sh_cand = RecShortlistCandidate(self.driver, self.wait)

        sh_cand.click_eye_button()
        sh_cand.click_shortlist_button()
        sh_cand.click_shortlist_note(add_candidate_details.get('notes'))
        sh_cand.click_save_shortlist()

        sss_name = ss_folder + timestamp + '_ss_dec_tag_shortlist.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC25', 'rec_decline')
    def test_dec_sched_interview(self):

        # Schedule an interview
        sch_int = RecSchedInt(self.driver, self.wait)
        add_user_admin = AddUser(self.driver, self.wait)
        leave_apply = LeaveESSApply(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)

        sch_int.click_sched_button()
        sch_int.click_interview_title(add_candidate_details.get('int_title'))
        add_user_admin.employee_entry(employee_entry_admin.get('employee_entry_leave'))
        add_user_admin.click_empl_name_admin_for_leave()
        leave_apply.click_from_date(ess_fullday_leave.get('spe_time_fromdate'))
        leave_apply.click_specify_time_hhmm_one(ess_fullday_leave.get('start_time'))
        hire_add_cand.click_notes_box(add_candidate_details.get('notes'))
        sch_int.click_save_sched_int()

        sss_name = ss_folder + timestamp + '_ss_dec_sched_interview.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC26', 'rec_decline')
    def test_dec_cand_passed(self):

        # Pass Candidate
        cand_pass = RecPassCandidate(self.driver, self.wait)

        cand_pass.click_cand_pass_button()
        cand_pass.click_save_cand_pass()

        sss_name = ss_folder + timestamp + '_ss_dec_cand_passed.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC27', 'rec_decline')
    def test_dec_cand_offer_job(self):

        # Pass Candidate
        offer_cand = RecOfferCandidate(self.driver, self.wait)

        offer_cand.click_offer_job_button()
        offer_cand.click_save_button_offer_job()

        sss_name = ss_folder + timestamp + '_ss_dec_cand_offer_job.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC28', 'rec_decline')
    def test_dec_cand_decline(self):

        # Pass Candidate
        del_cand = RecDelCandidate(self.driver, self.wait)
        dec_cand = RecDeclineCandidate(self.driver, self.wait)

        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)

        dec_cand.click_offer_declined_button()
        dec_cand.click_save_decline()

        sss_name = ss_folder + timestamp + '_ss_dec_cand_decline.png'
        self.driver.save_screenshot(sss_name)

        #Delete Candidate name

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        del_cand.click_delete_button()
        del_cand.click_confirm_delete()

        sss_name = ss_folder + timestamp + '_ss_dec_del_cand.png'
        self.driver.save_screenshot(sss_name)




















'''
    @pytest.mark.rec_decline
    def test_login_admin_recruitment(self):

        # Login as Admin for Recruitment
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(username_entry_admin.get('username_entry_leave'),
                               password_entry.get('password_entry_one'))
        login_admin.click_button()

        sss_name = ss_folder + timestamp + '_ss_admin_login.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

    @pytest.mark.rec_decline
    def test_dec_add_candidate(self):

        # Verify Hire Add Candidate
        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        add_pim = AddEmplPIM(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        add_vacancy.click_add_button_rec()
        add_pim.click_entername(add_candidate_data.get('hire_cand_fname'),
                                add_candidate_data.get('hire_cand_lname'))
        hire_add_cand.click_drp_vacancy()
        add_vacancy.click_vacancy_enter()
        hire_add_cand.click_email_box(add_candidate_details.get('email'))
        hire_add_cand.click_contact_box(add_candidate_details.get('number'))
        hire_add_cand.click_page_down()
        #hire_add_cand.click_upload_resume(add_candidate_details.get('resume'))
        hire_add_cand.click_keyword_box(add_candidate_details.get('keyword'))
        hire_add_cand.click_notes_box(add_candidate_details.get('notes'))
        #hire_add_cand.click_check_box()
        hire_add_cand.click_save_button_add_candidate()

        sss_name = ss_folder + timestamp + '_ss_dec_add_candidate.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

    @pytest.mark.rec_decline
    def test_dec_search_candidate(self):

        # Verify Search Candidate
        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        sss_name = ss_folder + timestamp + '_ss_dec_search_candidate.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

    @pytest.mark.rec_decline
    def test_dec_tag_shortlist(self):

        # Verify Search Candidate
        sh_cand = RecShortlistCandidate(self.driver, self.wait)
        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        sh_cand.click_eye_button()
        sh_cand.click_shortlist_button()
        sh_cand.click_shortlist_note(add_candidate_details.get('notes'))
        sh_cand.click_save_shortlist()

        sss_name = ss_folder + timestamp + '_ss_dec_tag_shortlist.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

    @pytest.mark.rec_decline
    def test_dec_sched_interview(self):

        # Schedule an interview
        sh_cand = RecShortlistCandidate(self.driver, self.wait)
        sch_int = RecSchedInt(self.driver, self.wait)
        add_user_admin = AddUser(self.driver, self.wait)
        leave_apply = LeaveESSApply(self.driver, self.wait)

        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        sh_cand.click_eye_button()
        sch_int.click_sched_button()
        sch_int.click_interview_title(add_candidate_details.get('int_title'))
        add_user_admin.employee_entry(employee_entry_admin.get('employee_entry_leave'))
        add_user_admin.click_empl_name_admin_for_leave()
        leave_apply.click_from_date(ess_fullday_leave.get('spe_time_fromdate'))
        leave_apply.click_specify_time_hhmm_one(ess_fullday_leave.get('start_time'))
        hire_add_cand.click_notes_box(add_candidate_details.get('notes'))
        sch_int.click_save_sched_int()

        sss_name = ss_folder + timestamp + '_ss_dec_sched_interview.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

    @pytest.mark.rec_decline
    def test_dec_cand_passed(self):

        # Pass Candidate
        cand_pass = RecPassCandidate(self.driver, self.wait)
        sh_cand = RecShortlistCandidate(self.driver, self.wait)

        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        sh_cand.click_eye_button()
        cand_pass.click_cand_pass_button()
        cand_pass.click_save_cand_pass()

        sss_name = ss_folder + timestamp + '_ss_dec_cand_passed.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

    @pytest.mark.rec_decline
    def test_dec_cand_offer_job(self):

        # Pass Candidate
        sh_cand = RecShortlistCandidate(self.driver, self.wait)
        offer_cand = RecOfferCandidate(self.driver, self.wait)

        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        sh_cand.click_eye_button()
        offer_cand.click_offer_job_button()
        offer_cand.click_save_button_offer_job()

        sss_name = ss_folder + timestamp + '_ss_dec_cand_offer_job.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

    @pytest.mark.rec_decline
    def test_dec_cand_decline(self):

        # Pass Candidate
        sh_cand = RecShortlistCandidate(self.driver, self.wait)
        del_cand = RecDelCandidate(self.driver, self.wait)
        dec_cand = RecDeclineCandidate(self.driver, self.wait)

        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        sh_cand.click_eye_button()
        dec_cand.click_offer_declined_button()
        dec_cand.click_save_decline()

        sss_name = ss_folder + timestamp + '_ss_dec_cand_decline.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

        #Delete Candidate name

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        del_cand.click_delete_button()
        del_cand.click_confirm_delete()

        sss_name = ss_folder + timestamp + '_ss_dec_del_cand.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)


'''










