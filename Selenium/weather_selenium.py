from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL of the weather site (example: New York weather page)
url = "https://weather.com/weather/today/l/USNY0996:1:US"  # You can change this to your preferred location
driver.get(url)

# Wait until the page has loaded the necessary data (temperature, condition)
wait = WebDriverWait(driver, 10)
temperature_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="TemperatureValue"]')))
condition_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="wxPhrase"]')))

# Extract the temperature and weather condition
temperature = temperature_element.text
condition = condition_element.text

# Print the results
print(f"Current Temperature: {temperature}")
print(f"Condition: {condition}")

# Optionally, extract more weather details (like wind, humidity, etc.)
wind_element = driver.find_element(By.XPATH, '//*[@data-testid="Wind"]')
humidity_element = driver.find_element(By.XPATH, '//*[@data-testid="PercentageValue"]')

wind = wind_element.text
humidity = humidity_element.text

print(f"Wind: {wind}")
print(f"Humidity: {humidity}")

# Wait a bit before closing (for viewing results)
time.sleep(5)

# Close the browser
driver.quit()
