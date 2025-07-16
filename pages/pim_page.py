import time

from selenium.webdriver.common.by import By
from utils.base_class import Baseclass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage(Baseclass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.menu_pim_locator = (By.XPATH, "//span[text()='PIM']")

        #configuration
        self.pim_configuration_locator = (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[1]")
        #OptionalFields
        self.pim_configuration_optionalfields_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[1]")
        self.pim_configuration_optionalfields_showdeprecatedfields_locator = \
            (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
        self.pim_configuration_optionalfields_ShowSSNfieldinPersonalDetails_locator = \
            (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]")
        self.pim_configuration_optionalfields_ShowSINfieldinPersonalDetails_locator = \
            (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[3]")
        self.pim_configuration_optionalfields_ShowUSTaxExemptionsmenu_locator = \
            (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[4]")
        self.pim_configuration_optionalfields_save_locator = \
            (By.XPATH, "//button[@type='submit']")

        #CustomFields
        self.pim_configuration_customfields_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]")
        self.pim_configuration_customfields_add_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")
        self.pim_configuration_customfields_fieldname_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.pim_configuration_customfields_screen_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.pim_configuration_customfields_type_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.pim_configuration_customfields_save_locator = \
            (By.XPATH, "//button[@type='submit']")

        #DataImport
        self.pim_configuration_dataimport_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[3]")
        self.pim_configuration_dataimport_selectfile_locator = \
            (By.XPATH, "//i[@class='oxd-icon bi-upload oxd-file-input-icon']")
        self.pim_configuration_dataimport_upload_locator = \
            (By.XPATH, "//button[@type='submit']")

        #ReportingMethods
        self.pim_configuration_reportingmethods_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[4]")
        self.pim_configuration_reportingmethods_add_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")
        self.pim_configuration_reportingmethods_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.pim_configuration_reportingmethods_save_locator = \
            (By.XPATH, "//button[@type='submit']")

        #TerminationReasons
        self.pim_configuration_terminationreasons_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[5]")
        self.pim_configuration_terminationreasons_add_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")
        self.pim_configuration_terminationreasons_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.pim_configuration_terminationreasons_save_locator = \
            (By.XPATH, "//button[@type='submit']")



        #employeelist
        self.pim_employeelist_locator = (By.XPATH, "//a[text()='Employee List']")
        self.pim_employeelist_employeename_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
        self.pim_employeelist_employeeid_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.pim_employeelist_employmentstatus_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.pim_employeelist_include_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.pim_employeelist_supervisorname_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
        self.pim_employeelist_jobtitle_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[3]")
        self.pim_employeelist_subunit_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[4]")
        self.pim_employeelist_search_locator = \
            (By.XPATH, "//button[@type='submit']")

        #addemployee
        self.pim_addemployee_locator = (By.XPATH, "//a[text()='Add Employee']")
        self.pim_addemployee_firstname_locator = \
            (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-firstname']")
        self.pim_addemployee_middlename_locator = \
            (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-middlename']")
        self.pim_addemployee_lastname_locator = \
            (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-lastname']")
        self.pim_addemployee_employeeid_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.pim_addemployee_fileuploadbutton_locator = \
            (By.XPATH, "//div[@class='oxd-file-div oxd-file-div--active']")
        self.pim_addemployee_savebutton_locator = (By.XPATH, "//button[@type='submit']")

        #reports
        self.pim_reports_locator = (By.XPATH, "//a[text()='Reports']")
        self.pim_reports_reportname_locator = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.pim_reports_search_button_locator = (By.XPATH, "//button[@type='submit']")

    #PIM
    def click_menu_pim(self):
            self.click_element(self.menu_pim_locator)

    #configuration
    def click_pim_configuration(self):
            self.click_element(self.pim_configuration_locator)

    #OptionalFields
    def click_pim_configuration_optionalfields(self):
            self.select_menu_dropdown_option(self.pim_configuration_optionalfields_locator)

    def click_pim_configuration_optionalfields_showdeprecatedfields(self):
            self.click_element(self.pim_configuration_optionalfields_showdeprecatedfields_locator)

    def click_pim_configuration_optionalfields_ShowSSNfieldinPersonalDetails(self):
            self.click_element(self.pim_configuration_optionalfields_ShowSSNfieldinPersonalDetails_locator)

    def click_pim_configuration_optionalfields_ShowSINfieldinPersonalDetails(self):
            self.click_element(self.pim_configuration_optionalfields_ShowSINfieldinPersonalDetails_locator)

    def click_pim_configuration_optionalfields_ShowUSTaxExemptionsmenu(self):
            self.click_element(self.pim_configuration_optionalfields_ShowUSTaxExemptionsmenu_locator)

    def click_pim_configuration_optionalfields_save(self):
            self.click_element(self.pim_configuration_optionalfields_save_locator)

    #CustomFields
    def click_pim_configuration_customfields(self,fieldname,screen,type):
            time.sleep(2)
            self.select_menu_dropdown_option(self.pim_configuration_customfields_locator)
            time.sleep(2)
            self.click_element(self.pim_configuration_customfields_add_locator)
            time.sleep(2)
            self.insert_text_in_input_field(self.pim_configuration_customfields_fieldname_locator,fieldname)
            time.sleep(2)
            self.select_custom_dropdown_option(self.pim_configuration_customfields_screen_locator,screen)
            time.sleep(2)
            self.select_custom_dropdown_option(self.pim_configuration_customfields_type_locator, type)
            time.sleep(2)
            self.click_element(self.pim_configuration_optionalfields_save_locator)
            time.sleep(2)

    #DataImport
    def click_pim_configuration_dataimport(self,path="C:\\Users\\Harini\\Downloads\\importData.csv"):
            time.sleep(2)
            self.select_menu_dropdown_option(self.pim_configuration_dataimport_locator)
            time.sleep(2)
            self.upload_file_element(self.pim_configuration_dataimport_selectfile_locator,path)
            time.sleep(2)
            self.click_element(self.pim_configuration_dataimport_upload_locator)
            time.sleep(2)

    #ReportingMethods
    def click_pim_configuration_reportingmethods(self,name):
            time.sleep(2)
            self.select_menu_dropdown_option(self.pim_configuration_reportingmethods_locator)
            time.sleep(2)
            self.click_element(self.pim_configuration_reportingmethods_add_locator)
            time.sleep(2)
            self.insert_text_in_input_field(self.pim_configuration_reportingmethods_name_locator,name)
            time.sleep(2)
            self.click_element(self.pim_configuration_reportingmethods_save_locator)
            time.sleep(2)

    #TerminationReasons
    def click_pim_configuration_terminationreasons(self, name):
        time.sleep(2)
        self.select_menu_dropdown_option(self.pim_configuration_terminationreasons_locator)
        time.sleep(2)
        self.click_element(self.pim_configuration_terminationreasons_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.pim_configuration_terminationreasons_name_locator, name)
        time.sleep(2)
        self.click_element(self.pim_configuration_terminationreasons_save_locator)
        time.sleep(2)



    #employeelist
    def click_pim_employeelist(self):
        self.click_element(self.pim_employeelist_locator)

    def enter_pim_employeelist_employeename(self,employeename):
            self.search_for_hint_option(self.pim_employeelist_employeename_locator,employeename)

    def enter_pim_employeelist_employeeid(self,employeeid):
            self.insert_text_in_input_field(self.pim_employeelist_employeeid_locator,employeeid)

    def enter_pim_employeelist_employmentstatus(self,employmentstatus):
            self.select_custom_dropdown_option(self.pim_employeelist_employmentstatus_locator,employmentstatus)

    def enter_pim_employeelist_include(self, include):
        self.select_custom_dropdown_option(self.pim_employeelist_include_locator, include)

    def enter_pim_employeelist_supervisorname(self, supervisorname):
        self.search_for_hint_option(self.pim_employeelist_supervisorname_locator, supervisorname)

    def enter_pim_employeelist_jobtitle(self,jobtitle):
            self.select_custom_dropdown_option(self.pim_employeelist_jobtitle_locator,jobtitle)

    def enter_pim_employeelist_subunit(self, subunit):
        self.select_custom_dropdown_option(self.pim_employeelist_subunit_locator, subunit)

    def click_pim_employeelist_search(self):
            self.click_element(self.pim_employeelist_search_locator)

    #add_employee
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

    def enter_pim_addemployee_fileuploadbutton(self,path="C:\\Users\\Harini\\Documents\\flowers.gif"):
            self.upload_file_element(self.pim_addemployee_fileuploadbutton_locator,path)

    def click_pim_addemployee_savebutton(self):
            self.click_element(self.pim_addemployee_savebutton_locator)


    #reports
    def click_pim_reports(self):
        self.click_element(self.pim_reports_locator)

    def enter_pim_reports_reportname(self,ReportName):
            self.search_for_hint_option(self.pim_reports_reportname_locator,ReportName)

    def click_pim_reports_search_button(self):
        self.click_element(self.pim_reports_search_button_locator)
