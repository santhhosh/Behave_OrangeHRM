from behave import given, when, then
from pages.Recruitment_page import RecruitmentPage
from utils.config_reader import load_config
from pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
from utils.locators import *

config = load_config()
import time

@given('the user redirecting to the login page for Recruitment Module')
def step_open_login_page(context):
    context.driver.get(config.get('DEFAULT', 'url'))
    context.login_page = LoginPage(context.driver)
    context.recruitment_page = RecruitmentPage(context.driver)
    context.locators = CommonlocatorsPage(context.driver)

@when('the user logins in with username "Admin" and password "admin123" for Recruitment Module')
def step_login_application(context):
    context.login_page.enter_username("Admin")
    time.sleep(2)
    context.login_page.enter_password("admin123")
    time.sleep(2)
    context.login_page.click_loginbutton()


#recruitment menu
@when('the user clicks on the Recruitment menu and redirects to the Recruitment page for Recruitment Module')
def step_click_menu_recruitment(context):
   context.recruitment_page.click_menu_recruitment()


#Recruitment_Candidates_form
@when('the user clicks candidates and selects "{jobtitle}","{vacancy}","{hiringmanager}","{status}","{keywords}","{fromdate}","{todate}","{methodofapplication}","{action}"')
def step_click_recruitment_candidates_form(context, jobtitle, vacancy, hiringmanager, status, keywords,
                                             fromdate, todate, methodofapplication, action):
    context.recruitment_page.click_recruitment_candidates()
    context.recruitment_page.click_recruitment_candidates_page(
        jobtitle, vacancy, hiringmanager, status, keywords, fromdate, todate, methodofapplication
    )

    if action.lower() == "save":
        context.locators.click_save()
    elif action.lower() == "cancel":
        context.locators.click_cancel()
    else:
        raise ValueError(f"Unsupported action: {action}")

#Recruitment_Candidates_addbutton
@when('the user clicks on candidates and clicks on add button and selects "{firstname}","{middlename}","{lastname}","{vacancy}","{email}","{contactnumber}","{path}","{keywords}","{fromdate}","{notes}","{action}"')
def step_recruitment_candidates_addbutton(context,firstname, middlename, lastname, vacancy, email,contactnumber,path,keywords, fromdate,
                                              notes, action):
    context.recruitment_page.click_recruitment_candidates()
    context.recruitment_page.click_recruitment_candidates_add(firstname, middlename, lastname, vacancy, email,contactnumber,path,keywords, fromdate,
                                              notes)
    if action.lower() == "save":
        context.locators.click_save()
    elif action.lower() == "cancel":
        context.locators.click_cancel()
    else:
        raise ValueError(f"Unsupported action: {action}")

#Recruitment_Candidates_list_checkbox_delete
@when('the user clicks on candidates and clicks on checkbox and clicks on alertcancel button')
def step_recruitment_candidates_list_checkbox_delete(context):
    context.recruitment_page.click_recruitment_candidates()
    context.locators.click_list_checkbox_delete()

#Recruitment_Candidates_list_delete_button
@when('the user clicks on candidates and clicks on delete button and clicks on alertcancel button')
def step_recruitment_candidates_list_checkbox_delete(context):
    context.recruitment_page.click_recruitment_candidates()
    context.locators.click_list_delete_button()

#Recruitment_Candidates_list_eye_button
@when('the user clicks on candidates and clicks on eye button')
def step_recruitment_candidates_list_eye_button(context):
    context.recruitment_page.click_recruitment_candidates()
    context.locators.click_list_eye_button()

#Recruitment_Vacancies_form
@when('the user clicks candidates and selects "{jobtitle}","{vacancy}","{hiringmanager}","{status}","{action}"')
def step_click_recruitment_vacancies_form(context, jobtitle, vacancy, hiringmanager, status, action):
    context.recruitment_page.click_recruitment_vacancies()
    context.recruitment_page.click_recruitment_vacancies_form(
        jobtitle, vacancy, hiringmanager, status
    )

    if action.lower() == "save":
        context.locators.click_save()
    elif action.lower() == "cancel":
        context.locators.click_cancel()
    else:
        raise ValueError(f"Unsupported action: {action}")