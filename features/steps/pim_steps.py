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

#Configuration_CustomFields_save
@when('the user clicks on configuration for CustomFields and enters "{fieldname}","{screen}","{type}" and clicks on save button')
def step_click_pim_configuration_customfields_save(context,fieldname,screen,type):
    context.pim_page.click_pim_configuration()
    context.pim_page.click_pim_configuration_customfields()
    context.pim_page.click_pim_configuration_customfields_add(fieldname,screen,type)
    context.pim_page.click_pim_save()

#Configuration_CustomFields_cancel
@when('the user clicks on configuration for CustomFields and enters "{fieldname}","{screen}","{type}" and clicks on cancel button')
def step_click_pim_configuration_customfields_cancel(context,fieldname,screen,type):
    context.pim_page.click_pim_configuration()
    context.pim_page.click_pim_configuration_customfields()
    context.pim_page.click_pim_configuration_customfields_add(fieldname,screen,type)
    context.pim_page.click_pim_cancel()



#Configuration_CustomFields_list_checkbox_delete
@when('the user clicks on configuration for customfields and clicks on checkbox and clicks on alertcancel button')
def step_click_pim_customfields_list_checkbox_delete(context):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_customfields()
   context.pim_page.click_pim_list_checkbox_delete()

#Configuration_CustomFields_list_deletebutton
@when('the user clicks on configuration for customfields and clicks on delete button of list and clicks on alertcancel button')
def step_click_pim_customfields_list_deletebutton(context):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_customfields()
   context.pim_page.click_pim_list_deletebutton()

#Configuration_CustomFields_list_editbutton_save
@when('the user clicks on configuration for customfields and clicks on edit button of list and performs edit "{name}" and clicks on save button')
def step_click_pim_customfields_list_editbutton_save(context,name):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_customfields()
   context.pim_page.click_pim_list_edit_button(name)
   context.pim_page.click_pim_save()


#Configuration_CustomFields_list_editbutton_cancel
@when('the user clicks on configuration for customfields and clicks on edit button of list and performs edit "{name}" and clicks on cancel button')
def step_click_pim_customfields_list_editbutton_cancel(context,name):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_customfields()
   context.pim_page.click_pim_list_edit_button(name)
   context.pim_page.click_pim_cancel()







#DataImport
@when('the user clicks on configuration for dataimport and uploads file')
def step_click_pim_configuration_dataimport(context):
    context.pim_page.click_pim_configuration()
    context.pim_page.click_pim_configuration_dataimport()

#ReportingMethods_save
@when('the user clicks on configuration for reportingmethods and enters "{name}" and clicks on save button')
def step_click_pim_configuration_reportingmethods_save(context,name):
    context.pim_page.click_pim_configuration()
    context.pim_page.click_pim_configuration_reportingmethods()
    context.pim_page.click_pim_configuration_reportingmethods_add(name)
    context.pim_page.click_pim_save()

#ReportingMethods_cancel
@when('the user clicks on configuration for reportingmethods and enters "{name}" and clicks on cancel button')
def step_click_pim_configuration_reportingmethods_cancel(context,name):
    context.pim_page.click_pim_configuration()
    context.pim_page.click_pim_configuration_reportingmethods()
    context.pim_page.click_pim_configuration_reportingmethods_add(name)
    context.pim_page.click_pim_cancel()

#Configuration_ReportingMethods_list_checkbox_delete
@when('the user clicks on configuration for reportingmethods and clicks on checkbox and clicks on alertcancel button')
def step_click_pim_reportingmethods_list_checkbox_delete(context):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_reportingmethods()
   context.pim_page.click_pim_list_checkbox_delete()

#Configuration_ReportingMethods_list_deletebutton
@when('the user clicks on configuration for reportingmethods and clicks on delete button of list and clicks on alertcancel button')
def step_click_pim_reportingmethods_list_deletebutton(context):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_reportingmethods()
   context.pim_page.click_pim_list_deletebutton()

#Configuration_ReportingMethods_list_editbutton_save
@when('the user clicks on configuration for reportingmethods and clicks on edit button of list and performs edit "{name}" and clicks on save button')
def step_click_pim_reportingmethods_list_editbutton_save(context,name):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_reportingmethods()
   context.pim_page.click_pim_list_edit_button(name)
   context.pim_page.click_pim_save()


