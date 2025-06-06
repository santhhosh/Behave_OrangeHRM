from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException

class Baseclass:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):

        self.driver.get(page_url)

    def insert_text_in_input_field(self, locator, input_text, timeout=30):

        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator))
        )
        element.clear()
        element.send_keys(input_text)

    def click_element(self, locator, timeout=30):

        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator))
        )
        element.click()

    def wait_till_element_is_present(self, locator, timeout=5):

           wait = WebDriverWait(self.driver,timeout)
           text = wait.until(
            EC.presence_of_element_located((locator))).text
















