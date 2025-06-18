from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import time

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

    def select_custom_dropdown_option(self, dropdown_locator, option_text, options_locator="//div[@role='option']",
                                      timeout=10):

        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(dropdown_locator)
        ).click()


        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, options_locator))
        )


        options = self.driver.find_elements(By.XPATH, options_locator)


        for option in options:
            if option.text.strip().lower() == option_text.strip().lower():
                ActionChains(self.driver).move_to_element(option).click().perform()
                return


        raise Exception(f"Dropdown option '{option_text}' not found")

    def select_menu_dropdown_option(self,locator,timeout=20):
        element = WebDriverWait(self.driver, timeout ).until(
            EC.visibility_of_element_located(locator)
        )
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def search_for_hint_option(self,locator,employee_data,timeout=20):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator))
        )
        element.send_keys(employee_data)
        suggestions = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//span"))
        )
        action = ActionChains(self.driver)
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    def click_calendar_element(self, locator, date, timeout=50):

        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator))
        )
        element.click()
        action = ActionChains(self.driver)
        action.click(element).key_down(Keys.CONTROL).send_keys("a")\
        .key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).send_keys(date).perform()

    def click_alert_element(self, timeout=10, action="accept"):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            if action.lower() == "accept":
                alert.accept()
            elif action.lower() == "dismiss":
                alert.dismiss()
            else:
                raise ValueError("Invalid action. Use 'accept' or 'dismiss'.")
        except Exception as e:
            print(f"Alert not found or error occurred: {e}")

    def upload_file_element(self, locator, timeout=20):

        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()


        time.sleep(2)


        keyboard = Controller()
        keyboard.type("C:\\Users\\Harini\\Documents\\flowers.gif")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)





















