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

def getPersonalData(driver):
	name = driver.find_element_by_xpath('//div[@class="flex-1 mr5"]/ul[1]/li[1]').text # Name
	description = driver.find_element_by_xpath('//h2[@class="mt1 t-18 t-black t-normal break-words"]').text # Description
	for i in driver.find_elements_by_xpath('//a[@data-control-name="contact_see_more"]'): #Contact info
		contactURL = i.get_attribute("href")
	driver.get (contactURL)	
	profileURL = driver.find_elements_by_xpath('//a[@class="pv-contact-info__contact-link link-without-visited-state t-14"]')[0].text #URL to LinkedIn Profile
	email = driver.find_elements_by_xpath('//a[@class="pv-contact-info__contact-link link-without-visited-state t-14"]')[1].text #URL to LinkedIn Profile
	
	print(name)
	print(description)
	print(profileURL)
	print(email)
	return 0

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
	try:
		getPersonalData(driver)
	except Exception:
		driver.quit()
		raise
	#print(driver.page_source)
	
	# Close browser
	driver.quit()

if __name__ == "__main__":
	main()