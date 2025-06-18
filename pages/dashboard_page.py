from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from utils.base_class import Baseclass

class DashboardPage(Baseclass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #Dashboard Page-upgrade button
        self.upgrade_button_locator = (By.XPATH, "//button[@class='oxd-glass-button orangehrm-upgrade-button']")

        #Dashboard Page_Time_At_Work
        self.timeatwork_stopwatch_locator = (By.XPATH, "//i[@class='oxd-icon bi-stopwatch']")
        self.timeatwork_date_locator = (By.XPATH, "//input[@placeholder='yyyy-dd-mm']")
        self.timeatwork_time_hour_locator = (By.XPATH, "//input[@class='oxd-input oxd-input--active oxd-time-hour-input-text']")
        self.timeatwork_time_minute_locator = (By.XPATH, "//input[@class='oxd-input oxd-input--active oxd-time-minute-input-text']")
        self.timeatwork_ampm_locator = (By.XPATH, "//input[@name='pm']")
        self.timeatwork_note_locator = (By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
        self.timeatwork_button_locator = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")



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

