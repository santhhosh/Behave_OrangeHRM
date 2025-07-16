from behave import given, when, then
from pages.time_page import TimePage
from utils.config_reader import load_config
from pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains

config = load_config()
import time

@given('the user redirecting to the login page for Time Module')
def step_open_login_page(context):
    context.driver.get(config.get('DEFAULT', 'url'))
    context.login_page = LoginPage(context.driver)
    context.time_page = TimePage(context.driver)

@when('the user logins in with username "Admin" and password "admin123" for Time Module')
def step_login_application(context):
    context.login_page.enter_username("Admin")
    time.sleep(2)
    context.login_page.enter_password("admin123")
    time.sleep(2)
    context.login_page.click_loginbutton()

@when('the user clicks on the Time menu and redirects to the Time page for Time Module')
def step_click_menu_time(context):
    #time.sleep(5)
    context.time_page.click_menu_time()
    #time.sleep(5)

#TimeSheets
#MyTimeSheets
@when('the user clicks on TimeSheets for mytimesheets and enters "{timesheetperiod}" and clicks on submit button')
def step_click_time_timesheets_mytimesheets(context,timesheetperiod):
    context.time_page.click_time_timesheets()
    context.time_page.click_time_timesheets_mytimesheets(timesheetperiod)


#EmployeeTimeSheets
@when('the user clicks on TimeSheets for employeetimesheets and enters "{employeename}" and clicks on save button')
def step_click_time_timesheets_employeetimesheets(context,employeename):
    context.time_page.click_time_timesheets()
    context.time_page.click_time_timesheets_employeetimesheets(employeename)

#Attendance
#MyRecords
@when('the user clicks on attendance for myrecords and enters "{date}" and clicks on view button')
def step_click_time_attendance_myrecords(context, date):
    context.time_page.click_time_attendance()
    context.time_page.click_time_attendance_myrecords(date)

    #def step_click_time_attendance_pencilbutton(context):
     #context.time_page.click_time_attendance_pencilbutton()

#PunchIn/Out
"""@when('the user clicks on attendance for PunchIn/Out and enters "{date}","{hour}","{minute}","{note}"and clicks on submit button')
def step_click_time_attendance_Punchinout(context, date,hour,minute,note):
    context.time_page.click_time_attendance()
    context.time_page.click_time_attendance_Punchinout(date,hour,minute,note)"""

@when('the user clicks on attendance for PunchIn/Out and enters "{date}","{note}"and clicks on submit button')
def step_click_time_attendance_Punchinout(context, date,note):
    context.time_page.click_time_attendance()
    context.time_page.click_time_attendance_Punchinout(date,note)

#EmployeeRecords
@when('the user clicks on attendance for EmployeeRecords and enters "{employeename}","{date}"and clicks on view button')
def step_click_time_attendance_employeerecords(context, employeename,date):
    context.time_page.click_time_attendance()
    context.time_page.click_time_attendance_employeerecords(employeename,date)

#Configuration
@when('the user clicks on attendance for Configuration and clicks on save button')
def step_click_time_attendance_configuration(context):
    context.time_page.click_time_attendance()
    context.time_page.click_time_attendance_configuration()

#Reports
#ProjectReports
@when('the user clicks on reports for projectreports and enters "{projectname}","{fromdate}","{todate}"clicks on view button')
def step_click_time_reports_projectreports(context,projectname,fromdate,todate):
    context.time_page.click_time_reports()
    context.time_page.click_time_reports_projectreports(projectname,fromdate,todate)

#EmployeeReports
@when('the user clicks on reports for employeereports and enters "{employeename}","{projectname}","{activityname}","{fromdate}","{todate}"clicks on view button')
def step_click_time_reports_employeereports(context,employeename,projectname,activityname,fromdate,todate):
    context.time_page.click_time_reports()
    context.time_page.click_time_reports_employeereports(employeename,projectname,activityname,fromdate,todate)

#AttendanceSummary
@when('the user clicks on reports for attendancesummary and enters "{employeename}","{jobtitle}","{subunit}","{employeementstatus}","{fromdate}","{todate}"clicks on view button')
def step_click_time_reports_attendancesummary(context,employeename,jobtitle,subunit,employeementstatus,fromdate,todate):
    context.time_page.click_time_reports()
    context.time_page.click_time_reports_attendancesummary(employeename,jobtitle,subunit,employeementstatus,fromdate,todate)

#projectinfo
#Customers
@when('the user clicks on projectinfo for customers and enters "{name}","{description}"clicks on view button')
def step_click_time_projectinfo_customers(context, name, description):
    context.time_page.click_time_projectinfo()
    context.time_page.click_time_projectinfo_customers(name, description)

#Projects
@when('the user clicks on projectinfo for projects and enters "{customername}","{project}","{projectadmin}"clicks on search button')
def step_click_time_projectinfo_projects(context, customername, project,projectadmin):
    context.time_page.click_time_projectinfo()
    context.time_page.click_time_projectinfo_projects(customername, project,projectadmin)

#Add_Projects
@when('the user clicks on projectinfo for projects and enters "{name}","{customername}","{description}","{projectadmin}"clicks on save button')
def step_click_time_projectinfo_addprojects(context, name,customername,description, projectadmin):
    context.time_page.click_time_projectinfo()
    context.time_page.click_time_projectinfo_addprojects(name,customername,description, projectadmin)
