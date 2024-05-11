import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def compare_product_prices():
    """
    This function compares product prices from different e-commerce websites.
    It accepts the URL of a product as input, scrapes websites for prices, and
    determines which website offers the product at a lower price.
    """

    # Initialize lists to store product prices, names, and domains
    prices = []
    product_names = []
    website_domains = []

    product_fetched = True

    # Loop through a range of product URLs
    for i in range(1, 3):
        product_url = input("Enter the URL of the product: ")

        # Check if the URL belongs to Flipkart
        if 'flipkart' in product_url:
            from scrape_flipkart_product_info import scrape_flipkart_product_info
            product_name, domain_name, product_price = scrape_flipkart_product_info(product_url)
        # Check if the URL belongs to Amazon
        elif 'amazon' in product_url:
            from amazonScrapper import amazonScrapper
            product_name, domain_name, product_price = amazonScrapper(product_url)
        else:
            print("Please enter a valid URL")
            break

        if product_name is None or domain_name is None or product_price is None:
            product_fetched = False
            print("An error occurred while trying to get product details. Please try again later or try another product.")
            break

        # Append product details to respective lists


        prices.append(product_price)
        product_names.append(product_name)
        website_domains.append(domain_name)


    if not product_fetched:
        return

    # Remove currency symbols and commas from the prices
    for i in range(len(prices)):
        prices[i] = prices[i].replace('₹', '')
        prices[i] = prices[i].replace(',', '')
        prices[i] = prices[i].replace('.', '')

    # Find the minimum price and its index in the list
    min_price = min(prices)
    min_price_index = prices.index(min_price)

    # website_domains[0]="amazon"
    if min_price_index==0:
        print(f'The product "{product_names[min_price_index]}" is available at Amazon for ₹{min_price}')
        
    else:
        print(f'The product "{product_names[min_price_index]}" is available at {website_domains[min_price_index]} for ₹{min_price}')

compare_product_prices()


