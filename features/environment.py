from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def before_scenario(context,scenario):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)

def after_scenario(context,scenario):
    context.driver.quit()

