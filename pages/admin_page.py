import time

from selenium.webdriver.common.by import By
from utils.base_class import Baseclass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage(Baseclass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.implicitly_wait(10)

        #Admin
        self.menu_admin_locator = (By.XPATH, "//span[text()='Admin']")

        #UserManagement
        self.admin_usermanagement_locator = (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[1]")

        #Users
        self.admin_usermanagement_users_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[1]")
        #add
        self.admin_usermanagement_users_add_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        #adduser
        self.admin_usermanagement_users_add_userrole_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.admin_usermanagement_users_add_employeename_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
        self.admin_usermanagement_users_add_status_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.admin_usermanagement_users_add_username_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_usermanagement_users_add_password_locator = \
            (By.XPATH, "(//input[@type='password'])[1]")
        self.admin_usermanagement_users_add_confirmpassword_locator = \
            (By.XPATH, "(//input[@type='password'])[2]")
        self.admin_usermanagement_users_add_save_locator = \
            (By.XPATH, "//button[@type='submit']")

        #systemusers
        self.admin_usermanagement_users_username_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_usermanagement_users_userrole_locator= \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        self.admin_usermanagement_users_employeename_locator = \
            (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
        self.admin_usermanagement_users_status_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        self.admin_usermanagement_users_search_locator = \
            (By.XPATH, "//button[@type='submit']")

        #Job
        self.admin_Job_locator = (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[2]")

        #JobTitles
        self.admin_job_jobtitles_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[1]")

        #JobTitles_add
        self.admin_job_jobtitles_add_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.admin_job_jobtitles_jobtitle_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_job_jobtitles_jobdescription_locator = \
            (By.XPATH, "(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[1]")
        self.admin_job_jobtitles_jobspecification_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-upload oxd-file-input-icon'])[1]")
        self.admin_job_jobtitles_note_locator = \
            (By.XPATH, "(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[2]")
        self.admin_job_jobtitles_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_job_jobtitles_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")

        #Pay_Grades
        self.admin_job_paygrades_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]")

        #Pay_Grades_add
        self.admin_job_paygrades_add_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.admin_job_paygrades_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_job_paygrades_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_job_paygrades_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")

        #Pay_Grades_checkbox_delete
        self.admin_job_paygrades_list_checkbox_locator = \
            (By.XPATH,
             "//div[text()='Grade_10']//preceding::div[1]")
        self.admin_job_paygrades_delete_locator = \
            (By.XPATH,
             "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin']")
        self.admin_job_paygrades_alertcancel_locator = \
            (By.XPATH,
             "//button[@class='oxd-button oxd-button--medium oxd-button--ghost orangehrm-button-margin']")

        #list_deletebutton
        self.admin_job_paygrades_list_deletebutton_locator = \
            (By.XPATH,"//div[@class='oxd-table-row oxd-table-row--with-border']//following::div[@class='oxd-table-cell oxd-padding-cell']//following::div[text()='Grade_10']//following::div//button[1]")
        #list_editbutton
        self.admin_job_paygrades_list_editbutton_locator = \
            (By.XPATH,"//div[@class='oxd-table-row oxd-table-row--with-border']//following::div[@class='oxd-table-cell oxd-padding-cell']//following::div[text()='Grade 1']//following::div//button[2]")
        self.admin_job_paygrades_list_editbutton_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_job_paygrades_list_editbutton_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_job_paygrades_list_editbutton_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")


        #EmploymentStatus
        self.admin_job_employmentstatus_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[3]")

        #EmploymentStatus_add
        self.admin_job_employmentstatus_add_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.admin_job_employmentstatus_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_job_employmentstatus_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_job_employmentstatus_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")

        #JobCategories
        self.admin_job_jobcategories_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[4]")

        #Job Categories_add
        self.admin_job_jobcategories_add_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.admin_job_jobcategories_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_job_jobcategories_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_job_jobcategories_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")

        #Job_WorkShifts
        self.admin_job_workshifts_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[5]")

        #Job_WorkShifts_add
        self.admin_job_workshifts_add_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.admin_job_workshifts_shiftname_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_job_workshifts_fromtime_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
        self.admin_job_workshifts_totime_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]")
        self.admin_job_workshifts_assignedemployees_locator = \
            (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.admin_job_workshifts_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_job_workshifts_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")

        #Job_WorkShifts_checkbox_delete
        self.admin_job_workshifts_list_checkbox_locator = \
            (By.XPATH,
             "//div[text()='General']//preceding::div[1]")
        self.admin_job_workshifts_list_delete_locator = \
            (By.XPATH,
             "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin']")
        self.admin_job_workshifts_list_alertcancel_locator = \
            (By.XPATH,
             "//button[@class='oxd-button oxd-button--medium oxd-button--ghost orangehrm-button-margin']")

        #Job_WorkShifts_list_deletebutton
        self.admin_job_workshifts_list_deletebutton_locator = \
            (By.XPATH,
             "//div[@class='oxd-table-row oxd-table-row--with-border']//following::div[@class='oxd-table-cell oxd-padding-cell']//following::div[text()='General']//following::div//button[1]")
        #Job_WorkShifts_list_editbutton
        self.admin_job_workshifts_list_editbutton_locator = \
            (By.XPATH,
             "//div[@class='oxd-table-row oxd-table-row--with-border']//following::div[@class='oxd-table-cell oxd-padding-cell']//following::div[text()='General']//following::div//button[2]")
        self.admin_job_workshifts_list_editbutton_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_job_workshifts_list_editbutton_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_job_workshifts_list_editbutton_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")


        #Organization
        self.admin_organization_locator = (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[3]")

        #Locations
        self.admin_organization_locations_locator = \
            (By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]")

        #Locations_save_reset
        self.admin_organization_locations_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_organization_locations_city_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
        self.admin_organization_locations_country_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])")
        self.admin_organization_locations_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_organization_locations_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[5]")

        #Locations_add
        self.admin_organization_locations_add_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.admin_organization_locations_add_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_organization_locations_add_city_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
        self.admin_organization_locations_add_state_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]")
        self.admin_organization_locations_add_postal_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[5]")
        self.admin_organization_locations_add_country_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])")
        self.admin_organization_locations_add_phone_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[6]")
        self.admin_organization_locations_add_fax_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[7]")
        self.admin_organization_locations_add_address_locator = \
            (By.XPATH, "(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[1]")
        self.admin_organization_locations_add_notes_locator = \
            (By.XPATH, "(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[2]")
        self.admin_organization_locations_add_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_organization_locations_add_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")

        #Locations_checkbox_delete
        self.admin_organization_locations_list_checkbox_locator = \
            (By.XPATH,
             "//div[text()='New York Sales Office']//preceding::div[1]")
        self.admin_organization_locations_list_delete_locator = \
            (By.XPATH,
             "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin']")
        self.admin_organization_locations_list_alertcancel_locator = \
            (By.XPATH,
             "//button[@class='oxd-button oxd-button--medium oxd-button--ghost orangehrm-button-margin']")

        #Locations_list_deletebutton
        self.admin_organization_locations_list_deletebutton_locator = \
            (By.XPATH,
             "//div[@class='oxd-table-row oxd-table-row--with-border']//following::div[@class='oxd-table-cell oxd-padding-cell']//following::div[text()='Yashwanth']//following::div//button[1]")
        # list_editbutton
        self.admin_job_paygrades_list_editbutton_locator = \
            (By.XPATH,
             "//div[@class='oxd-table-row oxd-table-row--with-border']//following::div[@class='oxd-table-cell oxd-padding-cell']//following::div[text()='Grade 1']//following::div//button[2]")
        self.admin_job_paygrades_list_editbutton_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_job_paygrades_list_editbutton_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_job_paygrades_list_editbutton_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")

        #Qualifications
        self.admin_qualifications_locator = (By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[4]")

        #Qualifications_Skills
        self.admin_qualifications_skills_locator = \
            (By.XPATH, "//a[contains(text(),'Skills')]")
        self.admin_qualifications_skills_add_locator = \
            (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button/i")
        """self.admin_qualifications_skills_name_locator = \
            (By.XPATH, "//input[@class='oxd-input oxd-input--active' and @fdprocessedid='7n70nc']")"""
        self.admin_qualifications_skills_name_locator = \
                    (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")

        """self.admin_qualifications_skills_description_locator = \
            (By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical' or @placeholder='Type description here']")"""
        self.admin_qualifications_skills_description_locator = \
                    (By.TAG_NAME, "textarea")
        self.admin_qualifications_skills_save_locator = \
            (By.XPATH, "//button[@type='button' or 'submit']/following-sibling::button[1]")
        self.admin_qualifications_skills_cancel_locator = \
            (By.XPATH, "//button[@type='button' or 'submit']/preceding-sibling::button[1]")

        #Qualifications_Education
        self.admin_qualifications_education_locator = \
            (By.XPATH, "//a[starts-with(text(),'Education')]")
        self.admin_qualifications_education_add_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.admin_qualifications_education_level_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_qualifications_education_save_locator = \
            (By.XPATH, "//div[@class='oxd-form-actions']/child::button[2]")
        self.admin_qualifications_education_cancel_locator = \
            (By.XPATH, "//div[@class='oxd-form-actions']/child::button[1]")

        #Qualifications_list_checkbox_delete
        self.admin_qualifications_list_pagination_locator = \
            (By.XPATH, "(//button[@class='oxd-pagination-page-item oxd-pagination-page-item--page'])[2]")
        self.admin_qualifications_list_checkbox_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']/parent::span)[2]")
        self.admin_qualifications_list_delete_locator = \
            (By.CSS_SELECTOR, "i[class='oxd-icon bi-trash-fill oxd-button-icon']")
        self.admin_qualifications_list_alertcancel_locator = \
            (By.CSS_SELECTOR,
             "button[class='oxd-button oxd-button--medium oxd-button--ghost orangehrm-button-margin']")

        # Qualifications_list_deletebutton
        self.admin_qualifications_list_deletebutton_locator = \
            (By.XPATH,
             "(//i[@class='oxd-icon bi-trash']/parent::button)[1]")

        # Qualifications_list_editbutton
        self.admin_qualifications_list_editbutton_locator = \
            (By.XPATH,
             "(//i[@class='oxd-icon bi-pencil-fill']/parent::button)[1]")
        self.admin_qualifications_list_editbutton_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")



        #Qualifications_Licenses
        self.admin_qualifications_licenses_locator = \
            (By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-link' and text()='Licenses']")
        self.admin_qualifications_licenses_add_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary' and @type='button']")
        self.admin_qualifications_licenses_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_qualifications_licenses_save_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
        self.admin_qualifications_licenses_cancel_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']")

        #Qualifications_Languages
        self.admin_qualifications_languages_locator = \
            (By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-link' and text()='Languages']/parent::li")
        self.admin_qualifications_languages_add_locator = \
            (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary' and @type='button']")
        self.admin_qualifications_languages_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_qualifications_languages_save_locator = \
            (By.XPATH, "//button[@type='button' or 'submit']/following-sibling::button[1]")
        self.admin_qualifications_languages_cancel_locator = \
            (By.XPATH, "//button[@type='button' or 'submit']/preceding-sibling::button[1]")

        # Qualifications_Memberships
        self.admin_qualifications_memberships_locator = \
            (By.XPATH, "//a[contains(text(),'Memberships')]")
        self.admin_qualifications_memberships_add_locator = \
            (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.admin_qualifications_memberships_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_qualifications_memberships_save_locator = \
            (By.CSS_SELECTOR, "button[type='submit']")
        self.admin_qualifications_memberships_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")

        #Nationalities_add
        self.admin_nationalities_locator = \
            (By.XPATH, "//a[text()='Nationalities' or class='oxd-topbar-body-nav-tab-item']")
        self.admin_nationalities_add_locator = \
            (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.admin_nationalities_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_nationalities_save_locator = \
            (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")
        self.admin_nationalities_cancel_locator = \
            (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[1]")

        #Nationalities_list_checkbox
        self.admin_nationalities_list_pagination_locator = \
            (By.XPATH, "(//button[@class='oxd-pagination-page-item oxd-pagination-page-item--page'])[2]")
        self.admin_nationalities_list_pagination_checkbox_locator = \
            (By.XPATH, "//div[text()='Afghan']//preceding::div[1]")
        self.admin_nationalities_list_pagination_delete_locator = \
            (By.CSS_SELECTOR, "i[class='oxd-icon bi-trash-fill oxd-button-icon']")
        self.admin_nationalities_list_pagination_alertcancel_locator = \
            (By.CSS_SELECTOR,
             "button[class='oxd-button oxd-button--medium oxd-button--ghost orangehrm-button-margin']")

        #Nationalities_list_deletebutton
        self.admin_nationalities_list_deletebutton_locator = \
            (By.XPATH,
             "(//div[text()='Afghan']//following::div/button/i)[1]")
        #Nationalities_list_editbutton
        self.admin_nationalities_list_editbutton_locator = \
            (By.XPATH,
             "(//div[text()='American']//following::div/button/i)[2]")
        self.admin_nationalities_list_editbutton_name_locator = \
            (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.admin_nationalities_list_editbutton_save_locator = \
            (By.XPATH, "//button[@type='submit']")
        self.admin_nationalities_list_editbutton_cancel_locator = \
            (By.XPATH, "(//button[@type='button'])[4]")




        #Myinfo
        """self.myinfo_locator = \
            (By.XPATH, "//span[text() = 'My Info']")
        self.myinfo_download_locator = \
            (By.CSS_SELECTOR, "i[class='oxd-icon bi-download']")"""



        #Admin
    def click_menu_admin(self):
            self.click_element(self.menu_admin_locator)

    #UserManagement_Users
    def click_admin_usermanagement_users(self):
            time.sleep(2)
            self.click_element(self.admin_usermanagement_locator)
            time.sleep(2)
            self.select_menu_dropdown_option(self.admin_usermanagement_users_locator)
            time.sleep(2)


    #adduser
    def click_admin_usermanagement_users_add(self, userrole,employeename,status,username,password,confirmpassword):
            time.sleep(2)
            self.click_element(self.admin_usermanagement_users_add_locator)
            time.sleep(2)
            self.select_custom_dropdown_option(self.admin_usermanagement_users_add_userrole_locator, userrole)
            time.sleep(2)
            self.search_for_hint_option(self.admin_usermanagement_users_add_employeename_locator,employeename)
            time.sleep(2)
            self.select_custom_dropdown_option(self.admin_usermanagement_users_add_status_locator, status)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_usermanagement_users_add_username_locator, username)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_usermanagement_users_add_password_locator, password)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_usermanagement_users_add_confirmpassword_locator, confirmpassword)
            time.sleep(2)
            self.click_element(self.admin_usermanagement_users_add_save_locator)
            time.sleep(2)

    #Systemusers
    def click_admin_usermanagement_users_systemusers(self, username,userrole, employeename, status):
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_usermanagement_users_username_locator,username)
        time.sleep(2)
        self.select_custom_dropdown_option(self.admin_usermanagement_users_userrole_locator, userrole)
        time.sleep(2)
        self.search_for_hint_option(self.admin_usermanagement_users_employeename_locator, employeename)
        time.sleep(2)
        self.select_custom_dropdown_option(self.admin_usermanagement_users_status_locator, status)
        time.sleep(2)
        self.click_element(self.admin_usermanagement_users_search_locator)
        time.sleep(2)

    #Job
    def click_admin_job(self):
        time.sleep(2)
        self.click_element(self.admin_Job_locator)


    #Job_JobTitles_add
    def click_admin_job_jobtitles_add(self, jobtitle,jobdescription,note,path="C:\\Users\\Harini\\Downloads\\importData.csv"):
        time.sleep(2)
        self.select_menu_dropdown_option(self.admin_job_jobtitles_locator)
        time.sleep(2)
        time.sleep(2)
        self.click_element(self.admin_job_jobtitles_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_job_jobtitles_jobtitle_locator, jobtitle)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_job_jobtitles_jobdescription_locator, jobdescription)
        time.sleep(2)
        self.upload_file_element(self.admin_job_jobtitles_jobspecification_locator, path)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_job_jobtitles_note_locator,note)
        time.sleep(2)
        """self.click_element(self.admin_job_jobtitles_save_locator)
        time.sleep(2)
        self.click_element(self.admin_job_jobtitles_cancel_locator)
        time.sleep(2)"""

    #Job_JobTitles_add_save_cancel
    def click_admin_job_jobtitles_save_cancel(self,action):
        time.sleep(2)
        if action.lower() == "save":
            self.click_element(self.admin_job_jobtitles_save_locator)

        elif action.lower() == "cancel":
            self.click_element(self.admin_job_jobtitles_cancel_locator)

        else:
            print("Invalid action. Please specify 'save' or 'cancel'.")
        time.sleep(2)

    #Job_PayGrades
    def click_admin_job_paygrades(self):
        time.sleep(2)
        self.select_menu_dropdown_option(self.admin_job_paygrades_locator)


    #Job_PayGrades_add
    def click_admin_job_paygrades_add(self,name):
            time.sleep(2)
            self.click_element(self.admin_job_paygrades_add_locator)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_job_paygrades_name_locator, name)
            time.sleep(2)

    #Job_PayGrades_add_save_cancel
    def click_admin_job_paygrades_add_save_cancel(self, action):
        time.sleep(2)
        if action.lower() == "save":
            self.click_element(self.admin_job_paygrades_save_locator)

        elif action.lower() == "cancel":
            self.click_element(self.admin_job_paygrades_cancel_locator)

        else:
            print("Invalid action. Please specify 'save' or 'cancel'.")
        time.sleep(2)

    #Job_PayGrades_checkbox_delete
    def click_admin_job_paygrades_checkbox_delete(self):
            time.sleep(2)
            self.click_element(self.admin_job_paygrades_list_checkbox_locator)
            time.sleep(2)
            self.click_element(self.admin_job_paygrades_delete_locator)
            time.sleep(2)
            self.click_element(self.admin_job_paygrades_alertcancel_locator)
            time.sleep(2)
            self.click_alert_element(action=" No, Cancel ")
            """self.click_element(self.admin_job_paygrades_edit_list_locator)
            time.sleep(2)"""

    #Job_PayGrades_list_deletebutton
    def click_admin_job_paygrades_list_deletebutton(self):
        time.sleep(2)
        self.click_element(self.admin_job_paygrades_list_deletebutton_locator)
        time.sleep(2)
        self.click_element(self.admin_job_paygrades_alertcancel_locator)
        time.sleep(2)
        self.click_alert_element(action=" No, Cancel ")


    #Job_PayGrades_list_editbutton
    def click_admin_job_paygrades_list_editbutton(self,name):
        time.sleep(2)
        self.click_element(self.admin_job_paygrades_list_editbutton_locator)
        time.sleep(2)
        self.click_calendar_element(self.admin_job_paygrades_list_editbutton_name_locator,name)
        #self.insert_text_in_input_field(self.admin_job_paygrades_list_editbutton_name_locator,name)
        time.sleep(2)
        """self.click_element(self.admin_job_paygrades_list_editbutton_save_locator)
        time.sleep(2)
        self.click_element(self.admin_job_paygrades_list_editbutton_cancel_locator)
        time.sleep(2)"""



    #Job_employmentstatus_add
    def admin_job_employmentstatus_add(self, name):
            time.sleep(2)
            self.select_menu_dropdown_option(self.admin_job_employmentstatus_locator)
            time.sleep(2)
            time.sleep(2)
            self.click_element(self.admin_job_employmentstatus_add_locator)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_job_employmentstatus_name_locator, name)
            time.sleep(2)

    #Job_employmentstatus_add_save_cancel
    def click_admin_job_employmentstatus_add_save_cancel(self, action):
            time.sleep(2)
            if action.lower() == "save":
                self.click_element(self.admin_job_employmentstatus_save_locator)

            elif action.lower() == "cancel":
                self.click_element(self.admin_job_employmentstatus_cancel_locator)

            else:
                print("Invalid action. Please specify 'save' or 'cancel'.")
            time.sleep(2)

    #Job_JobCategories_add
    def admin_job_jobcategories_add(self, name):
        time.sleep(2)
        self.select_menu_dropdown_option(self.admin_job_jobcategories_locator)
        time.sleep(2)
        time.sleep(2)
        self.click_element(self.admin_job_jobcategories_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_job_jobcategories_name_locator, name)
        time.sleep(2)

   #Job_JobCategories_add_save_cancel
    def click_admin_job_jobcategories_add_save_cancel(self, action):
        time.sleep(2)
        if action.lower() == "save":
            self.click_element(self.admin_job_jobcategories_save_locator)

        elif action.lower() == "cancel":
            self.click_element(self.admin_job_jobcategories_cancel_locator)

        else:
            print("Invalid action. Please specify 'save' or 'cancel'.")
        time.sleep(2)

    #Job_workshifts
    def admin_job_workshifts(self):
        time.sleep(2)
        self.select_menu_dropdown_option(self.admin_job_workshifts_locator)
        time.sleep(2)

   #Job_workshifts_add
    def admin_job_workshifts_add(self, shiftname,fromtime,totime,assignedemployees):
        time.sleep(2)
        self.click_element(self.admin_job_workshifts_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_job_workshifts_shiftname_locator,shiftname)
        time.sleep(2)
        self.click_calendar_element(self.admin_job_workshifts_fromtime_locator, fromtime)
        time.sleep(2)
        self.click_calendar_element(self.admin_job_workshifts_totime_locator, totime)
        time.sleep(2)
        self.search_for_hint_option(self.admin_job_workshifts_assignedemployees_locator, assignedemployees)
        time.sleep(2)



    #Job_workshifts_add_save
    def admin_job_workshifts_add_save(self):
        time.sleep(2)
        self.click_buttons(self.admin_job_workshifts_save_locator, "save")
        time.sleep(2)

    #Job_workshifts_add_cancel
    def admin_job_workshifts_add_cancel(self):
        time.sleep(2)
        self.click_buttons(self.admin_job_workshifts_cancel_locator, "cancel")
        time.sleep(2)

    #Job_workshifts_list_checkbox_delete
    def click_admin_job_workshifts_list_checkbox_delete(self):
        time.sleep(2)
        self.click_element(self.admin_job_workshifts_list_checkbox_locator)
        time.sleep(2)
        self.click_element(self.admin_job_workshifts_list_delete_locator)
        time.sleep(2)
        self.click_element(self.admin_job_workshifts_list_alertcancel_locator)
        time.sleep(2)
        self.click_alert_element(action=" No, Cancel ")

    #Job_workshifts_list_deletebutton
    def click_admin_job_workshifts_list_deletebutton(self):
            time.sleep(2)
            self.click_element(self.admin_job_workshifts_list_deletebutton_locator)
            time.sleep(2)
            self.click_element(self.admin_job_workshifts_list_alertcancel_locator)
            time.sleep(2)
            self.click_alert_element(action=" No, Cancel ")

    #Job_workshifts_list_editbutton
    def click_admin_job_workshifts_list_editbutton(self,name):
        time.sleep(2)
        self.click_element(self.admin_job_workshifts_list_editbutton_locator)
        time.sleep(2)
        self.click_calendar_element(self.admin_job_workshifts_list_editbutton_name_locator,name)
        time.sleep(2)

    #Job_workshifts_list_editbutton_save
    def click_admin_job_workshifts_list_editbutton_save(self):
            time.sleep(2)
            self.click_buttons(self.admin_job_workshifts_list_editbutton_save_locator,"save")
            time.sleep(2)

    #Job_workshifts_list_editbutton_cancel
    def click_admin_job_workshifts_list_editbutton_cancel(self):
        time.sleep(2)
        self.click_buttons(self.admin_job_workshifts_list_editbutton_cancel_locator,"cancel")
        time.sleep(2)






    #Organization
    def click_admin_organization(self):
            time.sleep(2)
            self.select_menu_dropdown_option(self.admin_organization_locator)
            time.sleep(2)
            self.select_menu_dropdown_option(self.admin_organization_locations_locator)
            time.sleep(2)




    #Locations_save
    def admin_organization_locations_save(self, name,city,country):
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_organization_locations_name_locator, name)
            time.sleep(2)
            self.select_custom_dropdown_option(self.admin_organization_locations_country_locator, country)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_organization_locations_city_locator, city)
            time.sleep(2)
            self.click_buttons(self.admin_organization_locations_save_locator, "save")
            time.sleep(2)

    # Locations_cancel
    def admin_organization_locations_reset(self, name, city, country):
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_organization_locations_name_locator, name)
        time.sleep(2)
        self.select_custom_dropdown_option(self.admin_organization_locations_country_locator, country)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_organization_locations_city_locator, city)
        time.sleep(2)
        self.click_buttons(self.admin_organization_locations_cancel_locator, "cancel")
        time.sleep(2)

    #Locations_add
    def admin_organization_locations_add(self, name, city, state,postal,country,phone,fax,address,notes):
            time.sleep(2)
            self.click_element(self.admin_organization_locations_add_locator)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_organization_locations_add_name_locator, name)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_organization_locations_add_city_locator, city)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_organization_locations_add_state_locator, state)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_organization_locations_add_postal_locator, postal)
            time.sleep(2)
            self.select_custom_dropdown_option(self.admin_organization_locations_add_country_locator, country)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_organization_locations_add_phone_locator, phone)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_organization_locations_add_fax_locator, fax)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_organization_locations_add_address_locator, address)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_organization_locations_add_notes_locator, notes)
            time.sleep(2)

    #Locations_add_save
    def admin_organization_locations_add_save(self):
            time.sleep(2)
            self.click_buttons(self.admin_organization_locations_add_save_locator, "save")
            time.sleep(2)

    #Locations_add_cancel
    def admin_organization_locations_add_cancel(self):
        time.sleep(2)
        self.click_buttons(self.admin_organization_locations_add_save_locator, "cancel")
        time.sleep(2)

    #Locations_list_checkbox_delete
    def click_admin_organization_locations_list_checkbox_delete(self):
            time.sleep(2)
            self.click_element(self.admin_organization_locations_list_checkbox_locator)
            time.sleep(2)
            self.click_element(self.admin_organization_locations_list_delete_locator)
            time.sleep(2)
            self.click_element(self.admin_organization_locations_list_alertcancel_locator)
            time.sleep(2)
            self.click_alert_element(action=" No, Cancel ")

    #Locations_list_deletebutton
    def click_admin_organization_locations_list_checkbox_delete(self):
        time.sleep(2)
        self.click_element(self.admin_organization_locations_list_checkbox_locator)
        time.sleep(2)
        self.click_element(self.admin_organization_locations_list_delete_locator)
        time.sleep(2)
        self.click_element(self.admin_organization_locations_list_alertcancel_locator)
        time.sleep(2)
        self.click_alert_element(action=" No, Cancel ")

    #Qualifications_Skills
    def click_admin_qualifications_skills(self):
            time.sleep(2)
            self.select_menu_dropdown_option(self.admin_qualifications_locator)
            time.sleep(2)
            self.click_element(self.admin_qualifications_skills_locator)
            time.sleep(2)

    #Qualifications_Skills_add
    def click_admin_qualifications_skills_add(self,name,description):
        time.sleep(2)
        self.click_element(self.admin_qualifications_skills_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_qualifications_skills_name_locator,name)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_qualifications_skills_description_locator,description)
        time.sleep(2)

    #Qualifications_Skills_add_save
    def click_admin_qualifications_skills_add_save(self):
            time.sleep(2)
            self.click_buttons(self.admin_qualifications_skills_save_locator,"save")
            time.sleep(2)

    # Qualifications_Skills_add_cancel
    def click_admin_qualifications_skills_add_cancel(self):
        time.sleep(2)
        self.click_buttons(self.admin_qualifications_skills_cancel_locator,"cancel")
        time.sleep(2)

    #Qualifications_Education
    def click_admin_qualifications_education(self):
            time.sleep(2)
            self.select_menu_dropdown_option(self.admin_qualifications_locator)
            time.sleep(2)
            self.click_element(self.admin_qualifications_education_locator)
            time.sleep(2)

    # Qualifications_Education_add
    def click_admin_qualifications_education_add(self, level):
        time.sleep(2)
        self.click_element(self.admin_qualifications_education_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_qualifications_education_level_locator, level)
        time.sleep(2)

    #Qualifications_education_add_save
    def click_admin_qualifications_education_add_save(self):
            time.sleep(2)
            self.click_buttons(self.admin_qualifications_education_save_locator, "save")
            time.sleep(2)

    #Qualifications_education_add_cancel
    def click_admin_qualifications_education_add_cancel(self):
            time.sleep(2)
            self.click_buttons(self.admin_qualifications_education_cancel_locator, "cancel")
            time.sleep(2)

    # Qualifications_list_checkbox_delete
    def click_admin_qualifications_list_checkbox_delete(self):
        """time.sleep(2)
        self.click_element(self.admin_qualifications_list_pagination_locator)"""
        time.sleep(2)
        self.click_element(self.admin_qualifications_list_checkbox_locator)
        time.sleep(2)
        self.click_element(self.admin_qualifications_list_delete_locator)
        time.sleep(2)
        self.click_element(self.admin_qualifications_list_alertcancel_locator)
        time.sleep(2)
        self.click_alert_element(action=" No, Cancel ")

    #Qualifications_list_deletebutton
    def click_admin_qualifications_list_deletebutton(self):
            time.sleep(2)
            self.click_element(self.admin_qualifications_list_deletebutton_locator)
            time.sleep(2)
            self.click_element(self.admin_qualifications_list_alertcancel_locator)
            time.sleep(2)
            self.click_alert_element(action=" No, Cancel ")

    # Qualifications_list_editbutton

    def click_admin_qualifications_list_editbutton(self, level):
        time.sleep(2)
        self.click_element(self.admin_qualifications_list_editbutton_locator)
        time.sleep(2)
        self.click_calendar_element(self.admin_qualifications_list_editbutton_name_locator, level)
        time.sleep(2)

    # Qualifications_skills_list_editbutton
    def click_admin_qualifications_skills_list_editbutton(self,name, description):
        time.sleep(2)
        self.click_element(self.admin_qualifications_list_editbutton_locator)
        time.sleep(2)
        self.click_calendar_element(self.admin_qualifications_skills_name_locator, name)
        time.sleep(2)
        self.click_calendar_element(self.admin_qualifications_skills_description_locator, description)
        time.sleep(2)

    """#Qualifications_education_list_checkbox_delete
    def click_admin_qualifications_education_list_checkbox_delete(self):
        time.sleep(2)
        self.click_element(self.admin_qualifications_education_list_pagination_checkbox_locator)
        time.sleep(2)
        self.click_element(self.admin_qualifications_education_list_pagination_delete_locator)
        time.sleep(2)
        self.click_element(self.admin_qualifications_education_list_pagination_alertcancel_locator)
        time.sleep(2)
        self.click_alert_element(action=" No, Cancel ")

    #Qualifications_education_list_deletebutton
    def click_admin_qualifications_education_list_deletebutton(self):
            time.sleep(2)
            self.click_element(self.admin_nationalities_list_pagination_checkbox_locator)
            time.sleep(2)
            self.click_element(self.admin_qualifications_education_list_deletebutton_locator)
            time.sleep(2)
            self.click_element(self.admin_qualifications_education_list_pagination_alertcancel_locator)
            time.sleep(2)
            self.click_alert_element(action=" No, Cancel ")

    #Qualifications_education_list_editbutton
    def click_admin_qualifications_education_list_editbutton(self, level):
        time.sleep(2)
        self.click_element(self.admin_qualifications_education_list_editbutton_locator)
        time.sleep(2)
        self.click_calendar_element(self.admin_qualifications_education_list_editbutton_name_locator, level)
        time.sleep(2)"""





    #Qualifications_Licenses
    def click_admin_qualifications_licenses(self):
        time.sleep(2)
        self.select_menu_dropdown_option(self.admin_qualifications_locator)
        time.sleep(2)
        self.click_element(self.admin_qualifications_licenses_locator)
        time.sleep(2)

    #Qualifications_Licenses_add
    def click_admin_qualifications_licenses_add(self, name):
        time.sleep(2)
        self.click_element(self.admin_qualifications_licenses_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_qualifications_licenses_name_locator, name)
        time.sleep(2)

    #Qualifications_Licenses_add_save
    def click_admin_qualifications_licenses_add_save(self):
        time.sleep(2)
        self.click_buttons(self.admin_qualifications_licenses_save_locator, "save")
        time.sleep(2)

    #Qualifications_Licenses_add_cancel
    def click_admin_qualifications_licenses_add_cancel(self):
        time.sleep(2)
        self.click_buttons(self.admin_qualifications_licenses_cancel_locator, "cancel")
        time.sleep(2)

    #Qualifications_Languages
    def click_admin_qualifications_languages(self):
            time.sleep(2)
            self.select_menu_dropdown_option(self.admin_qualifications_locator)
            time.sleep(2)
            self.click_element(self.admin_qualifications_languages_locator)
            time.sleep(2)

    #Qualifications_Languages_add
    def click_admin_qualifications_languages_add(self, name):
            time.sleep(2)
            self.click_element(self.admin_qualifications_languages_add_locator)
            time.sleep(2)
            self.insert_text_in_input_field(self.admin_qualifications_languages_name_locator, name)
            time.sleep(2)

    #Qualifications_Languages_add_save
    def click_admin_qualifications_languages_add_save(self):
            time.sleep(2)
            self.click_buttons(self.admin_qualifications_languages_save_locator, "save")
            time.sleep(2)

    #Qualifications_Languages_add_cancel
    def click_admin_qualifications_languages_add_cancel(self):
            time.sleep(2)
            self.click_buttons(self.admin_qualifications_languages_cancel_locator, "cancel")
            time.sleep(2)

    #Qualifications_Memberships
    def click_admin_qualifications_memberships(self):
        time.sleep(2)
        self.select_menu_dropdown_option(self.admin_qualifications_locator)
        time.sleep(2)
        self.click_element(self.admin_qualifications_memberships_locator)
        time.sleep(2)

    #Qualifications_Memberships_add
    def click_admin_qualifications_memberships_add(self, name):
        time.sleep(2)
        self.click_element(self.admin_qualifications_memberships_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_qualifications_memberships_name_locator, name)
        time.sleep(2)

    #Qualifications_Memberships_add_save
    def click_admin_qualifications_memberships_add_save(self):
        time.sleep(2)
        self.click_buttons(self.admin_qualifications_memberships_save_locator, "save")
        time.sleep(2)

    #Qualifications_Memberships_add_cancel
    def click_admin_qualifications_memberships_add_cancel(self):
        time.sleep(2)
        self.click_buttons(self.admin_qualifications_memberships_cancel_locator, "cancel")
        time.sleep(2)

    """#myinfo_download
    def click_myinfo_download(self,path="test_345"):
        time.sleep(2)
        self.click_element(self.myinfo_locator)
        time.sleep(2)
        self.upload_file_element(self.myinfo_download_locator, path)
        time.sleep(2)"""

    #Nationalities
    def click_admin_nationalities(self):
        time.sleep(2)
        self.click_element(self.admin_nationalities_locator)
        time.sleep(2)


    #Nationalities_add
    def click_admin_nationalities_add(self,name):
        self.click_element(self.admin_nationalities_add_locator)
        time.sleep(2)
        self.insert_text_in_input_field(self.admin_nationalities_name_locator,name)
        time.sleep(2)

    #Nationalities_add_save
    def click_admin_nationalities_add_save(self):
            time.sleep(2)
            self.click_buttons(self.admin_nationalities_save_locator, "save")
            time.sleep(2)

    #Nationalities_add_cancel
    def click_admin_nationalities_add_cancel(self):
            time.sleep(2)
            self.click_buttons(self.admin_nationalities_cancel_locator, "cancel")
            time.sleep(2)

    #Nationalities_list_checkbox_delete
    def click_admin_nationalities_list_checkbox_delete(self):
        """time.sleep(2)
        self.click_element(self.admin_nationalities_list_pagination_locator)"""
        time.sleep(2)
        self.click_element(self.admin_nationalities_list_pagination_checkbox_locator)
        time.sleep(2)
        self.click_element(self.admin_nationalities_list_pagination_delete_locator)
        time.sleep(2)
        self.click_element(self.admin_nationalities_list_pagination_alertcancel_locator)
        time.sleep(2)
        self.click_alert_element(action=" No, Cancel ")

    #Nationalities_list_deletebutton
    def click_admin_nationalities_list_deletebutton(self):
            """time.sleep(2)
            self.click_element(self.admin_nationalities_list_pagination_checkbox_locator)"""
            time.sleep(2)
            self.click_element(self.admin_nationalities_list_deletebutton_locator)
            time.sleep(2)
            self.click_element(self.admin_nationalities_list_pagination_alertcancel_locator)
            time.sleep(2)
            self.click_alert_element(action=" No, Cancel ")

    #Nationalities_list_editbutton
    def click_admin_nationalities_list_editbutton(self, name):
        time.sleep(2)
        self.click_element(self.admin_nationalities_list_editbutton_locator)
        time.sleep(2)
        self.click_calendar_element(self.admin_nationalities_list_editbutton_name_locator, name)


