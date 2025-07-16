from behave import given, when, then
from pages.admin_page import AdminPage
from utils.config_reader import load_config
from pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains

config = load_config()
import time

@given('the user redirecting to the login page for Admin Module')
def step_open_login_page(context):
    context.driver.get(config.get('DEFAULT', 'url'))
    context.login_page = LoginPage(context.driver)
    context.admin_page = AdminPage(context.driver)

@when('the user logins in with username "Admin" and password "admin123" for Admin Module')
def step_login_application(context):
    context.login_page.enter_username("Admin")
    time.sleep(2)
    context.login_page.enter_password("admin123")
    time.sleep(2)
    context.login_page.click_loginbutton()

@when('the user clicks on the Admin menu and redirects to the Admin page for Admin Module')
def step_click_menu_admin(context):
    context.admin_page.click_menu_admin()


#UserManagement
#Users
"""@when('the user clicks on usermanagement for users')
def step_click_admin_usermanagement_users(context):
    context.admin_page.click_admin_usermanagement_users()"""

#Users_add
@when('the user clicks on usermanagement for users and clicks add and enters "{userrole}","{employeename}","{status}","{username}","{password}","{confirmpassword}"')
def step_click_admin_usermanagement_users_add(context,userrole,employeename,status,username,password,confirmpassword):
    context.admin_page.click_admin_usermanagement_users()
    context.admin_page.click_admin_usermanagement_users_add(userrole,employeename,status,username,password,confirmpassword)

#Systemusers
@when('the user clicks on usermanagement for users and search and enters "{username}","{userrole}","{employeename}","{status}"')
def step_click_admin_usermanagement_users_systemusers(context,username,userrole, employeename, status):
    context.admin_page.click_admin_usermanagement_users()
    context.admin_page.click_admin_usermanagement_users_systemusers(username,userrole, employeename, status)

#Job_JobTitles
#JobTitles_add_save
@when('the user clicks on job for jobtitles and enters "{jobtitle}","{jobdescription}","{note}" and save')
def step_click_admin_job_jobtitles(context,jobtitle,jobdescription,note):
    context.admin_page.click_admin_job()
    context.admin_page.click_admin_job_jobtitles_add(jobtitle,jobdescription,note)
    context.admin_page.click_admin_job_jobtitles_save_cancel("save")

#JobTitles_add_cancel
@when('the user clicks on job for jobtitles and enters "{jobtitle}","{jobdescription}","{note}" and cancel')
def step_click_admin_job_jobtitles(context,jobtitle,jobdescription,note):
    context.admin_page.click_admin_job()
    context.admin_page.click_admin_job_jobtitles_add(jobtitle,jobdescription,note)
    context.admin_page.click_admin_job_jobtitles_save_cancel("cancel")

#PayGrades_add
#PayGrades_add_save
@when('the user clicks on job for paygrades and enters "{name}" and clicks on save button')
def step_click_admin_job_paygrades(context,name):
    context.admin_page.click_admin_job()
    context.admin_page.click_admin_job_paygrades()
    context.admin_page.click_admin_job_paygrades_add(name)
    context.admin_page.click_admin_job_paygrades_add_save_cancel("save")

#PayGrades_add_cancel
@when('the user clicks on job for paygrades and enters "{name}" and clicks on cancel button')
def step_click_admin_job_paygrades(context,name):
    context.admin_page.click_admin_job()
    context.admin_page.click_admin_job_paygrades()
    context.admin_page.click_admin_job_paygrades_add(name)
    context.admin_page.click_admin_job_paygrades_add_save_cancel("cancel")

#PayGrades_checkbox_delete
@when('the user clicks on job for paygrades and clicks on checkbox and clicks on alertcancel button')
def step_click_admin_job_paygrades_checkbox_delete(context):
    context.admin_page.click_admin_job()
    context.admin_page.click_admin_job_paygrades()
    context.admin_page.click_admin_job_paygrades_checkbox_delete()

#PayGrades_list_deletebutton
@when('the user clicks on job for paygrades and clicks on deletebutton of list and clicks on alertcancel button')
def step_click_admin_job_paygrades_checkbox_delete(context):
    context.admin_page.click_admin_job()
    context.admin_page.click_admin_job_paygrades()
    context.admin_page.click_admin_job_paygrades_list_deletebutton()

