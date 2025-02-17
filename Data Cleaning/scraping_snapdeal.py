import requests
from bs4 import BeautifulSoup
import csv

def scrape_snapdeal():
    base_url = "https://www.snapdeal.com"
    search_url = f"{base_url}/search?keyword=electronics"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', class_='product-tuple-listing')

    data = []

    for product in products:
        try:
            product_name = product.find('p', class_='product-title').text.strip()
        except AttributeError:
            product_name = "N/A"

        try:
            price = product.find('span', class_='product-price').text.strip()
        except AttributeError:
            price = "N/A"

        try:
            rating_div = product.find('div', class_='filled-stars')
            if rating_div and 'style' in rating_div.attrs:
            rating = rating_div['style'].split(':')[1].strip()
        else:
            rating = "N/A"
        except (AttributeError, KeyError, IndexError):
            rating = "N/A"


        try:
            reviews = product.find('div', class_='product-review').text.strip()
        except AttributeError:
            reviews = "N/A"

        try:
            category = "Electronics"  # Static category based on search query
        except AttributeError:
            category = "N/A"

        try:
            seller_info = product.find('span', class_='product-seller-name').text.strip()
        except AttributeError:
            seller_info = "N/A"

        try:
            discount = product.find('span', class_='product-discount').text.strip()
        except AttributeError:
            discount = "N/A"

        try:
            stock_status = "In Stock" if "Add to Cart" in product.text else "Out of Stock"
        except AttributeError:
            stock_status = "N/A"

        data.append({
            'Product Name': product_name,
            'Price': price,
            'Rating': rating,
            'Reviews': reviews,
            'Category': category,
            'Seller Info': seller_info,
            'Discount': discount,
            'Stock Status': stock_status
        })

    with open('snapdeal_products.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print("Data saved to snapdeal_products.csv")

if __name__ == "__main__":
    scrape_snapdeal()
