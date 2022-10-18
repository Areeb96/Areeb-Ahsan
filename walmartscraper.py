from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver
from csv import writer
import pdb
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import csv

#driver = webdriver.Chrome()
url= "https://www.walmart.ca/en/stores-near-me"
page = requests.get(url)



soup = BS(page.content, 'html.parser')
#storeList = soup.find_all('div', class_='sfa-main-body__list-view--active')
storeList = soup.find_all('div', class_='sfa-store-list-item sfa-store-list-item')

sleep(5)
with open('stores.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Address','Name']
    thewriter.writerow(header)

    for list in storeList:
        name = list.find('p', class_="sfa-store-list-item__content").text.replace('\n', '')
        address = list.find('h2', class_="sfa-store-list-item__name").text.replace('\n', '')        
        info = [name, address]
        thewriter.writerow(info)
        print(info)

#driver.close()

