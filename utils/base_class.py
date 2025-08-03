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
from selenium.webdriver.support.ui import Select

class Baseclass:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):

        self.driver.get(page_url)

    def insert_text_in_input_field(self, locator, input_text, timeout=30):
        time.sleep(2)
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator))
        )
        element.clear()
        element.send_keys(input_text)
        time.sleep(2)

    def click_element(self, locator, timeout=50):
        time.sleep(2)
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator))
        )
        element.click()
        time.sleep(2)


    def wait_till_element_is_present(self, locator, timeout=5):
           time.sleep(2)
           wait = WebDriverWait(self.driver,timeout)
           text = wait.until(
            EC.presence_of_element_located((locator))).text
           time.sleep(2)

    def select_custom_dropdown_option(self, dropdown_locator, option_text, options_locator="//div[@role='option']",
                                      timeout=10):
        time.sleep(2)
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(dropdown_locator)
        ).click()


        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, options_locator))
        )


        options = self.driver.find_elements(By.XPATH, options_locator)

        time.sleep(2)
        for option in options:
            if option.text.strip().lower() == option_text.strip().lower():
                ActionChains(self.driver).move_to_element(option).click().perform()
                return


        raise Exception(f"Dropdown option '{option_text}' not found")
        time.sleep(2)

    def select_menu_dropdown_option(self,locator,timeout=20):
        time.sleep(2)
        element = WebDriverWait(self.driver, timeout ).until(
            EC.visibility_of_element_located(locator)
        )
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()
        time.sleep(2)

    """def search_for_hint_option(self,locator,employee_data,timeout=20):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator))
        )
        element.send_keys(employee_data)
        suggestions = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//span"))
        )
        action = ActionChains(self.driver)
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()"""

    def search_for_hint_option(self, locator, employee_data, timeout=20):
        time.sleep(2)
        try:
            # Wait for the input element to appear and send keys
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(employee_data)

            # Wait for suggestions to appear
            suggestions = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//span"))
            )

            # Check if desired suggestion exists
            matched = False
            for suggestion in suggestions:
                if employee_data.lower() in suggestion.text.lower():
                    suggestion.click()
                    matched = True
                    break

            if not matched:
                print(f"'{employee_data}' not found in suggestions. Moving to next step.")

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error while searching for '{employee_data}': {str(e)}. Skipping to next.")
            time.sleep(2)

    def click_calendar_element(self, locator, date, timeout=50):
        time.sleep(2)

        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator))
        )
        element.click()
        action = ActionChains(self.driver)
        action.click(element).key_down(Keys.CONTROL).send_keys("a")\
        .key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).send_keys(date).perform()
        time.sleep(2)

    def click_alert_element(self, timeout=10, action="accept"):
        time.sleep(2)
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
            time.sleep(2)

    def upload_file_element(self, locator,pathoffile,timeout=20):
        time.sleep(2)

        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()


        time.sleep(2)


        keyboard = Controller()
        keyboard.type(pathoffile)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(2)

    """def switch_new_tab(self,locator,timeout=20):

        parent = self.driver.current_window_handle
        windows = self.driver.window_handles
        for win in windows:
            if win!= parent:
               self.driver.switch_to.window(win)
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        self.driver.close()
        self.driver.switch_to.window(parent)
        self.driver.quit()"""



    def switch_new_tab(self,timeout=10):
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        windows = self.driver.window_handles
        for win in windows:
            if win!= parent_window:
                self.driver.switch_to.window(win)
        time.sleep(2)

    def switch_back_parent_tab(self, timeout=10):
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        #self.driver.close()
        self.driver.switch_to.window(parent_window)
        time.sleep(2)

    def click_dropdown_element(self, locator, text, timeout=10):
        time.sleep(2)

        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        dropdown = Select(element)
        dropdown.select_by_visible_text(text)
        time.sleep(2)

    """def get_url_when_title_is(self, expected_title, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.title_is(expected_title))
        return self.driver.current_url"""

    """def get_current_url(self):
        return self.driver.current_url"""

    def get_current_url(self):
        time.sleep(2)
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        return current_url
        time.sleep(2)

    def click_buttons(self, locator, action):
        time.sleep(2)
        action = action.lower()
        if action == "save":
            self.click_element(locator)
        elif action == "cancel":
            self.click_element(locator)
        else:
            print("Invalid action. Please specify 'save' or 'cancel'.")
        time.sleep(2)

    def click_edit_buttons(self, locator, action, name):
        time.sleep(2)
        action = action.lower()
        if action == "text":
            self.click_calendar_element(locator,name)
        elif action == "textfield":
            self.click_calendar_element(locator,name)
        else:
            print("Invalid action")
        time.sleep(2)

    def select_first_dropdown_option_1(self, dropdown_locator, options_locator="//div[@role='option']", timeout=10):
        try:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(dropdown_locator)
            ).click()

            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, options_locator))
            )

            options = self.driver.find_elements(By.XPATH, options_locator)
            time.sleep(2)

            for option in options:
                option_text = option.text.strip()
                if option_text:  # skip blank or empty items
                    ActionChains(self.driver).move_to_element(option).click().perform()
                    print(f"Selected first available option: '{option_text}'")
                    return

            print("[INFO] No valid dropdown options found to select.")

        except Exception as e:
            print(f"[WARNING] Failed to select an option from dropdown: {e}")
            time.sleep(2)




















