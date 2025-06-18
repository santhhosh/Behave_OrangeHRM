from behave import given, when, then
from pages.pim_page import PIMPage
from utils.config_reader import load_config
from pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains

config = load_config()
import time

@given('the user redirecting to the login page')
def step_open_login_page(context):
    context.driver.get(config.get('DEFAULT', 'url'))
    context.login_page = LoginPage(context.driver)
    context.pim_page = PIMPage(context.driver)

@when('the user logins in with username "Admin" and password "admin123"')
def step_login_application(context):
    context.login_page.enter_username("Admin")
    time.sleep(2)
    context.login_page.enter_password("admin123")
    time.sleep(2)
    context.login_page.click_loginbutton()

@when('the user clicks on the PIM menu and redirects to the PIM page')
def step_click_menu_pim(context):
    time.sleep(5)
    context.pim_page.click_menu_pim()
    time.sleep(5)
#addemployee
@when('the user clicks on Addemployee')
def step_click_pim_addemployee(context):
    time.sleep(5)
    context.pim_page.click_pim_addemployee()
    time.sleep(5)

@when('the user enters firstname "{Firstname}"')
def step_enter_pim_addemployee_firstname(context,Firstname):
    time.sleep(5)
    context.pim_page.enter_pim_addemployee_firstname(Firstname)
    time.sleep(5)

@when('the user enters middlename "{Middlename}"')
def step_enter_pim_addemployee_middlename(context,Middlename):
    time.sleep(5)
    context.pim_page.enter_pim_addemployee_middlename(Middlename)
    time.sleep(5)

@when('the user enters lastname "{Lastname}"')
def step_enter_pim_addemployee_lastname(context,Lastname):
    time.sleep(5)
    context.pim_page.enter_pim_addemployee_lastname(Lastname)
    time.sleep(5)

@when('the user enters the employeeid "{Employeeid}"')
def step_enter_pim_addemployee_employeeid(context,Employeeid):
    #time.sleep(5)
    context.pim_page.enter_pim_addemployee_employeeid(Employeeid)
    time.sleep(5)

@when('the user uploads file')
def step_enter_pim_addemployee_fileuploadbutton(context):
    time.sleep(5)
    context.pim_page.enter_pim_addemployee_fileuploadbutton()
    time.sleep(5)

@when('the user clicks on the save button')
def step_click_pim_addemployee_savebutton(context):
    #time.sleep(5)
    context.pim_page.click_pim_addemployee_savebutton()
    time.sleep(5)

#reports
@when('the user clicks on Reports')
def step_click_pim_reports(context):
    time.sleep(5)
    context.pim_page.click_pim_reports()
    time.sleep(5)

@when('the user enters reportname "{ReportName}" of Reports')
def step_enter_pim_reports_reportname(context,ReportName):
    time.sleep(5)
    context.pim_page.enter_pim_reports_reportname(ReportName)
    time.sleep(5)

@when('the user clicks on the search button of Reports')
def step_click_pim_reports_search_button(context):
    time.sleep(5)
    context.pim_page.click_pim_reports_search_button()
    time.sleep(5)