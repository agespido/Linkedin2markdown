from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import geckodriver_autoinstaller
import yaml

# For this script to work properly, the two-step verification must be off.
# I can't take your phone and read your SMS code, sorry :)

def logIn(driver):

	# Get LinkedIn credentials
	keys = yaml.load(open('.credentials.yml'), Loader=yaml.FullLoader)

	# Log in page
	LOGIN_URL = "https://www.linkedin.com"

	driver.get (LOGIN_URL)
	driver.find_element_by_id('session_key').send_keys(keys['LinkedInKeys']['username'])
	driver.find_element_by_id('session_password').send_keys(keys['LinkedInKeys']['password'])
	driver.find_element_by_class_name('sign-in-form__submit-button').click()

	# If two-step verification is on, a timeout can be set here and 
	# wait until the verification code is introduce manually.

def getPersonalData():
	pass

def getSummary():
	pass

def getExperience():
	pass

def getEducation():
	pass

def main():
	geckodriver_autoinstaller.install()

	PROFILE_URL = "https://www.linkedin.com/in/"

	# if chromedriver is not in your path, you’ll need to add it here
	cap = DesiredCapabilities().FIREFOX
	cap["marionette"] = True

	driver = webdriver.Firefox(capabilities=cap)
	logIn(driver)

	# Profile page
	driver.get (PROFILE_URL)
	
	#driver.quit()

if __name__ == "__main__":
	main()