#Configuration_ReportingMethods_list_editbutton_cancel
@when('the user clicks on configuration for reportingmethods and clicks on edit button of list and performs edit "{name}" and clicks on cancel button')
def step_click_pim_reportingmethods_list_editbutton_cancel(context,name):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_reportingmethods()
   context.pim_page.click_pim_list_edit_button(name)
   context.pim_page.click_pim_cancel()

#TerminationReasons_save
@when('the user clicks on configuration for terminationreasons and enters "{name}" and clicks on save button')
def step_click_pim_configuration_terminationreasons_save(context,name):
    context.pim_page.click_pim_configuration()
    context.pim_page.click_pim_configuration_terminationreasons()
    context.pim_page.click_pim_configuration_terminationreasons_add(name)
    context.pim_page.click_pim_save()

#TerminationReasons_cancel
@when('the user clicks on configuration for terminationreasons and enters "{name}" and clicks on cancel button')
def step_click_pim_configuration_terminationreasons_cancel(context,name):
    context.pim_page.click_pim_configuration()
    context.pim_page.click_pim_configuration_terminationreasons()
    context.pim_page.click_pim_configuration_terminationreasons_add(name)
    context.pim_page.click_pim_cancel()

#Configuration_TerminationReasons_list_checkbox_delete
@when('the user clicks on configuration for terminationreasons and clicks on checkbox and clicks on alertcancel button')
def step_click_pim_terminationreasons_list_checkbox_delete(context):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_terminationreasons()
   context.pim_page.click_pim_list_checkbox_delete()

#Configuration_TerminationReasons_list_deletebutton
@when('the user clicks on configuration for terminationreasons and clicks on delete button of list and clicks on alertcancel button')
def step_click_pim_terminationreasons_list_deletebutton(context):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_terminationreasons()
   context.pim_page.click_pim_list_deletebutton()

#Configuration_TerminationReasons_list_editbutton_save
@when('the user clicks on configuration for terminationreasons and clicks on edit button of list and performs edit "{name}" and clicks on save button')
def step_click_pim_terminationreasons_list_editbutton_save(context,name):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_terminationreasons()
   context.pim_page.click_pim_list_edit_button(name)
   context.pim_page.click_pim_save()


#Configuration_TerminationReasons_list_editbutton_cancel
@when('the user clicks on configuration for terminationreasons and clicks on edit button of list and performs edit "{name}" and clicks on cancel button')
def step_click_pim_terminationreasons_list_editbutton_cancel(context,name):
   context.pim_page.click_pim_configuration()
   context.pim_page.click_pim_configuration_terminationreasons()
   context.pim_page.click_pim_list_edit_button(name)
   context.pim_page.click_pim_cancel()







#employeelist_save
@when('the user clicks on employeelist and enters "{employeename}","{employeeid}","{employmentstatus}","{include}","{supervisorname}","{jobtitle}","{subunit}" clicks on save button')
def step_click_pim_employeelist_save(context,employeename,employeeid,employmentstatus,include,supervisorname,jobtitle,subunit):
    context.pim_page.click_pim_employeelist()
    context.pim_page.click_pim_employeelist_search(employeename,employeeid,employmentstatus,include,supervisorname,jobtitle,subunit)
    context.pim_page.click_pim_save()

#employeelist_cancel
@when('the user clicks on employeelist and enters "{employeename}","{employeeid}","{employmentstatus}","{include}","{supervisorname}","{jobtitle}","{subunit}" clicks on cancel button')
def step_click_pim_employeelist_save(context,employeename,employeeid,employmentstatus,include,supervisorname,jobtitle,subunit):
    context.pim_page.click_pim_employeelist()
    context.pim_page.click_pim_employeelist_search(employeename,employeeid,employmentstatus,include,supervisorname,jobtitle,subunit)
    context.pim_page.click_pim_cancel()

#employeelist_list_checkbox_delete
@when('the user clicks on employeelist and clicks on checkbox and clicks on alertcancel button')
def step_click_pim_employeelist_list_checkbox_delete(context):
   context.pim_page.click_pim_employeelist()
   context.pim_page.click_pim_list_checkbox_delete()

#employeelist_list_deletebutton
@when('the user clicks on employeelist and clicks on delete button of list and clicks on alertcancel button')
def step_click_pim_employeelist_list_checkbox_delete(context):
   context.pim_page.click_pim_employeelist()
   context.pim_page.click_pim_list_deletebutton()

