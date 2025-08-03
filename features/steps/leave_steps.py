from behave import given, when, then
from pages.leave_page import LeavePage
from utils.config_reader import load_config
from pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains

config = load_config()
import time

@given('the user redirect to the login page')
def step_open_login_page(context):
    context.driver.get(config.get('DEFAULT', 'url'))
    context.login_page = LoginPage(context.driver)
    context.leave_page = LeavePage(context.driver)

@when('the user logging in with username "Admin" and password "admin123"')
def step_login_application(context):
    context.login_page.enter_username("Admin")
    time.sleep(2)
    context.login_page.enter_password("admin123")
    time.sleep(2)
    context.login_page.click_loginbutton()


#leave menu
@when('the user clicks on the leave menu and redirects to the leave page')
def step_click_menu_leave(context):
    time.sleep(5)
    context.leave_page.click_menu_leave()
    time.sleep(5)

#apply
@when('the user clicks on Apply')
def step_click_leave_apply(context):
    time.sleep(5)
    context.leave_page.click_leave_apply()
    time.sleep(5)

@when('the user selects leave type "{leave_type}" from dropdown of Apply')
def step_select_leave_apply_leave_type_dropdown(context,leave_type):
    time.sleep(10)
    context.leave_page.select_leave_apply_leave_type_dropdown(leave_type)
    time.sleep(10)

@when('the user selects fromdate "{from_date}" from the calendar of Apply')
def step_select_leave_apply_from_date(context,from_date):
    time.sleep(5)
    context.leave_page.select_leave_apply_from_date(from_date)
    time.sleep(5)

@when('the user selects todate "{to_date}" from the calendar of Apply')
def step_select_leave_apply_to_date(context,to_date):
    time.sleep(5)
    context.leave_page.select_leave_apply_to_date(to_date)
    time.sleep(5)

@when('the user enters comments "{comments}" of Apply')
def step_select_leave_apply_comments(context,comments):
    time.sleep(5)
    context.leave_page.select_leave_apply_comments(comments)
    time.sleep(5)

@when('the user clicks on the search button of Apply')
def step_click_leave_apply_search_button(context):
    time.sleep(5)
    context.leave_page.click_leave_apply_search_button()
    time.sleep(5)



#myleave
@when('the user clicks on My_Leave')
def step_click_leave_myleave(context):
    time.sleep(2)
    context.leave_page.click_leave_myleave()
    time.sleep(2)

@when('the user selects fromdate "{from_date}" from the calendar of My_Leave')
def step_select_leave_myleave_from_date(context, from_date):
    time.sleep(2)
    context.leave_page.select_leave_myleave_from_date(from_date)
    time.sleep(2)

@when('the user selects todate "{to_date}" from the calendar of My_Leave')
def step_select_leave_myleave_to_date(context, to_date):
    time.sleep(2)
    context.leave_page.select_leave_myleave_to_date(to_date)
    time.sleep(2)

@when('the user selects leave type "{leave_type}" from dropdown of My_Leave')
def step_select_leave_myleave_leave_type_dropdown(context, leave_type):
    time.sleep(5)
    context.leave_page.select_leave_myleave_leave_type_dropdown(leave_type)
    time.sleep(5)

@when('the user clicks on the search button of My_Leave')
def step_click_leave_myleave_search_button(context):
    time.sleep(5)
    context.leave_page.click_leave_myleave_search_button()
    time.sleep(5)

#entitlements
@when('the user clicks on the Entitlements for Add_Entitlements')
def step_click_leave_entitlements(context):
    time.sleep(5)
    context.leave_page.click_leave_entitlements()
    time.sleep(5)

#add entitlements
@when('the user clicks on the Add_Entitlements')
def step_click_leave_entitlements_addentitlements(context):
    time.sleep(5)
    context.leave_page.click_leave_entitlements_addentitlements()
    time.sleep(5)

"""@when('the user clicks on the radio button')
def step_select_leave_entitlements_addentitlements_radiobutton(context):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_addentitlements_radiobutton()
    time.sleep(5)"""

@when('the user enters employee name "{employee_name}" of Add_Entitlements')
def step_select_leave_entitlements_addentitlements_employeename(context,employee_name):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_addentitlements_employeename(employee_name)
    time.sleep(5)


@when('the user clicks on the dropdown arrow and select leave type "{leave_type}" from dropdown of Add_Entitlements')
def step_select_leave_entitlements_addentitlements_leavetypedropdown(context,leave_type):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_addentitlements_leavetypedropdown(leave_type)
    time.sleep(5)

