import time
import pytest

from Utilities.config import ss_folder
from Utilities.config import timestamp
from Utilities.data import username_entry_admin
from Utilities.data import add_candidate_data
from Utilities.data import add_candidate_details
from Utilities.data import search_cand_data
from Utilities.data import password_entry

from Pages.orangeHR_admin_PIM_add_empl import AddEmplPIM
from Pages.orangeHR_login_page import LoginPage
from Pages.orangeHR_recruitement_add_vacancy import RecAddVacancy
from Pages.orangeHR_recruitment_erase import RecDelCandidate
from Pages.orangeHR_recruitment_reject_candidate import RecRejCandidate
from Pages.orangeHR_recruitment_search_candidate import RecSearchCandidate
from Pages.orangeHR_recruitment_tag_shortlisted_and_reject import RecShortlistCandidate
from Pages.orangeHR_recuitment_hire_candidate import RecAddCandidate


@pytest.mark.usefixtures("setup")
class TestRecruitmentReject():

    @pytest.mark.tags('All', 'TS4_TC17', 'rec_reject')
    def test_login_admin_recruitment(self):

        # Login as Admin for Recruitment
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(username_entry_admin.get('username_entry_leave'),
                               password_entry.get('password_entry_one'))
        login_admin.click_button()

        sss_name = ss_folder + timestamp + '_ss_admin_login.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC18', 'rec_reject')
    def test_rej_add_candidate(self):

        # Verify Add Candidate for Reject
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

        sss_name = ss_folder + timestamp + '_ss_rej_add_candidate.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC19', 'rec_reject')
    def test_rej_search_candidate(self):

        # Verify Search Candidate for Reject
        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        sss_name = ss_folder + timestamp + '_ss_rej_search_candidate.png'
        self.driver.save_screenshot(sss_name)

    @pytest.mark.tags('All', 'TS4_TC20', 'rec_reject')
    def test_rej_tag_reject(self):

        # Verify Tag Reject Candidate
        sh_cand = RecShortlistCandidate(self.driver, self.wait)
        rej_cand = RecRejCandidate(self.driver, self.wait)
        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)
        del_cand = RecDelCandidate(self.driver, self.wait)

        sh_cand.click_eye_button()
        rej_cand.click_reject_button()
        rej_cand.click_save_reject()

        sss_name = ss_folder + timestamp + '_ss_rej_tag_reject.png'
        self.driver.save_screenshot(sss_name)

        # Delete Candidate name
        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        del_cand.click_delete_button()
        del_cand.click_confirm_delete()

        sss_name = ss_folder + timestamp + '_ss_rej_del_cand.png'
        self.driver.save_screenshot(sss_name)













'''
    @pytest.mark.rec_reject
    def test_login_admin_recruitment(self):

        # Login as Admin for Recruitment
        login_admin = LoginPage(self.driver)
        login_admin.user_entry(username_entry_admin.get('username_entry_leave'),
                               password_entry.get('password_entry_one'))
        login_admin.click_button()

        sss_name = ss_folder + timestamp + '_ss_admin_login.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

    @pytest.mark.rec_reject
    def test_rej_add_candidate(self):

        # Verify Add Candidate for Reject
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

        sss_name = ss_folder + timestamp + '_ss_rej_add_candidate.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

    @pytest.mark.rec_reject
    def test_rej_search_candidate(self):

        # Verify Search Candidate for Reject
        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        sss_name = ss_folder + timestamp + '_ss_rej_search_candidate.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

    @pytest.mark.rec_reject
    def test_rej_tag_reject(self):

        # Verify Tag Reject Candidate
        sh_cand = RecShortlistCandidate(self.driver, self.wait)
        rej_cand = RecRejCandidate(self.driver, self.wait)
        add_vacancy = RecAddVacancy(self.driver, self.wait)
        hire_add_cand = RecAddCandidate(self.driver, self.wait)
        search_cand = RecSearchCandidate(self.driver, self.wait)
        del_cand = RecDelCandidate(self.driver, self.wait)

        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        sh_cand.click_eye_button()
        rej_cand.click_reject_button()
        rej_cand.click_save_reject()

        sss_name = ss_folder + timestamp + '_ss_rej_tag_reject.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

        # Delete Candidate name
        add_vacancy.click_recruitment_button()
        hire_add_cand.click_candidate_button()
        search_cand.click_select_candidate_name(search_cand_data.get('cand_name'))
        search_cand.click_candidate_name()
        search_cand.click_search_for_candidate()

        del_cand.click_delete_button()
        del_cand.click_confirm_delete()

        sss_name = ss_folder + timestamp + '_ss_rej_del_cand.png'
        self.driver.save_screenshot(sss_name)
        time.sleep(3)

'''



