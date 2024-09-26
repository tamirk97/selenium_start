from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Open the One.co.il website
driver = webdriver.Chrome()

# Navigate to the specific topic article (example: "מכבי ת"א")
driver.get("https://www.one.co.il/Article/20-21/1,1,4,0/366839.html")  # Replace with the actual URL of the article you want

# Wait for the article page to load
time.sleep(5)

# Step 2: Scroll to the comments section
try:
    comment_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="one-comments-reply-box"]'))
    )
    print("Comment box found.")
    driver.execute_script("arguments[0].scrollIntoView(true);", comment_box)
except Exception as e:
    print(f"Error finding the comment section: {e}")
    driver.quit()
    exit()

# Step 3: Fill in the comment form
try:
    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="שם"]'))
    )
    name_field.send_keys("מכביטס")
    print("Name field filled.")

    club_badge_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'select[class="one-reply-team one-reply-hidden"]'))
    )
    club_badge_select.click()
    driver.find_element(By.CSS_SELECTOR, 'select[class="one-reply-team one-reply-hidden"] option[value="3"]').click()
    print("Club badge selected.")

    comment_field = driver.find_element(By.CSS_SELECTOR, 'textarea[class="one-reply-text"]')
    comment_field.send_keys("כל הממשלה הזאת גונבת את העם תאמינו לי אל תאמינו לאף אחד")
    print("Comment field filled.")

    submit_button = driver.find_element(By.CSS_SELECTOR, 'input[class="send-reply"]')
    submit_button.click()
    print("Comment submitted successfully.")
except Exception as e:
    print(f"Error filling out the comment form: {e}")

# Step 4: Close the browser
time.sleep(5)  # Optional: Wait to observe the result
driver.quit()