@when('the user clicks on the dropdown arrow and select leave period "{leave_period}" from dropdown of Add_Entitlements')
def step_select_leave_entitlements_addentitlements_leaveperiod(context,leave_period):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_addentitlements_leaveperiod(leave_period)
    time.sleep(5)


@when('the user enters entitlement in the particular field "{entitlement_data}" of Add_Entitlements')
def step_select_leave_entitlements_addentitlements_Entitlement(context,entitlement_data):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_addentitlements_Entitlement(entitlement_data)
    time.sleep(5)

@when('the user clicking on the save button of Add_Entitlements')
def step_select_leave_entitlements_addentitlements_savebutton(context):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_addentitlements_savebutton()
    time.sleep(5)

@when('the user clicking on the confirm button of Add_Entitlements')
def step_select_leave_entitlements_addentitlements_confirmbutton(context):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_addentitlements_confirmbutton()
    time.sleep(10)

#EmployeeEntitlements
@when('the user clicking on the Entitlements for Employee_Entitlements')
def step_click_leave_entitlements(context):
    time.sleep(5)
    context.leave_page.click_leave_entitlements()
    time.sleep(5)

@when('the user clicks on the EmployeeEntitlements')
def step_click_leave_entitlements_employeeentitlements(context):
    time.sleep(5)
    context.leave_page.click_leave_entitlements_employeeentitlements()
    time.sleep(5)

@when('the user enters employee name "{employee_name}" of Employee_Entitlements')
def step_click_leave_entitlements_employeeentitlements_employeename(context,employee_name):
    time.sleep(5)
    context.leave_page.click_leave_entitlements_employeeentitlements_employeename(employee_name)
    time.sleep(5)

@when('the user clicks on the dropdown arrow and select leavetype "{leave_type}" from dropdown of Employee_Entitlements')
def step_click_leave_entitlements_employeeentitlements_leavetypedropdown(context,leave_type):
    time.sleep(5)
    context.leave_page.click_leave_entitlements_employeeentitlements_leavetypedropdown(leave_type)
    time.sleep(5)

@when('the user clicks on the dropdown arrow and select leaveperiod "{leave_period}" from dropdown of Employee_Entitlements')
def step_select_leave_entitlements_employeeentitlements_leaveperiod(context,leave_period):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_employeeentitlements_leaveperiod(leave_period)
    time.sleep(5)

@when('the user clicking on the search button of Employee_Entitlements')
def step_select_leave_entitlements_employeeentitlements_searchbutton(context):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_employeeentitlements_searchbutton()
    time.sleep(5)

#myentitlements
@when('the user is on the Entitlements for My_Entitlements')
def step_click_leave_entitlements(context):
    time.sleep(5)
    context.leave_page.click_leave_entitlements()
    time.sleep(5)

@when('the user clicks on the MyEntitlements')
def step_click_leave_entitlements_myentitlements(context):
    time.sleep(5)
    context.leave_page.click_leave_entitlements_myentitlements()
    time.sleep(5)

@when('the user clicks on the dropdown arrow and select leavetype "{leave_type}" from dropdown of My_Entitlements')
def step_select_leave_entitlements_myentitlements_leavetypedropdown(context,leave_type):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_myentitlements_leavetypedropdown(leave_type)
    time.sleep(5)

@when('the user clicks on the dropdown arrow and select leaveperiod "<leave_period>" from dropdown of My_Entitlements')
def step_select_leave_entitlements_myentitlements_leaveperiod(context,leave_period):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_myentitlements_leaveperiod(leave_period)
    time.sleep(5)

@when('the user clicking on the search button of My_Entitlements')
def step_select_leave_entitlements_myentitlements_searchbutton(context):
    time.sleep(5)
    context.leave_page.select_leave_entitlements_myentitlements_searchbutton()
    time.sleep(5)

#reports
@when('the user is on the Reports for LeaveEntitlementsandUsageReport')
def step_click_leave_reports(context):
    time.sleep(5)
    context.leave_page.click_leave_reports()
    time.sleep(5)
#LeaveEntitlementsandUsage
@when('the user clicks on the LeaveEntitlementsandUsageReport')
def step_click_leave_reports_LeaveEntitlementsandUsage(context):
    time.sleep(5)
    context.leave_page.click_leave_reports_LeaveEntitlementsandUsage()
    time.sleep(5)

