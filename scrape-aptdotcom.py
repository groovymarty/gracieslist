import requests
from bs4 import BeautifulSoup

where = "wabasha-county-mn"

url = f"https://www.apartments.com/{where}/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}

html_text = requests.get(url, headers=headers).text
soup = BeautifulSoup(html_text, "html.parser")
placards = soup.find(id="placards")
properties = placards.find_all("div", class_="property-info")
for prop in properties:
    address = prop.find("div", class_="property-address").get_text()
    beds = prop.find("div", class_="bed-range").get_text()
    price = prop.find("div", class_="price-range").get_text()
    link = prop.find("a", class_="property-link").get("href")
    print(f'"{where}","{address}","{beds}","{price}","{link}"')
