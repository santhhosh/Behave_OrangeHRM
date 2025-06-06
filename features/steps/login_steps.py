from behave import given, when, then
from pages.login_page import LoginPage
from utils.config_reader import load_config

config = load_config()
import time

@given('the user is on the login page')
def step_open_login_page(context):
    context.driver.get(config.get('DEFAULT', 'url'))
    context.login_page = LoginPage(context.driver)

@when('the user enters username "{username}"')
def step_enter_username(context, username):
    context.login_page.enter_username(username)

@when('the user enters password "{password}"')
def step_enter_password(context, password):
    context.login_page.enter_password(password)

@when('the user clicks on the login button')
def step_click_login(context):
    context.login_page.click_loginbutton()


@then('the user must be able to login to the dashboard successfully "{expected_result}"')
def verify_dashboard_result(context,expected_result):
   try:
       time.sleep(5)
       context.login_page.verify_dashboard_1()
       #context.login_page.verify_dashboard_3()
   except:

        assert False, "Test Failed"
        if text == "Dashboard":
           assert True, "Test Passed"

# Forgot Password Steps


@when('the user clicks on the Forgot Password link')
def step_impl(context):
    context.login_page.click_forgotpassword()

@when('the user enters username "{username_1}" to reset password')
def step_impl(context, username_1):
    time.sleep(5)
    context.login_page.enter_username_forgotpassword(username_1)

@then('the user clicks on the reset password button')
def step_impl(context):

    context.login_page.click_reset_password()
    time.sleep(5)
@when('the user clicks on the "{Icon}" link')
def step_impl(context, Icon):
    if Icon.lower() == "linkedin":

        context.login_page.click_linkedin()
        time.sleep(5)
    elif Icon.lower() == "facebook":
        context.login_page.click_facebook()
        time.sleep(5)
    elif Icon.lower() == "youtube":
        context.login_page.click_youtube()
        time.sleep(5)
    elif Icon.lower() == "twitter":
        context.login_page.click_twitter()
        time.sleep(5)
    else:
        assert False, f"Unknown icon: {Icon}"
