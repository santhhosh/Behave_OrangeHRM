from selenium.webdriver.common.by import By
from utils.base_class import Baseclass

class PIMPage(Baseclass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #addemployee
        self.menu_pim_locator = (By.XPATH, "//span[text()='PIM']")
        self.pim_addemployee_locator = (By.XPATH, "//a[text()='Add Employee']")
        self.pim_addemployee_firstname_locator = (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-firstname']")
        self.pim_addemployee_middlename_locator = (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-middlename']")
        self.pim_addemployee_lastname_locator = (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-lastname']")
        self.pim_addemployee_employeeid_locator = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.pim_addemployee_fileuploadbutton_locator = (By.XPATH, "//div[@class='oxd-file-div oxd-file-div--active']")
        self.pim_addemployee_savebutton_locator = (By.XPATH, "//button[@type='submit']")

        #reports
        self.pim_reports_locator = (By.XPATH, "//a[text()='Reports']")
        self.pim_reports_reportname_locator = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.pim_reports_search_button_locator = (By.XPATH, "//button[@type='submit']")





    #add_employee
    def click_menu_pim(self):
            self.click_element(self.menu_pim_locator)

    def click_pim_addemployee(self):
            self.click_element(self.pim_addemployee_locator)

    def enter_pim_addemployee_firstname(self,Firstname):
            self.insert_text_in_input_field(self.pim_addemployee_firstname_locator,Firstname)

    def enter_pim_addemployee_middlename(self,Middlename):
            self.insert_text_in_input_field(self.pim_addemployee_middlename_locator,Middlename)

    def enter_pim_addemployee_lastname(self,Lastname):
            self.insert_text_in_input_field(self.pim_addemployee_lastname_locator,Lastname)

    def enter_pim_addemployee_employeeid(self,Employeeid):
            self.insert_text_in_input_field(self.pim_addemployee_employeeid_locator,Employeeid)

    def enter_pim_addemployee_fileuploadbutton(self):
            self.upload_file_element(self.pim_addemployee_fileuploadbutton_locator)

    def click_pim_addemployee_savebutton(self):
            self.click_element(self.pim_addemployee_savebutton_locator)


    #reports
    def click_pim_reports(self):
        self.click_element(self.pim_reports_locator)

    def enter_pim_reports_reportname(self,ReportName):
            self.search_for_hint_option(self.pim_reports_reportname_locator,ReportName)

    def click_pim_reports_search_button(self):
        self.click_element(self.pim_reports_search_button_locator)
