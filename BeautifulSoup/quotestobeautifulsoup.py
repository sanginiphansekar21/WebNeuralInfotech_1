import requests
from bs4 import BeautifulSoup

# URL of the Quotes to Scrape website
url = 'https://quotes.toscrape.com/'

# Send HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(f"Successfully fetched {url}")
else:
    print(f"Failed to fetch {url}, Status code: {response.status_code}")
    exit()

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the quotes on the page
quotes = soup.find_all('div', class_='quote')

# Loop through each quote and extract the necessary information
for quote in quotes:
    # Extract the quote text
    quote_text = quote.find('span', class_='text').text

    # Extract the author of the quote
    author = quote.find('small', class_='author').text

    # Extract the tags associated with the quote (if any)
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]

    # Print the quote, author, and tags
    print(f"Quote: {quote_text}")
    print(f"Author: {author}")
    print(f"Tags: {', '.join(tags)}\n")
