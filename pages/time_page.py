import time

from selenium.webdriver.common.by import By
from utils.base_class import Baseclass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TimePage(Baseclass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.implicitly_wait(10)


        self.menu_time_locator = (By.XPATH, "//span[text()='Time']")

        #TimeSheets
        self.time_timesheets_locator = (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[1]")

        #MyTimesheets
        self.time_timesheets_mytimesheets_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[1]")
        self.time_timesheets_mytimesheets_timesheetperiod_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.time_timesheets_mytimesheets_submit_locator= \
            (By.XPATH, "(//button[@type='button'])[7]")


        #EmployeeTimeSheets
        self.time_timesheets_employeetimesheets_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]")
        self.time_timesheets_employeetimesheets_employeename_locator = \
            (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.time_timesheets_employeetimesheets_view_locator = \
            (By.XPATH, "//button[@type='submit']")

        #Attendance
        self.time_attendance_locator = (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[2]")

        #MyRecords
        self.time_attendance_myrecords_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[1]")
        self.time_attendance_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.time_attendance_view_locator = \
            (By.XPATH, "//button[@type='submit']")

        #view_button
        self.time_attendance_pencil_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[1]")


        #PunchIn/Out
        self.time_attendance_Punchinout_locator =\
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]")
        self.time_attendance_Punchinout_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.time_attendance_Punchinout_time_locator = (
        By.XPATH, "(//i[@class='oxd-icon bi-clock oxd-time-input--clock'])[1]")
        self.time_attendance_Punchinout_hour_locator = (
        By.XPATH, "(//input[@class='oxd-input oxd-input--active oxd-time-hour-input-text'])[1]")
        self.time_attendance_Punchinout_minute_locator = (
            By.XPATH, "(//input[@class='oxd-input oxd-input--active oxd-time-minute-input-text'])[1]")
        self.time_attendance_Punchinout_ampm_locator = (By.XPATH, "//input[@name='pm']")
        self.time_attendance_Punchinout_note_locator = (
        By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
        self.time_attendance_Punchinout_button_locator = (
        By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")

        #EmployeeRecords
        self.time_attendance_employeerecords_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[3]")
        self.time_attendance_employeerecords_employeename_locator = \
            (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.time_attendance_employeerecords_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.time_attendance_employeerecords_view_locator = \
            (By.XPATH, "//button[@type='submit']")

        #Configuration
        self.time_attendance_configuration_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[4]")
        self.time_attendance_configuration_punchinginout_locator = \
            (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
        self.time_attendance_configuration_attendancerecords_locator = \
            (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]")
        self.time_attendance_configuration_subordinates_locator = \
            (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[3]")
        self.time_attendance_configuration_save_locator = \
            (By.XPATH, "//button[@type='submit']")

        #Reports
        self.time_reports_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[3]")

        #ProjectReports
        self.time_reports_projectreports_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[1]")
        self.time_reports_projectreports_projectname_locator = \
            (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.time_reports_projectreports_fromdate_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.time_reports_projectreports_todate_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]")
        self.time_reports_projectreports_approvedtimesheets_locator = \
            (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])")
        self.time_reports_projectreports_view_locator = \
            (By.XPATH, "//button[@type='submit']")

        #EmployeeReports
        self.time_reports_employeereports_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]")
        self.time_reports_employeereports_employeename_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
        self.time_reports_employeereports_projectname_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
        self.time_reports_employeereports_activityname_locator = \
            (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
        self.time_reports_employeereports_fromdate_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.time_reports_employeereports_todate_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]")
        self.time_reports_employeereports_approvedtimesheets_locator = \
            (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])")
        self.time_reports_employeereports_view_locator = \
            (By.XPATH, "//button[@type='submit']")

        #AttendanceSummary
        self.time_reports_attendancesummary_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[3]")
        self.time_reports_attendancesummary_employeename_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
        self.time_reports_attendancesummary_jobtitle_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.time_reports_attendancesummary_subunit_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.time_reports_attendancesummary_employeementstatus_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[3]")
        self.time_reports_attendancesummary_fromdate_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.time_reports_attendancesummary_todate_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]")
        self.time_reports_attendancesummary_view_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")

        #projectinfo
        self.time_projectinfo_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[4]")

        #Customers
        self.time_projectinfo_customers_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[1]")
        self.time_projectinfo_customers_add_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")
        self.time_projectinfo_customers_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.time_projectinfo_customers_description_locator = \
            (By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
        self.time_projectinfo_customers_save_locator = \
            (By.XPATH, "//button[@type='submit']")

        #Projects
        self.time_projectinfo_projects_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]")
        self.time_projectinfo_projects_customername_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
        self.time_projectinfo_projects_project_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
        self.time_projectinfo_projects_projectadmin_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[3]")
        self.time_projectinfo_projects_search_locator = \
            (By.XPATH, "//button[@type='submit']")

        #Projects_AddProjects
        self.time_projectinfo_add_locator = \
            (By.XPATH, "(//button[@type='button'])[5]")
        self.time_projectinfo_projects_add_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.time_projectinfo_projects_add_customername_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
        self.time_projectinfo_projects_add_description_locator = \
            (By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
        self.time_projectinfo_projects_add_projectadmin_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
        self.time_projectinfo_projects_add_save_locator = \
            (By.XPATH, "//button[@type='submit']")

        self.time_projectinfo_projects_add_addcustomer_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")





    #Time
    def click_menu_time(self):
            self.click_element(self.menu_time_locator)

    #TimeSheets
    def click_time_timesheets(self):
            self.click_element(self.time_timesheets_locator)

    #MyTimesheets
    def click_time_timesheets_mytimesheets(self,timesheetperiod):
            time.sleep(2)
            self.select_menu_dropdown_option(self.time_timesheets_mytimesheets_locator)
            time.sleep(2)
            self.click_calendar_element(self.time_timesheets_mytimesheets_timesheetperiod_locator,timesheetperiod)
            time.sleep(2)
            self.click_element(self.time_timesheets_mytimesheets_submit_locator)
            time.sleep(2)


    #EmployeeTimeSheets
    def click_time_timesheets_employeetimesheets(self,employeename):
            time.sleep(2)
            self.select_menu_dropdown_option(self.time_timesheets_employeetimesheets_locator)
            time.sleep(2)
            self.search_for_hint_option(self.time_timesheets_employeetimesheets_employeename_locator,employeename)
            time.sleep(2)
            self.click_element(self.time_timesheets_employeetimesheets_view_locator)
            time.sleep(2)

    #Attendance
    def click_time_attendance(self):
            self.click_element(self.time_attendance_locator)

    #MyRecords
    def click_time_attendance_myrecords(self,date):
            time.sleep(2)
            self.select_menu_dropdown_option(self.time_attendance_myrecords_locator)
            time.sleep(2)
            self.click_calendar_element(self.time_attendance_date_locator,date)
            time.sleep(2)
            self.click_element(self.time_attendance_view_locator)
            time.sleep(2)

            #def click_time_attendance_pencilbutton(self):
            time.sleep(2)
            self.click_element(self.time_attendance_pencil_locator)
            time.sleep(2)


    #PunchIn/Out
    def click_time_attendance_Punchinout(self, date,note):
            time.sleep(2)
            self.click_element(self.time_attendance_Punchinout_locator)
            time.sleep(2)
            self.click_calendar_element(self.time_attendance_Punchinout_date_locator, date)
            time.sleep(2)
            """self.click_element(self.time_attendance_Punchinout_time_locator)
            time.sleep(2)
            self.insert_text_in_input_field(self.time_attendance_Punchinout_hour_locator,hour)
            time.sleep(2)
            self.insert_text_in_input_field(self.time_attendance_Punchinout_minute_locator,minute)
            time.sleep(2)
            self.click_element(self.time_attendance_Punchinout_ampm_locator)
            time.sleep(2)"""
            self.insert_text_in_input_field(self.time_attendance_Punchinout_note_locator,note)
            time.sleep(2)
            self.click_element(self.time_attendance_Punchinout_button_locator)
            time.sleep(2)

    #EmployeeRecords
    def click_time_attendance_employeerecords(self, employeename,date):
        time.sleep(2)
        self.select_menu_dropdown_option(self.time_attendance_employeerecords_locator)
        time.sleep(2)
        self.search_for_hint_option(self.time_attendance_employeerecords_employeename_locator, employeename)
        time.sleep(2)
        self.click_calendar_element(self.time_attendance_employeerecords_date_locator, date)
        time.sleep(2)
        self.click_element(self.time_attendance_employeerecords_view_locator)
        time.sleep(2)

    #Configuration
    def click_time_attendance_configuration(self):
        time.sleep(2)
        self.select_menu_dropdown_option(self.time_attendance_configuration_locator)
        time.sleep(2)
        self.click_element(self.time_attendance_configuration_punchinginout_locator)
        time.sleep(2)
        self.click_element(self.time_attendance_configuration_attendancerecords_locator)
        time.sleep(2)
        self.click_element(self.time_attendance_configuration_subordinates_locator)
        time.sleep(2)
        self.click_element(self.time_attendance_configuration_save_locator)
        time.sleep(2)

    #Reports
    def click_time_reports(self):
            self.click_element(self.time_reports_locator)

    #projectreports
    def click_time_reports_projectreports(self,projectname,fromdate,todate):
        time.sleep(2)
        self.select_menu_dropdown_option(self.time_reports_projectreports_locator)
        time.sleep(2)
        self.search_for_hint_option(self.time_reports_projectreports_projectname_locator,projectname)
        time.sleep(2)
        self.click_calendar_element(self.time_reports_projectreports_fromdate_locator,fromdate)
        time.sleep(2)
        self.click_calendar_element(self.time_reports_projectreports_todate_locator,todate)
        time.sleep(2)
        self.click_element(self.time_reports_projectreports_approvedtimesheets_locator)
        time.sleep(2)
        self.click_element(self.time_reports_projectreports_view_locator)
        time.sleep(2)

    #EmployeeReports
    def click_time_reports_employeereports(self,employeename,projectname,activityname,fromdate,todate):
        time.sleep(2)
        self.select_menu_dropdown_option(self.time_reports_employeereports_locator)
        time.sleep(2)
        self.search_for_hint_option(self.time_reports_employeereports_employeename_locator,employeename)
        time.sleep(2)
        self.search_for_hint_option(self.time_reports_employeereports_projectname_locator,projectname)
        time.sleep(2)
        self.select_custom_dropdown_option(self.time_reports_employeereports_activityname_locator,activityname)
        time.sleep(2)
        self.click_calendar_element(self.time_reports_employeereports_fromdate_locator, fromdate)
        time.sleep(2)
        self.click_calendar_element(self.time_reports_employeereports_todate_locator,todate)
        time.sleep(2)
        self.click_element(self.time_reports_employeereports_approvedtimesheets_locator)
        time.sleep(2)
        self.click_element(self.time_reports_employeereports_view_locator)
        time.sleep(2)

    #AttendanceSummary
    def click_time_reports_attendancesummary(self,employeename,jobtitle,subunit,employeementstatus,fromdate,todate):
        time.sleep(2)
        self.select_menu_dropdown_option(self.time_reports_attendancesummary_locator)
        time.sleep(2)
        self.search_for_hint_option(self.time_reports_attendancesummary_employeename_locator,employeename)
        time.sleep(2)
        self.select_custom_dropdown_option(self.time_reports_attendancesummary_jobtitle_locator,jobtitle)
        time.sleep(2)
        self.select_custom_dropdown_option(self.time_reports_attendancesummary_subunit_locator,subunit)
        time.sleep(2)
        self.select_custom_dropdown_option(self.time_reports_attendancesummary_employeementstatus_locator, employeementstatus)
        time.sleep(2)
        self.click_calendar_element(self.time_reports_attendancesummary_fromdate_locator, fromdate)
        time.sleep(2)
        self.click_calendar_element(self.time_reports_attendancesummary_todate_locator,todate)
        time.sleep(2)
        self.click_element(self.time_reports_attendancesummary_view_locator)
        time.sleep(2)

    #projectinfo
    def click_time_projectinfo(self):
        self.click_element(self.time_projectinfo_locator)

    #Customers
    def click_time_projectinfo_customers(self, name, description):
        time.sleep(2)
        self.select_menu_dropdown_option(self.time_projectinfo_customers_locator)
        time.sleep(2)
        self.click_element(self.time_projectinfo_customers_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.time_projectinfo_customers_name_locator, name)
        time.sleep(2)
        self.insert_text_in_input_field(self.time_projectinfo_customers_description_locator, description)
        time.sleep(2)
        self.click_element(self.time_projectinfo_customers_save_locator)
        time.sleep(2)

    #Projects
    def click_time_projectinfo_projects(self, customername, project,projectadmin):
        time.sleep(2)
        self.select_menu_dropdown_option(self.time_projectinfo_projects_locator)
        time.sleep(2)
        self.search_for_hint_option(self.time_projectinfo_projects_customername_locator,customername)
        time.sleep(2)
        self.search_for_hint_option(self.time_projectinfo_projects_project_locator, project)
        time.sleep(2)
        self.search_for_hint_option(self.time_projectinfo_projects_projectadmin_locator, projectadmin)
        time.sleep(2)
        self.click_element(self.time_projectinfo_projects_search_locator)
        time.sleep(2)

    #Add_Projects
    def click_time_projectinfo_addprojects(self, name,customername,description, projectadmin):
        time.sleep(2)
        self.select_menu_dropdown_option(self.time_projectinfo_projects_locator)
        time.sleep(2)
        self.click_element(self.time_projectinfo_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.time_projectinfo_projects_add_name_locator, name)
        time.sleep(2)
        self.search_for_hint_option(self.time_projectinfo_projects_add_customername_locator, customername)
        time.sleep(2)
        self.insert_text_in_input_field(self.time_projectinfo_projects_add_description_locator,description)
        time.sleep(2)
        self.search_for_hint_option(self.time_projectinfo_projects_add_projectadmin_locator, projectadmin)
        time.sleep(2)
        self.click_element(self.time_projectinfo_projects_add_save_locator)
        time.sleep(2)