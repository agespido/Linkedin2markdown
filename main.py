from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()

LOGIN_URL = "https://www.linkedin.com"

# if chromedriver is not in your path, you’ll need to add it here
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True

driver = webdriver.Firefox(capabilities=cap)

# Log in screen
driver.get (LOGIN_URL)
driver.find_element_by_id('session_key').send_keys('user@mail.com')
driver.find_element_by_id('session_password').send_keys('password')
driver.find_element_by_class_name('sign-in-form__submit-button').click()
#driver.quit()