@when('the user clicking on the radio button of LeaveEntitlementsandUsageReport')
def step_click_leave_reports_LeaveEntitlementsandUsage_employee_radiobutton(context):
    time.sleep(5)
    context.leave_page.click_leave_reports_LeaveEntitlementsandUsage_employee_radiobutton()
    time.sleep(5)

@when('the user enters employeename "{employee_name}" of LeaveEntitlementsandUsageReport')
def step_click_leave_reports_LeaveEntitlementsandUsage_employeename(context,employee_name):
    time.sleep(5)
    context.leave_page.click_leave_reports_LeaveEntitlementsandUsage_employeename(employee_name)
    time.sleep(5)

@when('the user clicks on the dropdown arrow and select leaveperiod "{leave_period}" from dropdown of LeaveEntitlementsandUsageReport')
def step_click_leave_reports_LeaveEntitlementsandUsage_leaveperiod(context,leave_period):
    time.sleep(5)
    context.leave_page.click_leave_reports_LeaveEntitlementsandUsage_leaveperiod(leave_period)
    time.sleep(5)

@when('the user clicking on the generate button of LeaveEntitlementsandUsageReport')
def step_click_leave_reports_LeaveEntitlementsandUsage_generate(context):
    time.sleep(5)
    context.leave_page.click_leave_reports_LeaveEntitlementsandUsage_generate()
    time.sleep(5)

#My Leave Entitlements and Usage Report
@when('the user is on the Reports for MyLeaveEntitlementsandUsageReport')
def step_click_leave_reports(context):
    time.sleep(5)
    context.leave_page.click_leave_reports()
    time.sleep(5)

@when('the user clicks on the MyLeaveEntitlementsandUsageReport')
def step_click_leave_reports_MyLeaveEntitlementsandUsageReport(context):
    time.sleep(5)
    context.leave_page.click_leave_reports_MyLeaveEntitlementsandUsageReport()
    time.sleep(5)

@when('the user clicks on the dropdown arrow and select leaveperiod "{leave_period}" from dropdown of MyLeaveEntitlementsandUsageReport')
def step_click_leave_reports_MyLeaveEntitlementsandUsageReport_leaveperiod(context,leave_period):
    time.sleep(5)
    context.leave_page.click_leave_reports_MyLeaveEntitlementsandUsageReport_leaveperiod(leave_period)
    time.sleep(5)

@when('the user clicking on the generate button of MyLeaveEntitlementsandUsageReport')
def step_click_leave_reports_MyLeaveEntitlementsandUsageReport_generate(context):
    time.sleep(5)
    context.leave_page.click_leave_reports_MyLeaveEntitlementsandUsageReport_generate()
    time.sleep(5)

#configure
@when('the user is on the configure for LeavePeriod')
def step_click_leave_configure(context):
    time.sleep(5)
    context.leave_page.click_leave_configure()
    time.sleep(5)

#leave period
@when('the user clicks on the LeavePeriod')
def step_click_leave_configure_leaveperiod(context):
    time.sleep(5)
    context.leave_page.click_leave_configure_leaveperiod()
    time.sleep(5)

@when('the user selects startmonth "{start_month}" from the calendar of LeavePeriod')
def step_click_leave_configure_leaveperiod_startmonth(context,start_month):
    time.sleep(5)
    context.leave_page.click_leave_configure_leaveperiod_startmonth(start_month)
    time.sleep(5)

@when('the user selects startdate "{start_date}" from the calendar of LeavePeriod')
def step_click_leave_configure_leaveperiod_startdate(context,start_date):
    time.sleep(5)
    context.leave_page.click_leave_configure_leaveperiod_startdate(start_date)
    time.sleep(5)

@when('the user clicks on the save button of LeavePeriod')
def step_click_leave_configure_leaveperiod_save(context):
    time.sleep(5)
    context.leave_page.click_leave_configure_leaveperiod_save()
    time.sleep(5)

#leavetypes
@when('the user is on the configure for LeaveTypes')
def step_click_leave_configure(context):
    time.sleep(5)
    context.leave_page.click_leave_configure()
    time.sleep(5)

@when('the user clicks on the LeaveTypes')
def step_click_leave_configure_leavetypes(context):
    time.sleep(5)
    context.leave_page.click_leave_configure_leavetypes()
    time.sleep(5)

@when('the user clicks on the add button of LeaveTypes')
def step_click_leave_configure_leavetypes_addbutton(context):
    time.sleep(5)
    context.leave_page.click_leave_configure_leavetypes_addbutton()
    time.sleep(5)

