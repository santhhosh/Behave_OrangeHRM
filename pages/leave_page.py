from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from utils.base_class import Baseclass
from selenium.webdriver.common.action_chains import ActionChains
import time

class LeavePage(Baseclass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #leavemenu
        self.menu_leave_locator = (By.XPATH, "//a[@href='/web/index.php/leave/viewLeaveModule']")

        #apply
        self.leave_apply_locator = (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-item'])[1]")
        self.leave_apply_leave_type_dropdown_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.leave_apply_from_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.leave_apply_to_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]")
        self.leave_apply_comments_locator = \
            (By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
        self.leave_apply_search_button_locator = \
            (By.XPATH, "//button[@type='submit']")

        # Myleave
        self.leave_myleave_locator = (By.XPATH, "//a[text()='My Leave']")
        self.leave_myleave_from_date_locator  = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.leave_myleave_to_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]")
        self.leave_myleave_leave_type_dropdown_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.leave_myleave_search_button_locator = \
            (By.XPATH, "//button[@type='submit']")


        #entitlements
        self.leave_entitlements_locator = (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[1]")
        #addentitlements
        self.leave_entitlements_addentitlements_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[1]")
        self.leave_entitlements_addentitlements_radiobutton_locator = (
            By.XPATH, "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[2]")
        self.leave_entitlements_addentitlements_employeename_locator = \
            (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.leave_entitlements_addentitlements_leavetypedropdown_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.leave_entitlements_addentitlements_leavetypeddlist_locator = \
            (By.XPATH, "//div[@role='listbox']//span")
        self.leave_entitlements_addentitlements_leaveperiod_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.leave_entitlements_addentitlements_Entitlement_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.leave_entitlements_addentitlements_savebutton_locator = (
        By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
        self.leave_entitlements_addentitlements_confirmbutton_locator = (
            By.XPATH, "//button[text()=' Confirm ']")

        #employeeentitlements
        self.leave_entitlements_employeeentitlements_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]")
        self.leave_entitlements_employeeentitlements_employeename_locator =\
                     (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.leave_entitlements_employeeentitlements_leavetypedropdown_locator = (
        By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.leave_entitlements_employeeentitlements_leaveperiod_locator = (
        By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.leave_entitlements_employeeentitlements_searchbutton_locator = (
            By.XPATH, "//button[@type='submit']")

        #myentitlements
        self.leave_entitlements_myentitlements_locator = (
        By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[3]")
        self.leave_entitlements_myentitlements_leavetypedropdown_locator = (
            By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.leave_entitlements_myentitlements_leaveperiod_locator = (
            By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.leave_entitlements_myentitlements_searchbutton_locator = (
            By.XPATH, "//button[@type='submit']")

        #reports
        self.leave_reports_locator = (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[2]")

        #Leave Entitlements and Usage Report
        self.leave_reports_LeaveEntitlementsandUsage_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[1]")
        self.leave_reports_LeaveEntitlementsandUsage_employee_radiobutton_locator = \
            (By.XPATH, "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[2]")
        self.leave_reports_LeaveEntitlementsandUsage_employeename_locator = \
            (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.leave_reports_LeaveEntitlementsandUsage_leaveperiod_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.leave_reports_LeaveEntitlementsandUsage_generate_locator = \
            (By.XPATH, "//button[@type='submit']")

        #My Leave Entitlements and Usage Report
        self.leave_reports_MyLeaveEntitlementsandUsageReport_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]")
        self.leave_reports_MyLeaveEntitlementsandUsageReport_leaveperiod_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.leave_reports_MyLeaveEntitlementsandUsageReport_generate_locator = \
            (By.XPATH, "//button[@type='submit']")

        #configure
        self.leave_configure_locator = (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[3]")

        #leaveperiod
        self.leave_configure_leaveperiod_locator = (By.XPATH, "(//a[@role='menuitem'])[1]")
        self.leave_configure_leaveperiod_startmonth_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.leave_configure_leaveperiod_startdate_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.leave_configure_leaveperiod_save_locator = \
            (By.XPATH, "//button[@type='submit']")

        #leavetypes
        self.leave_configure_leavetypes_locator = (By.XPATH, "(//a[@role='menuitem'])[2]")
        self.leave_configure_leavetypes_addbutton_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.leave_configure_leavetypes_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.leave_configure_leavetypes_IsEntitlementSituational_locator = \
            (By.XPATH, "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]")
        self.leave_configure_leavetypes_save_locator = \
            (By.XPATH, "//button[@type='submit']")

        #workweek
        self.leave_configure_workweek_locator = (By.XPATH, "(//a[@role='menuitem'])[3]")
        self.leave_configure_workweek_monday_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.leave_configure_workweek_tuesday_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.leave_configure_workweek_wednesday_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[3]")
        self.leave_configure_workweek_thursday_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[4]")
        self.leave_configure_workweek_friday_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[5]")
        self.leave_configure_workweek_saturday_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[6]")
        self.leave_configure_workweek_sunday_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[7]")
        self.leave_configure_workweek_save_locator = \
            (By.XPATH, "//button[@type='submit']")

        # Holidays
        self.leave_configure_holidays_locator = (By.XPATH, "(//a[@role='menuitem'])[4]")
        self.leave_configure_holidays_from_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.leave_configure_holidays_to_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]")
        self.leave_configure_holidays_search_locator = \
            (By.XPATH, "//button[@type='submit']")


        # Leavelist
        self.leave_leavelist_from_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.leave_leavelist_to_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]")
        self.leave_leavelist_leave_withstatus_dropdown_locator = (
            By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
        self.leave_leavelist_leave_type_dropdown_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.leave_leavelist_search_employeename_locator = \
            (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.leave_leavelist_sub_unit_dropdown_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[3]")
        self.leave_leavelist_radio_button_locator = \
            (By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        self.leave_leavelist_search_button_locator = \
            (By.XPATH, "//button[@type='submit']")

        #Assign_Leave
        self.leave_assignleave_locator = (By.XPATH, "//a[text()='Assign Leave']")
        self.leave_assignleave_employeename_locator = \
            (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.leave_assignleave_leave_type_dropdown_locator = \
            (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
        self.leave_assignleave_from_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        self.leave_assignleave_to_date_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]")
        self.leave_assignleave_comments_locator = \
            (By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
        self.leave_assignleave_assign_button_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.leave_assignleave_confirm_button_locator = \
            (By.XPATH, "//button[text()=' Ok ']")

    #Leavemenu
    def click_menu_leave(self):
            self.click_element(self.menu_leave_locator)

    #apply
    def click_leave_apply(self):
            self.click_element(self.leave_apply_locator)

    def select_leave_apply_leave_type_dropdown(self, leave_type):
        self.select_custom_dropdown_option(self.leave_apply_leave_type_dropdown_locator,
                                           leave_type)

    def select_leave_apply_from_date(self, from_date):
        self.click_calendar_element(self.leave_apply_from_date_locator,
                                    from_date)

    def select_leave_apply_to_date(self, to_date):
        self.click_calendar_element(self.leave_apply_to_date_locator,
                                    to_date)

    def select_leave_apply_comments(self,comments):
        self.insert_text_in_input_field(self.leave_apply_comments_locator,comments)

    def click_leave_apply_search_button(self):
            self.click_element(self.leave_apply_search_button_locator)

    #myleave
    def click_leave_myleave(self):
            self.click_element(self.leave_myleave_locator)

    def select_leave_myleave_from_date(self, from_date):
        self.click_calendar_element(self.leave_myleave_from_date_locator,
                                    from_date)

    def select_leave_myleave_to_date(self, to_date):
        self.click_calendar_element(self.leave_myleave_to_date_locator,
                                    to_date)

    def select_leave_myleave_leave_type_dropdown(self, leave_type):
        self.select_custom_dropdown_option(self.leave_myleave_leave_type_dropdown_locator,
                                           leave_type)

    def click_leave_myleave_search_button(self):
            self.click_element(self.leave_myleave_search_button_locator)



    #entitlements
    def click_leave_entitlements(self):
            self.click_element(self.leave_entitlements_locator)

    #add entitlements
    def click_leave_entitlements_addentitlements(self):
     self.select_menu_dropdown_option(self.leave_entitlements_addentitlements_locator)

    """def select_leave_entitlements_addentitlements_radiobutton(self):
        self.click_element(self.leave_entitlements_addentitlements_radiobutton_locator)"""

    def select_leave_entitlements_addentitlements_employeename(self,employee_name):
     self.search_for_hint_option(self.leave_entitlements_addentitlements_employeename_locator,employee_name)

    def select_leave_entitlements_addentitlements_leavetypedropdown(self,leave_type):
        self.select_custom_dropdown_option(self.leave_entitlements_addentitlements_leavetypedropdown_locator,leave_type)

    def select_leave_entitlements_addentitlements_leaveperiod(self,leave_period):
        self.select_custom_dropdown_option(self.leave_entitlements_addentitlements_leaveperiod_locator,leave_period)

    def select_leave_entitlements_addentitlements_Entitlement(self,entitlement_data):
        self.insert_text_in_input_field(self.leave_entitlements_addentitlements_Entitlement_locator,entitlement_data)

    def select_leave_entitlements_addentitlements_savebutton(self):
        self.click_element(self.leave_entitlements_addentitlements_savebutton_locator)


    def select_leave_entitlements_addentitlements_confirmbutton(self):
        self.click_element(self.leave_entitlements_addentitlements_confirmbutton_locator)
        self.click_alert_element(action="Confirm")

    #EmployeeEntitlements
    def click_leave_entitlements_employeeentitlements(self):
     self.select_menu_dropdown_option(self.leave_entitlements_employeeentitlements_locator)

    def click_leave_entitlements_employeeentitlements_employeename(self,employee_name):
     self.search_for_hint_option(self.leave_entitlements_employeeentitlements_employeename_locator,employee_name)

    def click_leave_entitlements_employeeentitlements_leavetypedropdown(self,leave_type):
     self.select_custom_dropdown_option(self.leave_entitlements_employeeentitlements_leavetypedropdown_locator,leave_type)

    def select_leave_entitlements_employeeentitlements_leaveperiod(self, leave_period):
         self.select_custom_dropdown_option(self.leave_entitlements_employeeentitlements_leaveperiod_locator, leave_period)

    def select_leave_entitlements_employeeentitlements_searchbutton(self):
        self.click_element(self.leave_entitlements_employeeentitlements_searchbutton_locator)

    #myentitlements
    def click_leave_entitlements_myentitlements(self):
        self.select_menu_dropdown_option(self.leave_entitlements_myentitlements_locator)

    def select_leave_entitlements_myentitlements_leavetypedropdown(self, leave_type):
        self.select_custom_dropdown_option(self.leave_entitlements_myentitlements_leavetypedropdown_locator,
                                               leave_type)

    def select_leave_entitlements_myentitlements_leaveperiod(self, leave_period):
        self.select_custom_dropdown_option(self.leave_entitlements_myentitlements_leaveperiod_locator,
                                               leave_period)

    def select_leave_entitlements_myentitlements_searchbutton(self):
        self.click_element(self.leave_entitlements_myentitlements_searchbutton_locator)


    #reports
    def click_leave_reports(self):
         self.click_element(self.leave_reports_locator)

    #Leave Entitlements and Usage Report
    def click_leave_reports_LeaveEntitlementsandUsage(self):
         self.select_menu_dropdown_option(self.leave_reports_LeaveEntitlementsandUsage_locator)

    def click_leave_reports_LeaveEntitlementsandUsage_employee_radiobutton(self):
         self.click_element(self.leave_reports_LeaveEntitlementsandUsage_employee_radiobutton_locator)

    def click_leave_reports_LeaveEntitlementsandUsage_employeename(self,employee_name):
         self.search_for_hint_option(self.leave_reports_LeaveEntitlementsandUsage_employeename_locator,employee_name)

    def click_leave_reports_LeaveEntitlementsandUsage_leaveperiod(self, leave_period):
        self.select_custom_dropdown_option(self.leave_reports_LeaveEntitlementsandUsage_leaveperiod_locator, leave_period)

    def click_leave_reports_LeaveEntitlementsandUsage_generate(self):
        self.click_element(self.leave_reports_LeaveEntitlementsandUsage_generate_locator)

    #My Leave Entitlements and Usage Report
    def click_leave_reports_MyLeaveEntitlementsandUsageReport(self):
         self.select_menu_dropdown_option(self.leave_reports_MyLeaveEntitlementsandUsageReport_locator)

    def click_leave_reports_MyLeaveEntitlementsandUsageReport_leaveperiod(self, leave_period):
        self.select_custom_dropdown_option(self.leave_reports_MyLeaveEntitlementsandUsageReport_leaveperiod_locator, leave_period)

    def click_leave_reports_MyLeaveEntitlementsandUsageReport_generate(self):
        self.click_element(self.leave_reports_MyLeaveEntitlementsandUsageReport_generate_locator)

    # configure
    def click_leave_configure(self):
         self.click_element(self.leave_configure_locator)

    # leaveperiod
    def click_leave_configure_leaveperiod(self):
         self.select_menu_dropdown_option(self.leave_configure_leaveperiod_locator)

    def click_leave_configure_leaveperiod_startmonth(self, start_month):
        self.select_custom_dropdown_option(self.leave_configure_leaveperiod_startmonth_locator, start_month)

    def click_leave_configure_leaveperiod_startdate(self, start_date):
        self.select_custom_dropdown_option(self.leave_configure_leaveperiod_startdate_locator, start_date)

    def click_leave_configure_leaveperiod_save(self):
        self.click_element(self.leave_configure_leaveperiod_save_locator)

    #leavetypes
    def click_leave_configure_leavetypes(self):
         self.select_menu_dropdown_option(self.leave_configure_leavetypes_locator)

    def click_leave_configure_leavetypes_addbutton(self):
        self.click_element(self.leave_configure_leavetypes_addbutton_locator)

    def select_leave_configure_leavetypes_name(self,name):
        self.insert_text_in_input_field(self.leave_configure_leavetypes_name_locator,name)

    def click_leave_configure_leavetypes_IsEntitlementSituational(self):
        self.click_element(self.leave_configure_leavetypes_IsEntitlementSituational_locator)

    def click_leave_configure_leavetypes_save(self):
        self.click_element(self.leave_configure_leavetypes_save_locator)

    #workweek
    def click_leave_configure_workweek(self):
         self.select_menu_dropdown_option(self.leave_configure_workweek_locator)

    def select_leave_configure_workweek_monday(self, monday):
        self.select_custom_dropdown_option(self.leave_configure_workweek_monday_locator,
                                           monday)

    def select_leave_configure_workweek_tuesday(self, tuesday):
        self.select_custom_dropdown_option(self.leave_configure_workweek_tuesday_locator,
                                           tuesday)

    def select_leave_configure_workweek_wednesday(self, wednesday):
        self.select_custom_dropdown_option(self.leave_configure_workweek_wednesday_locator,
                                           wednesday)

    def select_leave_configure_workweek_thursday(self, thursday):
        self.select_custom_dropdown_option(self.leave_configure_workweek_thursday_locator,
                                           thursday)

    def select_leave_configure_workweek_friday(self, friday):
        self.select_custom_dropdown_option(self.leave_configure_workweek_friday_locator,
                                           friday)

    def select_leave_configure_workweek_saturday(self, saturday):
        self.select_custom_dropdown_option(self.leave_configure_workweek_saturday_locator,
                                           saturday)

    def select_leave_configure_workweek_sunday(self, sunday):
        self.select_custom_dropdown_option(self.leave_configure_workweek_sunday_locator,
                                           sunday)

    def click_leave_configure_workweek_save(self):
        self.click_element(self.leave_configure_workweek_save_locator)

    #Holidays
    def click_leave_configure_holidays(self):
         self.select_menu_dropdown_option(self.leave_configure_holidays_locator)

    def select_leave_configure_holidays_from_date(self, from_date):
        self.click_calendar_element(self.leave_configure_holidays_from_date_locator,
                                           from_date)

    def select_leave_configure_holidays_to_date(self, to_date):
        self.click_calendar_element(self.leave_configure_holidays_to_date_locator,
                                           to_date)

    def click_leave_configure_holidays_search(self):
        self.click_element(self.leave_configure_holidays_search_locator)





    # Leavelist
    def select_leave_leavelist_from_date(self, from_date):
        self.click_calendar_element(self.leave_leavelist_from_date_locator,
                                    from_date)

    def select_leave_leavelist_to_date(self, to_date):
        self.click_calendar_element(self.leave_leavelist_to_date_locator,
                                    to_date)

    def select_leave_leavelist_leave_withstatus_dropdown(self, leave_with_status):
        self.select_custom_dropdown_option(self.leave_leavelist_leave_withstatus_dropdown_locator,
                                           leave_with_status)

    def select_leave_leavelist_leave_type_dropdown(self, leave_type):
        self.select_custom_dropdown_option(self.leave_leavelist_leave_type_dropdown_locator,
                                           leave_type)

    def select_leave_leavelist_search_employeename(self, employee_name):
        self.search_for_hint_option(self.leave_leavelist_search_employeename_locator,
                                    employee_name)

    def select_leave_leavelist_sub_unit_dropdown(self, sub_unit):
        self.select_custom_dropdown_option(self.leave_leavelist_sub_unit_dropdown_locator,
                                           sub_unit)

    def click_leave_leavelist_radio_button(self):
        self.click_element(self.leave_leavelist_radio_button_locator)

    def click_leave_leavelist_search_button(self):
        self.click_element(self.leave_leavelist_search_button_locator)

    #Assign_Leave
    def click_leave_assignleave(self):
        self.click_element(self.leave_assignleave_locator)

    def select_leave_assignleave_form(self,
                                      employee_name,
                                      leave_type,
                                      from_date,
                                      to_date,
                                      comments):
        self.search_for_hint_option(self.leave_assignleave_employeename_locator,
                                    employee_name)
        self.select_custom_dropdown_option(self.leave_assignleave_leave_type_dropdown_locator,
                                           leave_type)
        self.click_calendar_element(self.leave_assignleave_from_date_locator,
                                    from_date)
        self.click_calendar_element(self.leave_assignleave_to_date_locator,
                                    to_date)
        self.insert_text_in_input_field(self.leave_assignleave_comments_locator, comments)
        self.click_element(self.leave_assignleave_assign_button_locator)
        self.click_element(self.leave_assignleave_confirm_button_locator)
        self.click_alert_element(action="Confirm")
    """def select_leave_assignleave_leave_type_dropdown(self, leave_type):


    def select_leave_assignleave_from_date(self, from_date):


    def select_leave_assignleave_to_date(self, to_date):


    def select_leave_assignleave_comments(self,comments):
        

    def click_leave_assignleave_assign_button(self):
        

    def click_leave_assignleave_confirm_button(self):"""










