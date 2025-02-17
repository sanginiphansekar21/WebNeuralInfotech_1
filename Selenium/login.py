from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to the login page
url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)

# Wait for the page to load (adjust the time if needed)
time.sleep(2)

# Find the username and password fields and input credentials
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Input username and password (these are just example credentials)
username_field.send_keys("student")
password_field.send_keys("Password123")

# Find the login button and click it to submit the form
login_button = driver.find_element(By.ID, "submit")
login_button.click()

# Wait for the page to load after login (you can adjust this as per the site's load time)
time.sleep(3)

# Check if login was successful by looking for specific content on the post-login page
# (Here, we assume the user is redirected to a new page or a success message appears)
# For example, let's check for a specific element on the new page (like a logout button or welcome message):
try:
    success_message = driver.find_element(By.CLASS_NAME, "entry-title")
    print("Login successful! Found element:", success_message.text)
except:
    print("Login failed or page structure changed!")

# Optionally, close the browser after the task
driver.quit()