@when('the user enters name "{name}" of LeaveTypes')
def step_select_leave_configure_leavetypes_name(context,name):
    time.sleep(5)
    context.leave_page.select_leave_configure_leavetypes_name(name)
    time.sleep(5)

@when('the user clicks radiobutton of LeaveTypes')
def step_click_leave_configure_leavetypes_IsEntitlementSituational(context):
    time.sleep(5)
    context.leave_page.click_leave_configure_leavetypes_IsEntitlementSituational()
    time.sleep(5)

@when('the user clicks on the save button of LeaveTypes')
def step_click_leave_configure_leavetypes_save(context):
    time.sleep(5)
    context.leave_page.click_leave_configure_leavetypes_save()
    time.sleep(5)

#workweek
@when('the user is on the configure for WorkWeek')
def step_click_leave_configure(context):
    time.sleep(5)
    context.leave_page.click_leave_configure()
    time.sleep(5)

@when('the user clicks on the WorkWeek')
def step_click_leave_configure_workweek(context):
    time.sleep(5)
    context.leave_page.click_leave_configure_workweek()
    time.sleep(5)

@when('the user selects monday dropdown "{monday}" of WorkWeek')
def step_select_leave_configure_workweek_monday(context,monday):
    time.sleep(5)
    context.leave_page.select_leave_configure_workweek_monday(monday)
    time.sleep(5)

@when('the user selects tuesday dropdown "{tuesday}" of WorkWeek')
def step_select_leave_configure_workweek_tuesday(context,tuesday):
    time.sleep(5)
    context.leave_page.select_leave_configure_workweek_tuesday(tuesday)
    time.sleep(5)

@when('the user selects wednesday dropdown "{wednesday}" of WorkWeek')
def step_select_leave_configure_workweek_wednesday(context,wednesday):
    time.sleep(5)
    context.leave_page.select_leave_configure_workweek_wednesday(wednesday)
    time.sleep(5)

@when('the user selects thursday dropdown "{thursday}" of WorkWeek')
def step_select_leave_configure_workweek_thursday(context,thursday):
    time.sleep(5)
    context.leave_page.select_leave_configure_workweek_thursday(thursday)
    time.sleep(5)

@when('the user selects friday dropdown "{friday}" of WorkWeek')
def step_select_leave_configure_workweek_friday(context,friday):
    time.sleep(5)
    context.leave_page.select_leave_configure_workweek_friday(friday)
    time.sleep(5)

@when('the user selects saturday dropdown "{saturday}" of WorkWeek')
def step_select_leave_configure_workweek_saturday(context,saturday):
    time.sleep(5)
    context.leave_page.select_leave_configure_workweek_saturday(saturday)
    time.sleep(5)

@when('the user selects sunday dropdown "{sunday}" of WorkWeek')
def step_select_leave_configure_workweek_sunday(context,sunday):
    time.sleep(5)
    context.leave_page.select_leave_configure_workweek_sunday(sunday)
    time.sleep(5)

@when('the user clicks on the save button of WorkWeek')
def step_click_leave_configure_workweek_save(context):
    time.sleep(5)
    context.leave_page.click_leave_configure_workweek_save()
    time.sleep(5)

#holidays
@when('the user is on the configure for Holidays')
def step_click_leave_configure(context):
    time.sleep(5)
    context.leave_page.click_leave_configure()
    time.sleep(5)

@when('the user clicks on the Holidays')
def step_click_leave_configure_holidays(context):
    time.sleep(5)
    context.leave_page.click_leave_configure_holidays()
    time.sleep(5)

@when('the user selects fromdate "{from_date}" from the calendar of Holidays')
def step_select_leave_configure_holidays_from_date(context,from_date):
    time.sleep(5)
    context.leave_page.select_leave_configure_holidays_from_date(from_date)
    time.sleep(5)

@when('the user selects todate "{to_date}" from the calendar of Holidays')
def step_select_leave_configure_holidays_to_date(context,to_date):
    time.sleep(5)
    context.leave_page.select_leave_configure_holidays_to_date(to_date)
    time.sleep(5)

@when('the user clicks on the search button of Holidays')
def step_click_leave_configure_holidays_search(context):
    time.sleep(5)
    context.leave_page.click_leave_configure_holidays_search()
    time.sleep(5)


