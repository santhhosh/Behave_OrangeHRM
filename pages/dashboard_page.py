from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from utils.base_class import Baseclass
from selenium.webdriver.support.ui import Select

class DashboardPage(Baseclass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #Dashboard Page-upgrade button
        self.upgrade_button_locator = \
            (By.XPATH, "//button[@class='oxd-glass-button orangehrm-upgrade-button']")
        self.upgrade_button_locale_locator =\
            (By.XPATH, "//select[@name='locale']")
        self.upgrade_button_bookademo_locator = (By.XPATH, "//a[text()='Book a Free Demo']")
        self.upgrade_button_bookademo_firstname_locator = (By.ID, "Form_getForm_Name")
        #self.upgrade_button_bookademo_firstname_locator = (By.XPATH, "//input[@name='Name']")
        self.upgrade_button_bookademo_phonenumber_locator = (By.XPATH, "//input[@id='Form_getForm_Contact']")
        self.upgrade_button_bookademo_email_locator = (By.NAME, "Email")
        self.upgrade_button_bookademo_companyname_locator = (By.NAME, "CompanyName")
        self.upgrade_button_bookademo_country_locator = (By.XPATH, "//select[@name='Country']")
        self.upgrade_button_bookademo_submit_locator = (By.XPATH, "//input[@type='submit']")



        #Dashboard Page_Time_At_Work
        self.timeatwork_stopwatch_locator = (By.XPATH, "//i[@class='oxd-icon bi-stopwatch']")
        self.timeatwork_date_locator = (By.XPATH, "//input[@placeholder='yyyy-dd-mm']")
        self.timeatwork_time_hour_locator = (By.XPATH, "//input[@class='oxd-input oxd-input--active oxd-time-hour-input-text']")
        self.timeatwork_time_minute_locator = (By.XPATH, "//input[@class='oxd-input oxd-input--active oxd-time-minute-input-text']")
        self.timeatwork_ampm_locator = (By.XPATH, "//input[@name='pm']")
        self.timeatwork_note_locator = (By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
        self.timeatwork_button_locator = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")

        #QuickLaunch
        self.dashboard_quicklaunch_assignleave_locator = (By.XPATH, "//button[@title='Assign Leave']")
        self.dashboard_quicklaunch_leavelist_locator = (By.XPATH, "//button[@title='Leave List']")
        self.dashboard_quicklaunch_timesheets_locator = (By.XPATH, "//button[@title='Timesheets']")
        self.dashboard_quicklaunch_applyleave_locator = (By.XPATH, "//button[@title='Apply Leave']")
        self.dashboard_quicklaunch_myleave_locator = (By.XPATH, "//button[@title='My Leave']")
        self.dashboard_quicklaunch_mytimesheet_locator = (By.XPATH, "//button[@title='My Timesheet']")

    #Dashboard Page_Time_At_Work
    def click_stopwatch(self):
        self.click_element(self.timeatwork_stopwatch_locator)

    def click_calendar(self,Date):
        self.insert_text_in_input_field(self.timeatwork_date_locator,Date)

    def click_hour(self,Hour):
        self.insert_text_in_input_field(self.timeatwork_time_hour_locator,Hour)

    def click_minute(self,Minute):
        self.insert_text_in_input_field(self.timeatwork_time_minute_locator,Minute)

    def click_ampm(self):
        self.click_element(self.timeatwork_ampm_locator)

    def enter_note(self,Note):
        self.insert_text_in_input_field(self.timeatwork_note_locator,Note)

    def click_out_in_button(self):
        self.click_element(self.timeatwork_button_locator)

    #Dashboard Page_upgrade button
    def click_upgrade_button(self):
        self.click_element(self.upgrade_button_locator)
        self.switch_new_tab()

    def click_upgrade_button_locale(self,locale):
        self.click_dropdown_element(self.upgrade_button_locale_locator,locale)

    def click_upgrade_button_bookademo(self):
        self.click_element(self.upgrade_button_bookademo_locator)

    def click_upgrade_button_bookademo_firstname(self,firstname):
        self.insert_text_in_input_field(self.upgrade_button_bookademo_firstname_locator, firstname)

    def click_upgrade_button_bookademo_phonenumber(self,phonenumber):
        self.insert_text_in_input_field(self.upgrade_button_bookademo_phonenumber_locator, phonenumber)

    def click_upgrade_button_bookademo_email(self,email):
        self.insert_text_in_input_field(self.upgrade_button_bookademo_email_locator, email)

    def click_upgrade_button_bookademo_companyname(self,companyname):
        self.insert_text_in_input_field(self.upgrade_button_bookademo_companyname_locator, companyname)

    def click_upgrade_button_bookademo_country(self,country):
       self.click_dropdown_element(self.upgrade_button_bookademo_country_locator, country)

    def click_upgrade_button_bookademo_submit(self):
        self.click_element(self.upgrade_button_bookademo_submit_locator)
        #self.switch_back_parent_tab()


    #QuickLaunch_assignleave
    def click_dashboard_quicklaunch_assignleave(self):
        self.click_element(self.dashboard_quicklaunch_assignleave_locator)
        self.get_current_url()

    #QuickLaunch_leavelist
    def click_dashboard_quicklaunch_leavelist(self):
            self.click_element(self.dashboard_quicklaunch_leavelist_locator)
            self.get_current_url()

    #QuickLaunch_timesheets
    def click_dashboard_quicklaunch_timesheets(self):
        self.click_element(self.dashboard_quicklaunch_timesheets_locator)
        self.get_current_url()

    #QuickLaunch_applyleave
    def click_dashboard_quicklaunch_applyleave(self):
            self.click_element(self.dashboard_quicklaunch_applyleave_locator)
            self.get_current_url()

    #QuickLaunch_myleave
    def click_dashboard_quicklaunch_myleave(self):
        self.click_element(self.dashboard_quicklaunch_myleave_locator)
        self.get_current_url()

    #QuickLaunch_mytimesheet
    def click_dashboard_quicklaunch_mytimesheet(self):
            self.click_element(self.dashboard_quicklaunch_mytimesheet_locator)
            self.get_current_url()