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

#configuration
@when('the user clicks on configuration for optionalfields')
def step_click_pim_configuration(context):
    time.sleep(5)
    context.pim_page.click_pim_configuration()
    time.sleep(5)

#OptionalFields
@when('the user clicks on optionalfields')
def step_click_pim_configuration_optionalfields(context):
    context.pim_page.click_pim_configuration_optionalfields()
    time.sleep(5)

@when('the user clicks on showdeprecatedfields of optionalfields')
def step_click_pim_configuration_optionalfields_showdeprecatedfields(context):
    context.pim_page.click_pim_configuration_optionalfields_showdeprecatedfields()
    time.sleep(5)

@when('the user clicks on ShowSSNfieldinPersonalDetails of optionalfields')
def step_click_pim_configuration_optionalfields_ShowSSNfieldinPersonalDetails(context):
    time.sleep(5)
    context.pim_page.click_pim_configuration_optionalfields_ShowSSNfieldinPersonalDetails()
    time.sleep(5)

@when('the user clicks on ShowSINfieldinPersonalDetails of optionalfields')
def step_click_pim_configuration_optionalfields_ShowSINfieldinPersonalDetails(context):
    context.pim_page.click_pim_configuration_optionalfields_ShowSINfieldinPersonalDetails()
    time.sleep(5)

@when('the user clicks on ShowUSTaxExemptionsmenu of optionalfields')
def step_click_pim_configuration_optionalfields_ShowUSTaxExemptionsmenu(context):
    context.pim_page.click_pim_configuration_optionalfields_ShowUSTaxExemptionsmenu()
    time.sleep(5)

@when('the user clicks on savebutton of optionalfields')
def step_click_pim_configuration_optionalfields_save(context):
    context.pim_page.click_pim_configuration_optionalfields_save()
    time.sleep(5)

#CustomFields
@when('the user clicks on configuration for CustomFields and enters "{fieldname}","{screen}","{type}"')
def step_click_pim_configuration_customfields(context,fieldname,screen,type):
    context.pim_page.click_pim_configuration()
    #time.sleep(5)
    context.pim_page.click_pim_configuration_customfields(fieldname,screen,type)
    #time.sleep(5)

#DataImport
@when('the user clicks on configuration for dataimport and uploads file')
def step_click_pim_configuration_dataimport(context):
    context.pim_page.click_pim_configuration()
    context.pim_page.click_pim_configuration_dataimport()

#ReportingMethods
@when('the user clicks on configuration for ReportingMethods and enters "{name}"')
def step_click_pim_configuration_reportingmethods(context,name):
    context.pim_page.click_pim_configuration()
    context.pim_page.click_pim_configuration_reportingmethods(name)

#TerminationReasons
@when('the user clicks on configuration for TerminationReasons and enters "{name}"')
def step_click_pim_configuration_terminationreasons(context,name):
    context.pim_page.click_pim_configuration()
    context.pim_page.click_pim_configuration_terminationreasons(name)


#employeelist
@when('the user clicks on EmployeeList on employeelist')
def step_click_pim_employeelist(context):
    time.sleep(5)
    context.pim_page.click_pim_employeelist()
    time.sleep(5)

@when('the user enters employeename "{employeename}" on employeelist')
def step_enter_pim_employeelist_employeename(context,employeename):
    #time.sleep(5)
    context.pim_page.enter_pim_employeelist_employeename(employeename)
    time.sleep(5)

@when('the user enters employeeid "{employeeid}" on employeelist')
def step_enter_pim_employeelist_employeeid(context,employeeid):
    #time.sleep(5)
    context.pim_page.enter_pim_employeelist_employeeid(employeeid)
    time.sleep(5)

@when('the user selects employmentstatus "{employmentstatus}" on employeelist')
def step_enter_pim_employeelist_employmentstatus(context,employmentstatus):
    #time.sleep(5)
    context.pim_page.enter_pim_employeelist_employmentstatus(employmentstatus)
    time.sleep(5)

@when('the user selects include "{include}" on employeelist')
def step_enter_pim_employeelist_include(context,include):
    #time.sleep(5)
    context.pim_page.enter_pim_employeelist_include(include)
    time.sleep(5)

@when('the user enters supervisorname "{supervisorname}" on employeelist')
def step_enter_pim_employeelist_supervisorname(context,supervisorname):
    #time.sleep(5)
    context.pim_page.enter_pim_employeelist_supervisorname(supervisorname)
    time.sleep(5)

@when('the user selects jobtitle "{jobtitle}" on employeelist')
def step_enter_pim_employeelist_jobtitle(context,jobtitle):
    #time.sleep(5)
    context.pim_page.enter_pim_employeelist_jobtitle(jobtitle)
    time.sleep(5)

@when('the user selects subunit "{subunit}" on employeelist')
def step_enter_pim_employeelist_subunit(context,subunit):
    #time.sleep(5)
    context.pim_page.enter_pim_employeelist_subunit(subunit)
    time.sleep(5)

@when('the user clicks on search button on employeelist')
def step_click_pim_employeelist_search(context):
    #time.sleep(5)
    context.pim_page.click_pim_employeelist_search()
    time.sleep(5)


#addemployee
@when('the user clicks on Addemployee')
def step_enter_pim_employeelist_include_dropdown(context):
    time.sleep(5)
    context.pim_page.enter_pim_employeelist_include_dropdown()
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