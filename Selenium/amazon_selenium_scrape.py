from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
driver.get("https://www.amazon.com/s?k=laptops")
time.sleep(5)  # Wait for the page to load

# Scrape product data
products = []
items = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
for item in items:
    try:
        title = item.find_element(By.XPATH, ".//h2/a").text
        price = item.find_element(By.XPATH, ".//span[@class='a-price']").text
        products.append({"Title": title, "Price": price})
    except:
        continue

# Save to CSV
df = pd.DataFrame(products)
df.to_csv("amazon_products_selenium.csv", index=False)
driver.quit()
print("Data saved to 'amazon_products_selenium.csv'")