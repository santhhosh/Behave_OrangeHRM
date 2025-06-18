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
@when('the user clicks on the upgrade button')
def step_click_upgrade_button(context):
    time.sleep(5)
    context.dashboard_page.click_upgrade_button()
    time.sleep(5)

















"""@when('the user clicks on myleave')
def step_click_myleave_item(context):
    time.sleep(5)
    context.dashboard_page.click_leave_myleave()
    time.sleep(5)

@when('the user enters FromDate "{FromDate}"')
def step_click_myleave_calendar(context,FromDate):
    #time.sleep(5)
    context.dashboard_page.click_leave_myleave_fromdate(FromDate)
    time.sleep(5)"""












"""@when('the user enters date in the calendar "{Date}"')
def step_enter_calendar(context,Date):
    time.sleep(5)
    context.dashboard_page.click_calendar(Date)

@when('the user enters hour in the time field "{Hour}"')
def step_enter_hour(context,Hour):
    time.sleep(5)
    context.dashboard_page.click_hour(Hour)

@when('the user enters minute in the time field "{Minute}"')
def step_enter_minute(context,Minute):
    time.sleep(5)
    context.dashboard_page.click_minute(Minute)

@when('the user selects time section of the day')
def step_click_ampm(context):
    time.sleep(5)
    context.dashboard_page.click_ampm()"""

































"""@when('the user click on reset button')
def step_click_leave_reset(context):
    time.sleep(5)
    context.dashboard_page.click_reset()
    time.sleep(5)


@when('the user click on apply button')
def step_click_apply(context):
    time.sleep(5)
    context.dashboard_page.click_apply()
    time.sleep(5)

@when('the user applies for leave with type, dates and comment')
def step_apply_leave(context):
    page = context.dashboard_page
    page.select_leave_type()
    page.enter_from_date("2025-06-10")
    page.enter_to_date("2025-06-10")
    page.enter_comment("Applying for test automation leave.")
    page.click_apply()

@then('the leave application should be submitted')
def step_verify_leave_submission(context):
    # Add assertion or verification based on your DOM after clicking apply
    print("Leave applied (verify manually or add assert)")

@when('the user enters from date "{FromDate}" and to date "{ToDate}"')
def step_enter_fromdate_todate(context,FromDate,ToDate):
    time.sleep(5)
    context.dashboard_page.fromdate_enter(FromDate)
    time.sleep(5)
    context.dashboard_page.todate_enter(ToDate)


@then('the user enters employee name "{EmployeeName}"')
def step_enter_leave_hintitem(context,Search):
    time.sleep(5)
    context.dashboard_page.forhints_enter(Search)
    time.sleep(5)




@then('the user clicks on the search button')
def step_click_leave_searchbutton(context):
    #time.sleep(5)
    context.dashboard_page.click_search_button()
    time.sleep(5)"""