#PayGrades_list_editbutton
@when('the user clicks on job for paygrades and clicks on editbutton of list and edit "{name}" and clicks on save button')
def step_click_admin_job_paygrades_checkbox_delete(context,name):
    context.admin_page.click_admin_job()
    context.admin_page.click_admin_job_paygrades()
    context.admin_page.click_admin_job_paygrades_list_editbutton(name)
    context.admin_page.click_admin_job_paygrades_add_save_cancel("save")




#employmentstatus_add
#employmentstatus_add_save
@when('the user clicks on job for employmentstatus and enters "{name}" and clicks on save button')
def step_click_admin_job_employmentstatus(context,name):
    context.admin_page.click_admin_job()
    context.admin_page.admin_job_employmentstatus_add(name)
    context.admin_page.click_admin_job_employmentstatus_add_save_cancel("save")

#employmentstatus_add_cancel
@when('the user clicks on job for employmentstatus and enters "{name}" and clicks on cancel button')
def step_click_admin_job_employmentstatus(context,name):
    context.admin_page.click_admin_job()
    context.admin_page.admin_job_employmentstatus_add(name)
    context.admin_page.click_admin_job_employmentstatus_add_save_cancel("cancel")

#JobCategories_add
#JobCategories_add_save
@when('the user clicks on job for jobcategories and enters "{name}" and clicks on save button')
def step_click_admin_job_jobcategories(context,name):
    context.admin_page.click_admin_job()
    context.admin_page.admin_job_jobcategories_add(name)
    context.admin_page.click_admin_job_jobcategories_add_save_cancel("save")

#JobCategories_add_cancel
@when('the user clicks on job for jobcategories and enters "{name}" and clicks on cancel button')
def step_click_admin_job_jobcategories(context,name):
    context.admin_page.click_admin_job()
    context.admin_page.admin_job_jobcategories_add(name)
    context.admin_page.click_admin_job_jobcategories_add_save_cancel("cancel")

#Job_workshifts_add_save
@when('the user clicks on job for workshifts and enters "{shiftname}","{fromtime}","{totime}","{assignedemployees}" and clicks on save button')
def step_click_admin_job_workshifts_add_save(context,shiftname,fromtime,totime,assignedemployees):
    context.admin_page.click_admin_job()
    context.admin_page.admin_job_workshifts()
    context.admin_page.admin_job_workshifts_add(shiftname,fromtime,totime,assignedemployees)
    context.admin_page.admin_job_workshifts_add_save()

#Job_workshifts_add_cancel
@when('the user clicks on job for workshifts and enters "{shiftname}","{fromtime}","{totime}","{assignedemployees}" and clicks on cancel button')
def step_click_admin_job_workshifts_add_save(context,shiftname,fromtime,totime,assignedemployees):
    context.admin_page.click_admin_job()
    context.admin_page.admin_job_workshifts()
    context.admin_page.admin_job_workshifts_add(shiftname,fromtime,totime,assignedemployees)
    context.admin_page.admin_job_workshifts_add_cancel()

#Job_workshifts_list_checkbox_delete
@when('the user clicks on job for workshifts and clicks on checkbox and clicks on alertcancel button')
def step_admin_job_workshifts_list_checkbox_delete(context):
    context.admin_page.click_admin_job()
    context.admin_page.admin_job_workshifts()
    context.admin_page.click_admin_job_workshifts_list_checkbox_delete()

#Job_workshifts_list_deletebutton
@when('the user clicks on job for workshifts and clicks on delete button of list and clicks on alertcancel button')
def step_click_admin_job_workshifts_list_deletebutton(context):
    context.admin_page.click_admin_job()
    context.admin_page.admin_job_workshifts()
    context.admin_page.click_admin_job_workshifts_list_deletebutton()

#Job_workshifts_list_editbutton_save
@when('the user clicks on job for workshifts and clicks on edit button of list and performs edit "{name}" and clicks on save button')
def step_click_admin_job_workshifts_list_deletebutton(context,name):
    context.admin_page.click_admin_job()
    context.admin_page.admin_job_workshifts()
    context.admin_page.click_admin_job_workshifts_list_editbutton(name)
    context.admin_page.click_admin_job_workshifts_list_editbutton_save()

#Job_workshifts_list_editbutton_cancel
@when('the user clicks on job for workshifts and clicks on edit button of list and performs edit "{name}" and clicks on cancel button')
def step_click_admin_job_workshifts_list_deletebutton(context,name):
    context.admin_page.click_admin_job()
    context.admin_page.admin_job_workshifts()
    context.admin_page.click_admin_job_workshifts_list_editbutton(name)
    context.admin_page.click_admin_job_workshifts_list_editbutton_cancel()

