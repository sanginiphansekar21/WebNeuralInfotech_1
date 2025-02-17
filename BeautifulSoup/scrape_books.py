import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data from Books to Scrape
def scrape_books_to_csv(base_url, output_file):
    # Prepare the CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Availability', 'Rating'])  # Header row

        page = 1  # Start from the first page
        while True:
            print(f"Scraping page {page}...")
            # Send a request to the current page
            response = requests.get(f"{base_url}/catalogue/page-{page}.html")
            
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

                writer.writerow([title, price, availability, rating])  # Write row to CSV
            
            page += 1  # Go to the next page

    print(f"Data successfully saved to {output_file}")

# Example usage
base_url = "http://books.toscrape.com"
output_file = "books_data.csv"
scrape_books_to_csv(base_url, output_file)
