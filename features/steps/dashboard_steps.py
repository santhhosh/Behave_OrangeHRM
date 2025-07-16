from behave import given, when, then
from pages.dashboard_page import DashboardPage
from utils.config_reader import load_config
from pages.login_page import LoginPage
from utils.base_class import Baseclass

config = load_config()
import time

@given('the user redirects to the login page')
def step_open_login_page(context):
    context.driver.get(config.get('DEFAULT', 'url'))
    context.login_page = LoginPage(context.driver)
    context.dashboard_page = DashboardPage(context.driver)

@when('the user login in with username "Admin" and password "admin123"')
def step_login_application(context):
    context.login_page.enter_username("Admin")
    time.sleep(2)
    context.login_page.enter_password("admin123")
    time.sleep(2)
    context.login_page.click_loginbutton()

#Dashboard Page_Time_At_Work

@when('the user clicks on the stopwatch link')
def step_click_stopwatch(context):
    time.sleep(5)
    context.dashboard_page.click_stopwatch()

@when('the user enters note "{Note}"')
def step_enter_note(context,Note):
    time.sleep(5)
    context.dashboard_page.enter_note(Note)

@when('the user clicks on the button')
def step_click_out_in_button(context):
    time.sleep(5)
    context.dashboard_page.click_out_in_button()
    time.sleep(5)

#Dashboard Page_upgrade button
@when('click on upgrade button')
def step_click_upgrade_button(context):
    time.sleep(5)
    context.dashboard_page.click_upgrade_button()
    time.sleep(5)

@when('the user selects locale "{locale}"')
def step_click_upgrade_button_locale(context,locale):
    time.sleep(5)
    context.dashboard_page.click_upgrade_button_locale(locale)
    time.sleep(5)

@when('click on bookademo button')
def step_click_upgrade_button_bookademo(context):
    time.sleep(5)
    context.dashboard_page.click_upgrade_button_bookademo()
    time.sleep(5)

@when('the user enters firstname "{firstname}" at bookademo')
def step_click_upgrade_button_bookademo_firstname(context,firstname):
    time.sleep(5)
    context.dashboard_page.click_upgrade_button_bookademo_firstname(firstname)
    time.sleep(5)

@when('the user enters phonenumber "{phonenumber}" at bookademo')
def step_click_upgrade_button_bookademo_phonenumber(context,phonenumber):
    time.sleep(5)
    context.dashboard_page.click_upgrade_button_bookademo_phonenumber(phonenumber)
    time.sleep(5)

@when('the user enters email "{email}" at bookademo')
def step_click_upgrade_button_bookademo_email(context,email):
    time.sleep(5)
    context.dashboard_page.click_upgrade_button_bookademo_email(email)
    time.sleep(5)

@when('the user enters companyname "{companyname}" at bookademo')
def step_click_upgrade_button_bookademo_companyname(context,companyname):
    time.sleep(5)
    context.dashboard_page.click_upgrade_button_bookademo_companyname(companyname)
    time.sleep(5)


@when('the user selects country "{country}" at bookademo')
def step_click_upgrade_button_bookademo_country(context,country):
    time.sleep(5)
    context.dashboard_page.click_upgrade_button_bookademo_country(country)
    time.sleep(5)

@when('the user clicks submit button at bookademo')
def step_click_upgrade_button_bookademo_submit(context):
    time.sleep(5)
    context.dashboard_page.click_upgrade_button_bookademo_submit()
    time.sleep(5)


#QuickLaunch_assignleave
@when('the user goes to quicklaunch and clicks assignleave')
def step_click_dashboard_quicklaunch_assignleave(context):
    time.sleep(2)
    context.dashboard_page.click_dashboard_quicklaunch_assignleave()
    time.sleep(2)

#QuickLaunch_leavelist
@when('the user goes to quicklaunch and clicks leavelist')
def step_click_dashboard_quicklaunch_leavelist(context):
    time.sleep(2)
    context.dashboard_page.click_dashboard_quicklaunch_leavelist()
    time.sleep(2)

#QuickLaunch_timesheets
@when('the user goes to quicklaunch and clicks timesheets')
def step_click_dashboard_quicklaunch_timesheets(context):
    time.sleep(2)
    context.dashboard_page.click_dashboard_quicklaunch_timesheets()
    time.sleep(2)

#QuickLaunch_applyleave
@when('the user goes to quicklaunch and clicks applyleave')
def step_click_dashboard_quicklaunch_applyleave(context):
    time.sleep(2)
    context.dashboard_page.click_dashboard_quicklaunch_applyleave()
    time.sleep(2)

#QuickLaunch_myleave
@when('the user goes to quicklaunch and clicks myleave')
def step_click_dashboard_quicklaunch_myleave(context):
    time.sleep(2)
    context.dashboard_page.click_dashboard_quicklaunch_myleave()
    time.sleep(2)

#QuickLaunch_mytimesheet
@when('the user goes to quicklaunch and clicks mytimesheet')
def step_click_dashboard_quicklaunch_mytimesheet(context):
    time.sleep(2)
    context.dashboard_page.click_dashboard_quicklaunch_mytimesheet()
    time.sleep(2)










