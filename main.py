import requests
import time, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# initializing driver
driver_path = Service('chromedriver')
driver = webdriver.Chrome(service=driver_path)
# getting the website
driver.get('https://haveibeenpwned.com/')
# finding the input box in which email id is to be searched
input_box = driver.find_element(By.ID, "Account")
# search button
search_box = driver.find_element(By.ID, 'searchPwnage')
# taking the mail id from the user
email_id = input('Enter the email id - ')
# sending keys to the input box
input_box.send_keys(email_id)
# sending keys to the button
search_box.send_keys(Keys.ENTER)
time.sleep(0.01)
# pawned_details = driver.find_element(By.CLASS_NAME, 'pwnedCompanyTitle')
# print(pawned_details)
# for i in pawned_details:
#     print(i.getText())
# print(pawned_details.text)
time.sleep(300)
driver.quit()