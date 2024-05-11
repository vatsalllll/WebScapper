from bs4 import BeautifulSoup
import requests

# Define custom user-agent to mimic a web browser
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}

def amazonScrapper(url):
    """
    This is a website scrapper which scraps the data and fetches it to the user.
    It gives the product name, website name and the price of the product.
    """

    try:
        # Send an HTTP request to the URL and retrieve the HTML content
        html_text = requests.get(url, headers=headers).text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_text, 'lxml')

        # Check if the product is available
        if not soup.find('div', class_='a-alert-content'):
            print("The product is not listed on Amazon")
            return None, None, None

        # Extract the product name
        title_div = soup.find('div', id='titleSection')
        title_h1 = title_div.find('h1', id='title').text.strip()
        product_name = title_h1

        # Check if the product name is available
        if product_name is None:
            print("Failed to retrieve the product name. Please try again or choose another product.")
            return None, None, None

        # Extract the product price
        price_span = soup.find('span', class_='a-price-whole')
        price = price_span.text.strip()

        # Check if the price is available
        if price is None:
            print("Product price is not available. Please try another product.")
            return None, None, None

        # Extract the website name
        website_name = soup.find('title')
        website_name = website_name.text.strip().split(' ')[-1]

        # Check if the website name is available
        if website_name is None:
            print("Website name is not available. Please try another name or product.")
            return None, None, None

        # Print the product name, website name, and price
        print("Product Name:", product_name)
        print("Website Name:", "Amazon")
        print("Price:", price)

        return product_name, website_name, price

    except Exception as e:
        print(f"An error occurred while processing the page!! Please find a different product or enter a valid URL: {e}")
        return None, None, None




