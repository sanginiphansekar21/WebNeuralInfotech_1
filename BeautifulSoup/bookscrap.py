import requests
from bs4 import BeautifulSoup

# URL of the website
url = "http://books.toscrape.com"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the book containers (each book is inside a div with class 'product_pod')
    books = soup.find_all('article', class_='product_pod')

    # Loop through each book and extract the required information
    for book in books:
        # Extract the title of the book
        title = book.find('h3').find('a').get('title')
        
        # Extract the price of the book
        price = book.find('p', class_='price_color').text
        
        # Extract the availability (if the book is in stock)
        availability = book.find('p', class_='instock availability').text.strip()
        
        # Print the extracted information
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Availability: {availability}")
        print("-" * 30)
else:
    print("Failed to retrieve the webpage.")
