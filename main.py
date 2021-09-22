from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
import time

# Provide link for Zillow
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?userPosition=-79.25638049999999,43.7321214&userPositionBounds=43.7371214,-79.2513805,43.727121399999994,-79.26138049999999&currentLocationSearch=true&searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-79.29011196057127%2C%22east%22%3A-79.22264903942869%2C%22south%22%3A43.71392852180301%2C%22north%22%3A43.7503091706464%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22price%22%3A%7B%22max%22%3A823461%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%7D"
response = requests.get(URL, headers={"Accept-Language": "en-US,en;q=0.9,ml;q=0.8", "Accept-Encoding": "gzip, deflate",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"})
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')

house_addresses = []
house_rent = []
house_link = []

#Scaraping for affordable houses
affordable_house_prices = soup.find_all(name="div", class_="list-card-price")
affordable_house_addresses = soup.find_all(name="address", class_="list-card-addr")
affordable_house_links = soup.find_all(name="a", href=True, class_="list-card-link")

house_addresses = []
house_rent = []
house_link = []

for rent in affordable_house_prices:
    house_rent.append(rent.getText())
for address in affordable_house_addresses:
    house_addresses.append(address.getText())
for link in affordable_house_links:
    house_link.append(link['href'])

print(house_rent)
print(house_addresses)
print(house_link)


chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Automating filling in Google Forms

for n in range(len(house_rent)):

    # Provide link for a Google Forms
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSe-sGdygfZvNwhuNJUBKaxN-HuF7UNJRZahhWGnUBtQ9_24Nw/viewform?usp'
               '=sf_link')
    address_info = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                            '1]/div/div[1]/input')
    address_info.send_keys(house_addresses[n])

    rent_info = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                             '1]/div/div[1]/input')
    rent_info.send_keys(house_rent[n])

    link_info = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
    link_info.send_keys(house_link[n])

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    submit_button.click()