#Organization_Locations_Save
@when('the user clicks on organization for locations and enters "{name}","{city}","{country}" and clicks on save button')
def step_click_admin_organization_locations_save(context,name,city,country):
    context.admin_page.click_admin_organization()
    #context.admin_page.click_admin_organization_locations()
    context.admin_page.admin_organization_locations_save(name,city,country)

#Organization_Locations_Cancel
@when('the user clicks on organization for locations and enters "{name}","{city}","{country}" and clicks on cancel button')
def step_click_admin_organization_locations_cancel(context,name,city,country):
    context.admin_page.click_admin_organization()
    #context.admin_page.click_admin_organization_locations()
    context.admin_page.admin_organization_locations_reset(name,city,country)

#Organization_Locations_Add_Save
@when('the user clicks on organization for locations and enters "{name}","{city}","{state}","{postal}","{country}","{phone}","{fax}","{address}","{notes}"and clicks on save button')
def step_admin_organization_locations_add_save(context, name, city, state,postal,country,phone,fax,address,notes):
    context.admin_page.click_admin_organization()
    context.admin_page.admin_organization_locations_add(name, city, state,postal,country,phone,fax,address,notes)
    context.admin_page.admin_organization_locations_add_save()

#Organization_Locations_Add_Cancel
@when('the user clicks on organization for locations and enters "{name}","{city}","{state}","{postal}","{country}","{phone}","{fax}","{address}","{notes}"and clicks on cancel button')
def step_admin_organization_locations_add_cancel(context, name, city, state,postal,country,phone,fax,address,notes):
    context.admin_page.click_admin_organization()
    context.admin_page.admin_organization_locations_add(name, city, state,postal,country,phone,fax,address,notes)
    context.admin_page.admin_organization_locations_add_cancel()

#Organization_Locations_Cancel
@when('the user clicks on organization for locations and clicks on checkbox and clicks on alertcancel button')
def step_click_admin_organization_locations_cancel(context):
    context.admin_page.click_admin_organization()
    context.admin_page.click_admin_organization_locations_list_checkbox_delete()

#Qualifications_Skills_add_save
@when('the user clicks on qualifications for skills and enters "{name}","{description}" and clicks on save button')
def step_click_admin_qualifications_skills_add_save(context,name,description):
    context.admin_page.click_admin_qualifications_skills()
    context.admin_page.click_admin_qualifications_skills_add(name,description)
    context.admin_page.click_admin_qualifications_skills_add_save()

#Qualifications_Skills_add_cancel
@when('the user clicks on qualifications for skills and enters "{name}","{description}" and clicks on cancel button')
def step_click_admin_qualifications_skills_add_save(context,name,description):
    context.admin_page.click_admin_qualifications_skills()
    context.admin_page.click_admin_qualifications_skills_add(name,description)
    context.admin_page.click_admin_qualifications_skills_add_cancel()

#Qualifications_education_add_save
@when('the user clicks on qualifications for education and enters "{level}" and clicks on save button')
def step_click_admin_qualifications_education_add_save(context,level):
    context.admin_page.click_admin_qualifications_education()
    context.admin_page.click_admin_qualifications_education_add(level)
    context.admin_page.click_admin_qualifications_education_add_save()

#Qualifications_education_add_cancel
@when('the user clicks on qualifications for education and enters "{level}" and clicks on cancel button')
def step_click_admin_qualifications_education_add_save(context,level):
    context.admin_page.click_admin_qualifications_education()
    context.admin_page.click_admin_qualifications_education_add(level)
    context.admin_page.click_admin_qualifications_education_add_cancel()

#Qualifications_education_list_checkbox_delete
@when('the user clicks on qualifications for education and clicks on checkbox and clicks on alertcancel button')
def step_click_admin_qualifications_education_add_save(context):
    context.admin_page.click_admin_qualifications_education()
    context.admin_page.click_admin_qualifications_education_list_checkbox_delete()

#Qualifications_education_list_deletebutton
@when('the user clicks on qualifications for education and clicks on delete button of list and clicks on alertcancel button')
def step_click_admin_qualifications_education_add_save(context):
    context.admin_page.click_admin_qualifications_education()
    context.admin_page.click_admin_qualifications_education_list_deletebutton()


