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

# Ensure the dropdown is fully visible
dropdown_items_selector = ".mat-menu-content .mat-option"  # Update this with the actual selector
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, dropdown_items_selector)))

# Click 'Regulatory Search' from the expanded dropdown
try:
    regulatory_search_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Regulatory Search')]]")))
    regulatory_search_option.click()
    print("Clicked 'Regulatory Search'.")
except Exception as e:
    print(f"Failed to click on the option due to: {e}")


#
# # Click on the Permit Type dropdown to expand it
# dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-labelledby='mat-form-field-label-9']")))
# dropdown.click()
#
# # Wait for the dropdown options to be visible
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.mat-select-panel")))
#
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
