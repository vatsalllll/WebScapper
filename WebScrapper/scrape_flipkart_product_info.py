import requests
from bs4 import BeautifulSoup

headers_custom = header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"}


def scrape_flipkart_product_info(product_page_url):
    """
    This is a website scrapper which scraps the data and fetches it to the user.
    It gives the product name, website name and the price of the product.
    """
    try:
        # Send a request to the URL and get the HTML content
        html_content = requests.get(product_page_url, headers=headers_custom).text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'lxml')

        # Check if the product is available on Flipkart
        if not soup.find('span', class_='B_NuCI'):
            print("Product not found on Flipkart.")
            return None, None, None

        # Extract the product name
        title = soup.find('span', class_='B_NuCI')
        product_name = title.text.strip()

        # Extract the product price
        price_div = soup.find('div', class_='_30jeq3 _16Jk6d')
        price = price_div.text.strip()

        # print(f'The product "{ product_name }" is available at Flipkart for a price of {price}')
        print("Product Name:", product_name)
        print("Website Name:", "Flipkart")
        print("Price:", price)

        return product_name, "Flipkart", price

    except Exception as e:
        print(f"An error occurred while processing the page!! Please find a different product or enter a valid URL: {e}")
        return None, None, None