#Qualifications_licenses_add_save
@when('the user clicks on qualifications for licenses and enters "{name}" and clicks on save button')
def step_click_admin_qualifications_licenses_add_save(context,name):
    context.admin_page.click_admin_qualifications_licenses()
    context.admin_page.click_admin_qualifications_licenses_add(name)
    context.admin_page.click_admin_qualifications_licenses_add_save()

#Qualifications_licenses_add_cancel
@when('the user clicks on qualifications for licenses and enters "{name}" and clicks on cancel button')
def step_click_admin_qualifications_licenses_add_cancel(context,name):
    context.admin_page.click_admin_qualifications_licenses()
    context.admin_page.click_admin_qualifications_licenses_add(name)
    context.admin_page.click_admin_qualifications_licenses_add_cancel()

#Qualifications_languages_add_save
@when('the user clicks on qualifications for languages and enters "{name}" and clicks on save button')
def step_click_admin_qualifications_languages_add_save(context,name):
    context.admin_page.click_admin_qualifications_languages()
    context.admin_page.click_admin_qualifications_languages_add(name)
    context.admin_page.click_admin_qualifications_languages_add_save()

#Qualifications_languages_add_cancel
@when('the user clicks on qualifications for languages and enters "{name}" and clicks on cancel button')
def step_click_admin_qualifications_languages_add_cancel(context,name):
    context.admin_page.click_admin_qualifications_languages()
    context.admin_page.click_admin_qualifications_languages_add(name)
    context.admin_page.click_admin_qualifications_languages_add_cancel()

#Qualifications_memberships_add_save
@when('the user clicks on qualifications for memberships and enters "{name}" and clicks on save button')
def step_click_admin_qualifications_memberships_add_save(context,name):
    context.admin_page.click_admin_qualifications_memberships()
    context.admin_page.click_admin_qualifications_memberships_add(name)
    context.admin_page.click_admin_qualifications_memberships_add_save()

#Qualifications_memberships_add_cancel
@when('the user clicks on qualifications for memberships and enters "{name}" and clicks on cancel button')
def step_click_admin_qualifications_memberships_add_cancel(context,name):
    context.admin_page.click_admin_qualifications_memberships()
    context.admin_page.click_admin_qualifications_memberships_add(name)
    context.admin_page.click_admin_qualifications_memberships_add_cancel()

"""#myinfo_download
@when('the user clicks on myinfo and clicks on download button')
def step_click_myinfo_download(context):
    context.admin_page.click_myinfo_download()"""


#Nationalities_add_save
@when('the user clicks on nationalities and enters "{name}" and clicks on save button')
def step_click_admin_nationalities_add_save(context,name):
    context.admin_page.click_admin_nationalities()
    context.admin_page.click_admin_nationalities_add(name)
    context.admin_page.click_admin_nationalities_add_save()

#Nationalities_add_cancel
@when('the user clicks on nationalities and enters "{name}" and clicks on cancel button')
def step_click_admin_nationalities_add_save(context,name):
    context.admin_page.click_admin_nationalities()
    context.admin_page.click_admin_nationalities_add(name)
    context.admin_page.click_admin_nationalities_add_cancel()

#Nationalities_list_checkbox_delete
@when('the user clicks on nationalities and clicks on checkbox and clicks on alertcancel button')
def step_click_admin_nationalities_add_save(context):
    context.admin_page.click_admin_nationalities()
    context.admin_page.click_admin_nationalities_list_checkbox_delete()

#Nationalities_list_delete
@when('the user clicks on nationalities and clicks on delete button of list and clicks on alertcancel button')
def step_click_admin_nationalities_list_deletebutton(context):
    context.admin_page.click_admin_nationalities()
    context.admin_page.click_admin_nationalities_list_deletebutton()

#Nationalities_list_editbutton_save
@when('the user clicks on nationalities and clicks on edit button of list and performs edit "{name}" and clicks on save button')
def step_click_admin_nationalities_list_editbutton_save(context,name):
    context.admin_page.click_admin_nationalities()
    context.admin_page.click_admin_nationalities_list_editbutton(name)
    context.admin_page.click_admin_nationalities_add_save()

#Nationalities_list_editbutton_cancel
@when('the user clicks on nationalities and clicks on edit button of list and performs edit "{name}" and clicks on cancel button')
def step_click_admin_nationalities_list_editbutton_cancel(context,name):
    context.admin_page.click_admin_nationalities()
    context.admin_page.click_admin_nationalities_list_editbutton(name)
    context.admin_page.click_admin_nationalities_add_cancel()



