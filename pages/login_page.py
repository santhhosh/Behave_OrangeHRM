from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from utils.base_class import Baseclass

class LoginPage(Baseclass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Login Locators
        self.username_input_locator = (By.NAME, "username")
        self.password_input_locator = (By.NAME, "password")
        self.login_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
        self.dashboard_text = (By.XPATH, "//h6[text()='Dashboard']")
        self.error_invalid_creds = (By.XPATH, "//p[text()='Invalid credentials']")
        self.username_required = (By.XPATH, "(//span[text()='Required'])[1]")
        self.password_required = (By.XPATH, "(//span[text()='Required'])[2]")

        # Forgot Password
        self.forgot_password_link = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
        self.forgot_username_input = (By.XPATH, "//input[@name = 'username']")
        self.reset_password_button = (By.XPATH, "//button[@type='submit']")

        # Social Media Icons
        self.linkedin_icon = (By.XPATH, "//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']")
        self.facebook_icon = (By.XPATH, "//a[@href='https://www.facebook.com/OrangeHRM/']")
        self.youtube_icon = (By.XPATH, "//a[@href='https://www.youtube.com/c/OrangeHRMInc']")
        self.twitter_icon = (By.XPATH, "//a[@href='https://twitter.com/orangehrm?lang=en']")

    # Actions
    def enter_username(self, username):
        self.insert_text_in_input_field(self.username_input_locator, username)

    def enter_password(self, password):
        self.insert_text_in_input_field(self.password_input_locator, password)

    def click_loginbutton(self):
        self.click_element(self.login_button_locator)

    def verify_dashboard_1(self):
        self.wait_till_element_is_present(self.dashboard_text)

    def verify_dashboard_3(self):
        self.wait_till_element_is_present(self.error_invalid_creds)

    # Forgot Password
    def click_forgotpassword(self):
        self.click_element(self.forgot_password_link)

    def enter_username_forgotpassword(self, username_1):
        self.insert_text_in_input_field(self.forgot_username_input, username_1)

    def click_reset_password(self):
        self.click_element(self.reset_password_button)

    # Icons
    def click_linkedin(self):
        self.click_element(self.linkedin_icon)

    def click_facebook(self):
        self.click_element(self.facebook_icon)

    def click_youtube(self):
        self.click_element(self.youtube_icon)

    def click_twitter(self):
        self.click_element(self.twitter_icon)
