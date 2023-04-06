import requests
import time, json, pandas as pd, numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# initializing driver
driver_path = Service('chromedriver')
driver = webdriver.Chrome(service=driver_path)

# url 
url = 'https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar'

# getting the website
driver.get(url=url)

# getting all the links from the images of the products 
images = driver.find_elements(By.CLASS_NAME, 's-no-outline')

# creating a list to save all the links of the products
all_product_links = []
for i in images:
    if i.get_attribute('href'):
        all_product_links.append(i.get_attribute('href'))

# creating lists to store product data
product_titles, product_ratings, product_prices, product_sellers = [], [], [], []


# for the error that occurs we have a solution that we run the loop until it scrapes all the data 
# all the links.

# making a scraping function
def scrape():

    # initialized count variable
    count = 0
    
    # loop through the links to particularly scrape data from products
    for i in all_product_links:
        # getting the link
        driver.get(i)
        # scraping the information
        product_title = driver.find_element(By.ID, 'title').text
        product_rating = driver.find_element(By.XPATH, '//*[@id="reviewsMedley"]/div/div[1]/span[1]/span/div[3]/span').text[:-14]
        product_price = driver.find_element(By.CLASS_NAME, '_p13n-desktop-sims-fbt_price_p13n-sc-price__bCZQt').text
        product_seller = driver.find_element(By.ID, 'merchant-info').text[8:][:-25]
        # adding those to the list
        product_titles.append(product_title)
        product_prices.append(product_price)
        product_ratings.append(product_rating)
        product_sellers.append(product_seller)
        count += 1

    # creating a dataframe using pandas
    dataframe = pd.DataFrame({'Product Name': product_titles, 
                            'Price': product_prices,
                            'Seller Name': product_sellers,
                            'Rating': product_ratings
                            })

    # making csv file
    csv_file = dataframe.to_csv('product_details.csv')

    # closing the driver
    driver.quit()
    return count

scrape_count = scrape()
while scrape_count != len(all_product_links):
    scrape_count = scrape()
    if scrape_count == len(all_product_links):
        break


