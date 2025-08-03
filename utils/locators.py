from selenium.webdriver.common.by import By
from utils.base_class import Baseclass
import time

# save
search_button_locator = (By.XPATH, "//button[@type='submit']")
# cancel
reset_button_locator = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--ghost']")

# list_checkbox_delete
list_pagination_locator = \
    (By.XPATH, "(//button[@class='oxd-pagination-page-item oxd-pagination-page-item--page'])[2]")
list_checkbox_locator = \
    (By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']/parent::span)[2]")
list_delete_locator = \
    (By.CSS_SELECTOR, "i[class='oxd-icon bi-trash-fill oxd-button-icon']")
list_alertcancel_locator = \
    (By.CSS_SELECTOR,
     "button[class='oxd-button oxd-button--medium oxd-button--ghost orangehrm-button-margin']")

# list_deletebutton
list_deletebutton_locator = \
    (By.XPATH,
     "(//i[@class='oxd-icon bi-trash']/parent::button)[2]")
# list_editbutton
list_editbutton_locator = \
    (By.XPATH,
     "(//i[@class='oxd-icon bi-pencil-fill']/parent::button)[1]")
# list_eyebutton
list_eyebutton_locator = \
    (By.XPATH,
     "(//i[@class='oxd-icon bi-eye-fill']/parent::button)[1]")

# list_textfill
list_textfill_locator = \
    (By.XPATH,
     "(//i[@class='oxd-icon bi-file-text-fill']/parent::button)[1]")
#Date
date_locator = \
            "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[{index}]"
fromdate_locator = \
            (By.XPATH,date_locator.format(index=1))
todate_locator = \
            (By.XPATH,date_locator.format(index=2))
#Dropdown
dropdown_locator = \
            "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[{index}]"
dropdown_locator1 = \
            (By.XPATH, dropdown_locator.format(index=1))
dropdown_locator2 = \
            (By.XPATH, dropdown_locator.format(index=2))
dropdown_locator3 = \
             (By.XPATH, dropdown_locator.format(index=3))
dropdown_locator4 = \
            (By.XPATH, dropdown_locator.format(index=4))
dropdown_locator5 = \
            (By.XPATH, dropdown_locator.format(index=5))

#Searchforhints
searchforhints_locator = \
            (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
#Inputfield_commaseperated
inputfield_commaseperated_locator = \
            (By.CSS_SELECTOR, "input[placeholder='Enter comma seperated words...']")

#add_button
add_locator = \
            (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")

#Inputfield
input_locator = \
            "(//input[@placeholder = 'First Name' or 'Middle Name' or 'Middle Name'])[{index}]"
input_locator1 = \
            (By.XPATH, input_locator.format(index=1))
input_locator2 = \
            (By.XPATH, input_locator.format(index=2))
input_locator3 = \
            (By.XPATH, input_locator.format(index=3))
input_locator4 = \
            (By.XPATH, input_locator.format(index=4))
input_locator5 = \
            (By.XPATH, input_locator.format(index=5))
input_locator6 = \
            (By.XPATH, input_locator.format(index=6))
input_locator7 = \
            (By.XPATH, input_locator.format(index=7))
input_locator8 = \
            (By.XPATH, input_locator.format(index=8))
input_locator9 = \
            (By.XPATH, input_locator.format(index=9))
input_locator10 = \
            (By.XPATH, input_locator.format(index=10))
#File_Upload
file_upload_locator = \
            (By.XPATH, "(//i[@class='oxd-icon bi-upload oxd-file-input-icon'])[1]")
#Textarea
textarea_locator = \
            (By.XPATH, "(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[1]")



class CommonlocatorsPage(Baseclass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


   #save
    def click_save(self):
      self.click_buttons(search_button_locator, "save")


    #cancel
    def click_cancel(self):
     self.click_buttons(reset_button_locator, "cancel")

    #list_checkbox_delete
    def click_list_checkbox_delete(self):
         time.sleep(2)
         self.click_element(list_checkbox_locator)
         time.sleep(2)
         self.click_element(list_delete_locator)
         time.sleep(2)
         self.click_element(list_alertcancel_locator)
         time.sleep(2)
         self.click_alert_element(action=" No, Cancel ")

    #list_delete_button
    def click_list_delete_button(self):
        self.click_element(list_deletebutton_locator)
        self.click_element(list_alertcancel_locator)
        self.click_alert_element(action=" No, Cancel ")

    #list_eye_button
    def click_list_eye_button(self):
            self.click_element(list_eyebutton_locator)
