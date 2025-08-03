from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from utils.base_class import Baseclass
from selenium.webdriver.common.action_chains import ActionChains
from utils.config_reader import load_config
from utils.locators import *
#from utils.locators import *

import time
config = load_config()

class RecruitmentPage(Baseclass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #recruitmentmenu
        self.menu_recruitment_locator = (By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[5]")


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

        # Candidates
        self.recruitment_candidates_locator = (By.XPATH, "//a[contains(text(),'Candidates')]")
        #vacancies
        self.recruitment_vacancies_locator = (By.XPATH, "//a[contains(text(),'Vacancies')]")
        """recruitment_dropdown_locator = \
            "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[{index}]"
        self.recruitment_candidates_jobtitle_locator = \
            (By.XPATH, recruitment_dropdown_locator.format(index=1))
        self.recruitment_candidates_vacancy_locator = \
            (By.XPATH, recruitment_dropdown_locator.format(index=2))
        self.recruitment_candidates_hiringmanager_locator = \
             (By.XPATH, recruitment_dropdown_locator.format(index=3))
        self.recruitment_candidates_status_locator = \
            (By.XPATH, recruitment_dropdown_locator.format(index=4))
        self.recruitment_candidates_candidatename_locator = \
            (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
        self.recruitment_candidates_keywords_locator = \
            (By.CSS_SELECTOR, "input[placeholder='Enter comma seperated words...']")"""

        """recruitment_date_locator = \
            "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[{index}]"
        self.recruitment_candidates_fromdate_locator = \
            (By.XPATH, recruitment_date_locator.format(index=1))
        self.recruitment_candidates_todate_locator = \
            (By.XPATH, recruitment_date_locator.format(index=2))
        self.recruitment_candidates_methodofapplication_locator = \
            (By.XPATH, recruitment_dropdown_locator.format(index=5))"""






    #Recruitmentmenu
    def click_menu_recruitment(self):
            self.click_element(self.menu_recruitment_locator)


    #Recruitment_Candidates
    def click_recruitment_candidates(self):
            self.click_element(self.recruitment_candidates_locator)


    #Recruitment_Candidates_form
    def click_recruitment_candidates_form(self,jobtitle, vacancy,hiringmanager,status,keywords,fromdate,todate,methodofapplication):
        

        self.select_custom_dropdown_option(dropdown_locator1,jobtitle)
        
        self.select_custom_dropdown_option(dropdown_locator2, vacancy)
        
        self.select_custom_dropdown_option(dropdown_locator3, hiringmanager)
        
        self.select_custom_dropdown_option(dropdown_locator4, status)
        
        #self.search_for_hint_option(searchforhints_locator , candidatename)
        
        self.insert_text_in_input_field(input_locator3, keywords)
        
        self.click_calendar_element(fromdate_locator, fromdate)
        
        self.click_calendar_element(todate_locator, todate)
        
        self.select_custom_dropdown_option(dropdown_locator5, methodofapplication)

    #Recruitment_Candidates_add
    def click_recruitment_candidates_add(self, firstname, middlename, lastname, vacancy, email,contactnumber,keywords, fromdate,notes,
                                         path="C:\\Users\\Harini\\Documents\\OrangeHRM_File_upload\\OrangeHRM DATA.txt"):
            #addbutton
            self.click_element(add_locator)
            self.insert_text_in_input_field(input_locator2,firstname)
            self.insert_text_in_input_field(input_locator3, middlename)
            self.insert_text_in_input_field(input_locator4, lastname)
            self.select_custom_dropdown_option(dropdown_locator1, vacancy)
            self.insert_text_in_input_field(input_locator5, email)
            self.insert_text_in_input_field(input_locator6, contactnumber)
            self.upload_file_element(file_upload_locator, path)
            self.insert_text_in_input_field(input_locator8, keywords)
            self.click_calendar_element(fromdate_locator, fromdate)
            self.insert_text_in_input_field(textarea_locator, notes)

    #Recruitment_Vacancies
    def click_recruitment_vacancies(self):
        self.click_element(self.recruitment_vacancies_locator)

    #Recruitment_Vacancies_form
    def click_recruitment_vacancies_form(self, jobtitle, vacancy, hiringmanager, status):
            self.select_custom_dropdown_option(dropdown_locator1, jobtitle)

            self.select_custom_dropdown_option(dropdown_locator2, vacancy)

            self.select_custom_dropdown_option(dropdown_locator3, hiringmanager)

            self.select_custom_dropdown_option(dropdown_locator4, status)



