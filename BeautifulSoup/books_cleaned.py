import requests
from bs4 import BeautifulSoup
import csv
import re

# Function to clean data
def clean_data(raw_data):
    cleaned_data = []
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    
    for row in raw_data:
        title = row['title']
        # Remove non-numeric characters (except '.') from price
        price = float(re.sub(r'[^\d.]', '', row['price']))  
        availability = 'In stock' in row['availability']  # Convert to boolean
        rating = rating_map.get(row['rating'], 0)  # Convert rating text to number
        
        cleaned_data.append([title, price, availability, rating])
    return cleaned_data

# Function to scrape data from Books to Scrape
def scrape_books_to_csv(base_url, output_file):
    raw_data = []
    page = 1  # Start from the first page
    while True:
        print(f"Scraping page {page}...")
        # Send a request to the current page
        response = requests.get(f"{base_url}/catalogue/page-{page}.html")
        response.encoding = 'utf-8'  # Ensures proper decoding
        
        # Stop if we reach a non-existing page
        if response.status_code != 200:
            print("No more pages to scrape. Exiting.")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all book items on the page
        books = soup.find_all('article', class_='product_pod')

        # Extract data for each book
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text.strip()
            availability = book.find('p', class_='instock availability').text.strip()
            rating = book.p['class'][1]  # Extract the second class (e.g., "Four")

            raw_data.append({
                'title': title,
                'price': price,
                'availability': availability,
                'rating': rating
            })
        
        page += 1  # Go to the next page

    # Clean the raw data
    cleaned_data = clean_data(raw_data)

    # Save cleaned data to a CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price (in £)', 'In Stock', 'Rating (out of 5)'])  # Header row
        writer.writerows(cleaned_data)

    print(f"Cleaned data successfully saved to {output_file}")

# Example usage
base_url = "http://books.toscrape.com"
output_file = "cleaned_books_data.csv"
scrape_books_to_csv(base_url, output_file)