#leavelist
@when('the user selects fromdate "{from_date}" from the calendar of leave_list')
def step_select_leave_leavelist_from_date(context,from_date):
    time.sleep(2)
    context.leave_page.select_leave_leavelist_from_date(from_date)
    time.sleep(2)

@when('the user selects todate "{to_date}" from the calendar of leave_list')
def step_select_leave_leavelist_to_date(context,to_date):
    time.sleep(2)
    context.leave_page.select_leave_leavelist_to_date(to_date)
    time.sleep(2)

@when('the user selects leave with status "{leave_with_status}" from dropdown of leave_list')
def step_select_leave_leavelist_leave_withstatus_dropdown(context,leave_with_status):
    time.sleep(2)
    context.leave_page.select_leave_leavelist_leave_withstatus_dropdown(leave_with_status)
    time.sleep(5)

@when('the user selects leave type "{leave_type}" from dropdown of leave_list')
def step_select_leave_leavelist_leave_type_dropdown(context,leave_type):
    time.sleep(5)
    context.leave_page.select_leave_leavelist_leave_type_dropdown(leave_type)
    time.sleep(5)

@when('the user enters employeename "{employee_name}" of leave_list')
def step_select_leave_leavelist_search_employeename(context,employee_name):
    time.sleep(5)
    context.leave_page.select_leave_leavelist_search_employeename(employee_name)
    time.sleep(5)

@when('the user selects subunit "{sub_unit}" from dropdown of leave_list')
def step_select_leave_leavelist_sub_unit_dropdown(context,sub_unit):
    time.sleep(5)
    context.leave_page.select_leave_leavelist_sub_unit_dropdown(sub_unit)
    time.sleep(5)

@when('the user clicks on the radio button of leave_list')
def step_click_leave_leavelist_radio_button(context):
    time.sleep(5)
    context.leave_page.click_leave_leavelist_radio_button()
    time.sleep(5)

@when('the user clicks on the search button of leave_list')
def step_click_leave_leavelist_search_button(context):
    time.sleep(5)
    context.leave_page.click_leave_leavelist_search_button()
    time.sleep(5)

#Assign_Leave
@when('the user clicks on Assign_Leave and enters "{employee_name}","{leave_type}","{from_date}","{to_date}","{comments}"')
def step_click_leave_assignleave(context,employee_name,
                                      leave_type,
                                      from_date,
                                      to_date,
                                      comments):
    #time.sleep(2)
    context.leave_page.click_leave_assignleave()
    context.leave_page.select_leave_assignleave_form(employee_name,
                                                     leave_type,
                                                     from_date,
                                                     to_date,
                                                     comments)

    #time.sleep(2)

"""@when('the user enters employeename "{employee_name}" of Assign_Leave')
def step_select_leave_assignleave_employeename(context,employee_name,
                                      leave_type,
                                      from_date,
                                      to_date,
                                      comments):
    
    context.leave_page.select_leave_assignleave_form(employee_name,
                                      leave_type,
                                      from_date,
                                      to_date,
                                      comments)"""


"""@when('the user selects leave type "{leave_type}" from dropdown of Assign_Leave')
def step_select_leave_assignleave_leave_type_dropdown(context,leave_type):
    time.sleep(5)
    context.leave_page.select_leave_assignleave_leave_type_dropdown(leave_type)
    time.sleep(5)

@when('the user selects fromdate "{from_date}" from the calendar of Assign_Leave')
def step_select_leave_assignleave_from_date(context,from_date):
    time.sleep(5)
    context.leave_page.select_leave_assignleave_from_date(from_date)
    time.sleep(5)

@when('the user selects todate "{to_date}" from the calendar of Assign_Leave')
def step_select_leave_assignleave_to_date(context,to_date):
    time.sleep(5)
    context.leave_page.select_leave_assignleave_to_date(to_date)
    time.sleep(5)

@when('the user enters comments "{comments}" of Assign_Leave')
def step_select_leave_assignleave_comments(context,comments):
    time.sleep(5)
    context.leave_page.select_leave_assignleave_comments(comments)
    time.sleep(5)

@when('the user clicks on the assign button of Assign_Leave')
def step_click_leave_assignleave_assign_button(context):
    time.sleep(5)
    context.leave_page.click_leave_assignleave_assign_button()
    time.sleep(5)

@when('the user clicking on the confirm button of Assign_Leave')
def step_click_leave_assignleave_confirm_button(context):
    time.sleep(5)
    context.leave_page.click_leave_assignleave_confirm_button()
    time.sleep(5)"""






