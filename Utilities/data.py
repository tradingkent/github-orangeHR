# Admin Credential for Login
admin_credential = {'user': 'Admin',
                    'passw': 'admin123'}

# PIM Add Users

first_empl = {'firstname': 'Tyrion',
              'lastname': 'Lannister'}

sec_empl = {'firstname': 'Jon',
            'lastname': 'Snow'}

third_empl = {'firstname': 'Daenerys',
              'lastname': 'Targaryen'}

fourth_empl = {'firstname': 'Robert',
               'lastname': 'Baratheon'}

fifth_empl = {'firstname': 'Night',
              'lastname': 'King',
              'uname': 'Night_testyyy',
              'newfname': 'White',
              'newlname': 'Walker'}

sixth_empl = {'firstname': 'Ned',
              'lastname': 'Stark'}


# Validation and Negative Invalid Credentials
validation_login = {'Verif': 'Admin', 'Invalid': 'Invalid credentials',
                    'Blank': 'Required', 'Acc Disabled': 'Account disabled',
                    'ESS_Verif': 'Dashboard'}

# Add User Validation
add_user_validation = {'add_user': 'Add'}

# Employee Entry Admin and Disabled
employee_entry_admin = {'employee_entry': 'Jon',
                        'employee_entry_disabled': 'Daenerys',
                        'employee_entry_leave': 'Tyrion'}

# Employee Entry ESS and Disabled
employee_entry_ess = {'employee_entry': 'Robert',
                      'employee_entry_disabled': 'Ned'}

# Username Entry for Admin and Disabled
username_entry_admin = {'username_entry': 'Jon_testyyy',
                        'username_entry_disabled': 'Daenerys_testyyy',
                        'username_entry_leave': 'Tyrion_testyyy'}

# Username Entry for ESS and Disabled
username_entry_ess = {'username_entry': 'Robert_testyyy',
                      'username_entry_disabled': 'Ned_testyyy'}

# Password Entry
password_entry = {'password_entry_one': 'Testing09*',
                  'password_entry_two': 'Testing09*'}

# New Password Entry
new_password_entry = {'new_password_entry_one': 'Testing10*',
                      'new_password_entry_two': 'Testing10*'}

# Search Entry for Admin and Disabled
search_username_entry_admin = {'username_entry': 'Jon_testyyy',
                               'username_entry_disabled': 'Daenerys_testyyy'}

## Negative Invalid Credentials ##
invalid_credentials = {'invalid_username': 'Admin0',
                       'invalid_password': 'admin1234'}

# Leave ESS
ess_credential = {'user': 'Robert_testyyy',
                  'passw': 'Testing08*'}

ess_fullday_leave = {'fromdate': '2023-02-10',
                     'todate': '2023-02-10',
                     'half_mor_fromdate': '2023-02-13',
                     'half_mor_todate': '2023-02-13',
                     'half_aft_fromdate': '2023-02-20',
                     'half_aft_todate': '2023-02-20',
                     'spe_time_fromdate': '2023-02-17',
                     'spe_time_todate': '2023-02-17',
                     'spe_ag_time_fromdate': '2023-02-21',
                     'spe_ag_time_todate': '2023-02-21',
                     'start_time': '09:00 AM',
                     'end_time': '01:00 PM'}

leave_balance_applied = {'fullday': '13.00 Day(s)',
                         'halfday_morning': '12.50 Day(s)',
                         'halfday_afternoon': '12.00 Day(s)',
                         'specify_time': '11.50 Day(s)',
                         'specify_ag_time': '11.00 Day(s)',
                         'cancel_leave': '12.00 Day(s)',
                         'cancel_leave_ess': '11.50 Day(s)'}


leave_entitlement_verif = {'leave_type': 'CAN - Bereavement',
                           'number_of_leaves': '14'}

# Leave Admin

admin_credential_leave = {'user': 'DONOTDELETE_lisa',
                          'passw': 'Testing08*'}

comment = {'comment': 'sample comment'}

assign_leave = {'fromdate': '2023-01-13', 'todate': '2023-01-13'}

entitlement_days = {'days': '14', 'days_ess': '15'}


### Recruitment ###
add_vacancy_data = {'vac_name': 'AT', 'desc_box': 'Must be good with math', 'pos_num': '6'}

add_candidate_data = {'hire_cand_fname': 'Euron', 'hire_cand_lname': 'Greyjoy'}

add_candidate_details = {'email': 'sample_email@example.com',
                         'number': '09912354316',
                         'resume': 'C:\\python-selenium\\orangeHR\\Logs\\sample_resume.pdf',
                         'keyword': 'acc, stud, oust',
                         'notes': 'this one is outstanding', 'int_title': 'AT HIRING'}

search_cand_data = {'cand_name': 'Euron'}