"""#employeelist_list_editbutton_save
@when('the user clicks on employeelist and clicks on edit button of list and performs edit "{name}" and clicks on save button')
def step_click_pim_employeelist_list_editbutton_save(context,name):
   context.pim_page.click_pim_employeelist()
   context.pim_page.click_pim_list_editbutton(name)
   context.pim_page.click_pim_save()

#employeelist_list_editbutton_cancel
@when('the user clicks on employeelist and clicks on edit button of list and performs edit "{name}" and clicks on cancel button')
def step_click_pim_employeelist_list_editbutton_cancel(context,name):
   context.pim_page.click_pim_employeelist()
   context.pim_page.click_pim_list_editbutton(name)
   context.pim_page.click_pim_cancel()"""



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

#reports_save
@when('the user clicks on reports enters "{ReportName}" and clicks on the save button')
def step_click_pim_reports_save(context,ReportName):
   context.pim_page.click_pim_reports()
   context.pim_page.click_pim_reports_reportname(ReportName)
   context.pim_page.click_pim_save()

#reports_cancel
@when('the user clicks on reports enters "<ReportName>" and clicks on the cancel button')
def step_click_pim_reports_save(context,ReportName):
   context.pim_page.click_pim_reports()
   context.pim_page.click_pim_reports_reportname(ReportName)
   context.pim_page.click_pim_cancel()

#reports_add_save
@when('the user clicks on reports and click on add button enters "{reportname}","{selectioncriteria}","{include}","{displayfieldgroup}","{displayfield}" and clicks on the save button')
def step_click_pim_reports_add_save(context,reportname,selectioncriteria,include,displayfieldgroup,displayfield):
   context.pim_page.click_pim_reports()
   context.pim_page.click_pim_reports_add(reportname,selectioncriteria,include,displayfieldgroup,displayfield)
   context.pim_page.click_pim_save()

#reports_add_cancel
@when('the user clicks on reports and click on add button enters "{reportname}","{selectioncriteria}","{include}","{displayfieldgroup}","{displayfield}" and clicks on the cancel button')
def step_click_pim_reports_add_cancel(context,reportname,selectioncriteria,include,displayfieldgroup,displayfield):
   context.pim_page.click_pim_reports()
   context.pim_page.click_pim_reports_add(reportname,selectioncriteria,include,displayfieldgroup,displayfield)
   context.pim_page.click_pim_cancel()

#reports_list_checkbox_delete
@when('the user clicks on reports and clicks on checkbox and clicks on alertcancel button')
def step_click_pim_reports_list_checkbox_delete(context):
   context.pim_page.click_pim_reports()
   context.pim_page.click_pim_list_checkbox_delete()

#reports_list_deletebutton
@when('the user clicks on reports and clicks on delete button of list and clicks on alertcancel button')
def step_click_pim_reports_list_checkbox_delete(context):
   context.pim_page.click_pim_reports()
   context.pim_page.click_pim_list_deletebutton()

#reports_list_editbutton_save
@when('the user clicks on reports and clicks on edit button of list and performs edit "{name}" and clicks on save button')
def step_click_pim_reports_list_editbutton_save(context,name):
   context.pim_page.click_pim_reports()
   context.pim_page.click_pim_list_editbutton(name)
   context.pim_page.click_pim_save()

#reports_list_editbutton_cancel
@when('the user clicks on reports and clicks on edit button of list and performs edit "{name}" and clicks on cancel button')
def step_click_pim_reports_list_editbutton_cancel(context,name):
   context.pim_page.click_pim_reports()
   context.pim_page.click_pim_list_editbutton(name)
   context.pim_page.click_pim_cancel()

#reports_list_textfill
@when('the user clicks on reports and clicks on textfill button of list')
def step_click_pim_reports_list_editbutton_cancel(context):
   context.pim_page.click_pim_reports()
   context.pim_page.click_pim_list_textfill()








"""@when('the user enters reportname "{ReportName}" of Reports')
def step_enter_pim_reports_reportname(context,ReportName):
    time.sleep(5)
    context.pim_page.enter_pim_reports_reportname(ReportName)
    time.sleep(5)

@when('the user clicks on the search button of Reports')
def step_click_pim_reports_search_button(context):
    time.sleep(5)
    context.pim_page.click_pim_reports_search_button()
    time.sleep(5)"""