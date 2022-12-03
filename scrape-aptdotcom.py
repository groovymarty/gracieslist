import requests
import time
import random
from bs4 import BeautifulSoup


def random_delay():
    time.sleep(3+random.random()*5)


places = ["wabasha-county-mn", "rochester-mn"]
for where in places:
    page = 1
    while True:
        if page == 1:
            url = f"https://www.apartments.com/{where}/"
        else:
            url = f"https://www.apartments.com/{where}/{page}/"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}
        print("delaying...")
        random_delay()
        print(f"getting {where} page {page}")
        html_text = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html_text, "html.parser")
        placards = soup.find(id="placards")
        properties = placards.find_all("div", class_="property-info")
        for prop in properties:
            address_div = prop.find("div", class_="property-address")
            beds_div = prop.find("div", class_="bed-range")
            price_div = prop.find("div", class_="price-range")
            if address_div and beds_div and price_div:
                address = address_div.get_text()
                beds = beds_div.get_text()
                price = price_div.get_text()
                link = prop.find("a", class_="property-link").get("href")
                print(f'"{where}","{address}","{beds}","{price}","{link}"')
        page_range = soup.find("span", class_="pageRange")
        if page_range:
            last_page = int(page_range.get_text().split()[-1])
        else:
            last_page = 1
        if page >= last_page:
            break
        else:
            page += 1
