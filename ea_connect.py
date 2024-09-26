from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Launch the browser and navigate to the EA Web App login page
driver = webdriver.Chrome()
driver.get('https://www.ea.com/fifa/ultimate-team/web-app/')

# Step 2: Wait for the initial "Login" button to appear and click it
try:
    initial_login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
    )
    initial_login_button.click()
    print("Initial login button clicked. Proceeding to login form.")
except:
    print("Initial login button not found or not clickable.")
    driver.quit()

# Step 3: Wait for the email and password fields to appear
try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "email")))
    print("Login form loaded successfully.")
except:
    print("Login form did not load. Check the website status.")
    driver.quit()

# Step 4: Enter the login credentials (replace with your credentials)
email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")

email_input.send_keys("tamirk97@gmail.com")  # Replace with your email
password_input.send_keys("Tamir2020")  # Replace with your password

# Step 5: Click the Login button or hit enter
password_input.send_keys(Keys.RETURN)

# Step 6: Wait for the main page to load
try:
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "ut-navigation-bar-view")))
    print("Logged in successfully.")
except:
    print("Login failed or the main page took too long to load.")
    driver.quit()

# Step 7: Navigate to the Transfer Market
try:
    transfer_market_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Transfer Market')]"))
    )
    transfer_market_button.click()
    print("Navigated to Transfer Market.")
except:
    print("Failed to navigate to Transfer Market.")
    driver.quit()

# Step 8: Perform a search for "Messi"
try:
    search_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search for Player']"))
    )
    search_input.send_keys("Messi")
    search_input.send_keys(Keys.RETURN)
    print("Searching for Messi in the Transfer Market.")
except:
    print("Failed to enter search text or find the search input.")
    driver.quit()

# Step 9: Wait for the search results to load
try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "resultItems")))
    print("Search results loaded successfully.")
    # Additional code here to handle results or click specific items
except:
    print("Search results did not load or took too long.")
    driver.quit()

# Optional: Pause to see results
time.sleep(10)

# Close the browser
driver.quit()
