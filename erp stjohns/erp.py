from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time  # To use sleep for a more straightforward handling of timing

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get('https://permitting.sjrwmd.com/ep/#/ep')

# Wait for the page to load completely
wait = WebDriverWait(driver, 5)

# Click on the "Click to Login" button
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.card.card-block.d-flex.bg-white.mb-0.services-image")))
login_button.click()
time.sleep(5)
# Login Process
username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
username.send_keys("apratim.biswas@realtydynamics.app")
password.send_keys("Realty Dynamics App, LLC.")
login_submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mat-raised-button")))
login_submit_button.click()
time.sleep(5)

# Click on the 'Search' dropdown button
search_button = wait.until(EC.element_to_be_clickable((By.ID, "mat-tab-link-8")))
search_button.click()
print("Clicked on 'Search' dropdown.")  # Debugging output
# Find all elements with the class 'mat-menu-item'
menu_items = driver.find_elements(By.CSS_SELECTOR, "button.mat-menu-item")
# Iterate through found elements to click the one with the correct text
for item in menu_items:
    if "Regulatory Search" in item.text:
        item.click()
        break

time.sleep(15)

# We assume the label 'Permit Type' is next to the dropdown we need to interact with
# This might need adjustment based on the actual structure of your webpage
permit_type_label = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Permit Type')]")))
parent_element = permit_type_label.find_element(By.XPATH, "..")  # Going to the parent element
dropdown = parent_element.find_element(By.CSS_SELECTOR, "mat-select")  # Finding the dropdown within the parent
dropdown.click()

# Now, wait for the dropdown options to appear and be clickable
environmental_permit_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(text(), 'Environmental Resource Permit')]")))
environmental_permit_option.click()

# # Scroll to and click on the desired option
# desired_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.mat-select-min-line.ng-tns-c83-7.ng-star-inserted:contains('Environmental Resource Permitting')")))
# actions = ActionChains(driver)
# actions.move_to_element(desired_option).perform()  # Scroll into view if necessary
# desired_option.click()
#
# # Select "Received Date" from the next dropdown
# received_date_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Received Date')]")))
# received_date_option.click()
#
#
#
# # Enter dates in "From Date" and "To Date"
# from_date_input = wait.until(EC.element_to_be_clickable((By.ID, 'mat-input-8')))
# to_date_input = wait.until(EC.element_to_be_clickable((By.ID, 'mat-input-9')))
#
# from_date_input.click()  # Open the date picker for "From Date"
# from_date_input.clear()
# from_date_input.send_keys('1/1/2024')
# from_date_input.send_keys(Keys.RETURN)  # You might need to adjust this depending on how the date picker reacts
#
# to_date_input.click()  # Open the date picker for "To Date"
# to_date_input.clear()
# to_date_input.send_keys('4/15/2024')
# to_date_input.send_keys(Keys.RETURN)  # Similarly, adjust as needed
#
# # Click the 'Search' button and wait for 10 seconds
# search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Search')]//ancestor::button")))
# search_button.click()
# time.sleep(10)
#
# # Clean up and close the browser once done
# driver.quit()
