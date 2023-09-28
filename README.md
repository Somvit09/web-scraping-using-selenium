# Amazon Product Scraper

This Python script is designed to scrape product details from Amazon India based on a search query and save the results in a CSV file. It uses Selenium and Chrome WebDriver to automate the web scraping process.

## Setup

### Prerequisites

- Python 3.x
- Chrome browser
- Chrome WebDriver (included in the repository)

### Installation

Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Somvit09/web-scraping-using-selenium.git
   cd the-project-directory
   pip install -r requirements.txt
   python get_product_details.py


Notes

The script uses Selenium with Chrome WebDriver to automate web interactions. Make sure you have Chrome installed and the WebDriver included in the project directory.

Depending on your internet connection and the number of product links to scrape, the script may take some time to complete.

You can customize the URL in the script to search for different products on Amazon India by modifying the url variable in the get_product_details.py file.

Please be aware of Amazon's scraping policies and use this script responsibly and in compliance with Amazon's terms of service.

Objective

The objective of the provided Python script, get_product_details.py, is to scrape product details from Amazon India based on a predefined search query and save the scraped data into a CSV file. Here's a breakdown of its objectives:

Web Scraping: The script uses Selenium, a web automation tool, to interact with the Amazon India website programmatically. It navigates to a specific URL containing search results and collects data from product pages.

Data Collection: The script collects the following product details for each item found in the search results:

  Product Name
  Price
  Seller Name
  Rating
Data Storage: It stores the collected data in a structured format by creating a Pandas DataFrame.

CSV Export: The script exports the DataFrame to a CSV file named product_details_new.csv. This CSV file contains the scraped product data, making it easy to analyze and work with the collected information.

Automated Scraping: The script continues to scrape data until it has processed all the product links on the Amazon page. It includes error handling to ensure that even if some product pages do not have the expected data, the script will continue scraping others.

Reusability: The script is designed to be reusable. You can customize the URL in the script to search for different products on Amazon India by modifying the url variable in the get_product_details.py file.

Overall, the objective of this Python script is to automate the process of gathering product information from Amazon India for a specific search query, making it easier to gather and analyze data from the e-commerce platform.








   
