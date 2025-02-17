from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Selenium WebDriver (e.g., using ChromeDriver)
driver = webdriver.Chrome()  # Ensure you have the correct WebDriver installed

try:
    # Open the Wikipedia homepage
    driver.get("https://www.wikipedia.org/")
    time.sleep(2)  # Wait for the page to load

    # Find the search input field
    search_box = driver.find_element(By.ID, "searchInput")
    
    # Enter the search term and press Enter
    search_term = "Web scraping"
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)  # Wait for the results page to load

    # Scrape the first paragraph of the article
    first_paragraph = driver.find_element(By.XPATH, "//p[not(@class)]").text
    print("First Paragraph:\n", first_paragraph)

    # Optionally, scrape the title of the page
    title = driver.find_element(By.ID, "firstHeading").text
    print("\nPage Title:", title)

finally:
    # Close the browser
    driver.quit()
