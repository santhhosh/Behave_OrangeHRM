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

        #reports_Add
        self.pim_add_button_locator = (
            By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.pim_add_reportname_locator = (
            By.XPATH, "//input[@class='oxd-input oxd-input--active' and @placeholder='Type here ...']")
        self.pim_add_selectioncriteria_locator = (
            By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.pim_add_include_locator = (
            By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.pim_add_displayfieldgroup_locator = (
            By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[3]")
        self.pim_add_displayfield_locator = (
            By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[4]")
        self.pim_add_plusbutton_locator = (
            By.XPATH, "(//i[@class='oxd-icon bi-plus'])[2]")

        #reports
        self.pim_reports_locator = (By.XPATH, "//a[text()='Reports']")
        self.pim_reports_reportname_locator = (By.XPATH, "//input[@placeholder='Type for hints...']")

        #save
        self.pim_search_button_locator = (By.XPATH, "//button[@type='submit']")
        #cancel
        self.pim_reset_button_locator = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--ghost']")



        #pim_list_checkbox_delete
        self.pim_list_pagination_locator = \
            (By.XPATH, "(//button[@class='oxd-pagination-page-item oxd-pagination-page-item--page'])[2]")
        self.pim_list_checkbox_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']/parent::span)[5]")
        self.pim_list_delete_locator = \
            (By.CSS_SELECTOR, "i[class='oxd-icon bi-trash-fill oxd-button-icon']")
        self.pim_list_alertcancel_locator = \
            (By.CSS_SELECTOR,
             "button[class='oxd-button oxd-button--medium oxd-button--ghost orangehrm-button-margin']")

        # pim_list_deletebutton
        self.pim_list_deletebutton_locator = \
            (By.XPATH,
             "(//i[@class='oxd-icon bi-trash']/parent::button)[2]")

        # pim_list_editbutton
        self.pim_list_editbutton_locator = \
            (By.XPATH,
             "(//i[@class='oxd-icon bi-pencil-fill']/parent::button)[1]")

        # pim_list_textfill
        self.pim_list_textfill_locator = \
            (By.XPATH,
             "(//i[@class='oxd-icon bi-file-text-fill']/parent::button)[1]")

    #PIM
    def click_menu_pim(self):
            self.click_element(self.menu_pim_locator)

    #pim_save
    def click_pim_save(self):
        
        self.click_buttons(self.pim_search_button_locator, "save")
        

    #pim_cancel
    def click_pim_cancel(self):
        
        self.click_buttons(self.pim_reset_button_locator, "cancel")
        

    # pim_list_checkbox_delete
    def click_pim_list_checkbox_delete(self):
            """
            self.click_element(self.pim_list_pagination_locator)"""
            
            self.click_element(self.pim_list_checkbox_locator)
            
            self.click_element(self.pim_list_delete_locator)
            
            self.click_element(self.pim_list_alertcancel_locator)
            
            self.click_alert_element(action=" No, Cancel ")

    # pim_list_deletebutton
    def click_pim_list_deletebutton(self):
            
            self.click_element(self.pim_list_deletebutton_locator)
            
            self.click_element(self.pim_list_alertcancel_locator)
            
            self.click_alert_element(action=" No, Cancel ")

    #pim_list_editbutton
    def click_pim_list_editbutton(self,name):
        
        self.click_element(self.pim_list_editbutton_locator)
        
        self.click_calendar_element(self.pim_add_reportname_locator, name)
        

    #pim_list_editbutton_1
    def click_pim_list_edit_button(self, name):
            
            self.click_element(self.pim_list_editbutton_locator)
            
            self.click_calendar_element(self.pim_configuration_customfields_fieldname_locator, name)
            



    #pim_list_textfill
    def click_pim_list_textfill(self):
            
            self.click_element(self.pim_list_textfill_locator)
            



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
    def click_pim_configuration_customfields(self):
            
            self.select_menu_dropdown_option(self.pim_configuration_customfields_locator)
            

    #CustomFields_add
    def click_pim_configuration_customfields_add(self,fieldname,screen,type):
            #
            self.click_element(self.pim_configuration_customfields_add_locator)
            #
            self.insert_text_in_input_field(self.pim_configuration_customfields_fieldname_locator,fieldname)
            
            self.select_custom_dropdown_option(self.pim_configuration_customfields_screen_locator,screen)
            
            self.select_custom_dropdown_option(self.pim_configuration_customfields_type_locator, type)
            
            """self.click_element(self.pim_configuration_optionalfields_save_locator)
            """

    #DataImport
    def click_pim_configuration_dataimport(self,path="C:\\Users\\Harini\\Downloads\\importData.csv"):
            
            self.select_menu_dropdown_option(self.pim_configuration_dataimport_locator)
            
            self.upload_file_element(self.pim_configuration_dataimport_selectfile_locator,path)
            
            self.click_element(self.pim_configuration_dataimport_upload_locator)
            

    #ReportingMethods

    def click_pim_configuration_reportingmethods(self):
        
        self.select_menu_dropdown_option(self.pim_configuration_reportingmethods_locator)
        

    #ReportingMethods
    def click_pim_configuration_reportingmethods_add(self,name):
            
            self.click_element(self.pim_configuration_reportingmethods_add_locator)
            
            self.insert_text_in_input_field(self.pim_configuration_reportingmethods_name_locator,name)
            
            """self.click_element(self.pim_configuration_reportingmethods_save_locator)
            """

     #TerminationReasons
    def click_pim_configuration_terminationreasons(self):
        
        self.select_menu_dropdown_option(self.pim_configuration_terminationreasons_locator)
        

    #TerminationReasons
    def click_pim_configuration_terminationreasons_add(self, name):
        
        self.click_element(self.pim_configuration_terminationreasons_add_locator)
        
        self.insert_text_in_input_field(self.pim_configuration_terminationreasons_name_locator, name)
        
        self.click_element(self.pim_configuration_terminationreasons_save_locator)
        

    #employeelist
    def click_pim_employeelist(self):
            
            self.click_element(self.pim_employeelist_locator)
            

    #employeelist_search
    def click_pim_employeelist_search(self,employeename,employeeid,employmentstatus,include,supervisorname,jobtitle,subunit):
        
        self.search_for_hint_option(self.pim_employeelist_employeename_locator, employeename)
        
        self.insert_text_in_input_field(self.pim_employeelist_employeeid_locator,employeeid)
        
        self.select_custom_dropdown_option(self.pim_employeelist_employmentstatus_locator, employmentstatus)
        
        self.select_custom_dropdown_option(self.pim_employeelist_include_locator, include)
        
        self.search_for_hint_option(self.pim_employeelist_supervisorname_locator, supervisorname)
        
        self.select_custom_dropdown_option(self.pim_employeelist_jobtitle_locator, jobtitle)
        
        self.select_custom_dropdown_option(self.pim_employeelist_subunit_locator, subunit)
        


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
        

    #reports_reportname
    def click_pim_reports_reportname(self,ReportName):
        
        self.search_for_hint_option(self.pim_reports_reportname_locator, ReportName)
        

    #reports_add
    def click_pim_reports_add(self,reportname,selectioncriteria,include,displayfieldgroup,displayfield):
        
        self.click_element(self.pim_add_button_locator)
        
        self.insert_text_in_input_field(self.pim_add_reportname_locator, reportname)
        
        self.select_custom_dropdown_option(self.pim_add_selectioncriteria_locator, selectioncriteria)
        
        self.select_custom_dropdown_option(self.pim_add_include_locator, include)
        
        self.select_custom_dropdown_option(self.pim_add_displayfieldgroup_locator, displayfieldgroup)
        
        self.select_custom_dropdown_option(self.pim_add_displayfield_locator, displayfield)
        
        self.click_element(self.pim_add_plusbutton_locator)
        







