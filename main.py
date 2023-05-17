import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By

ua = UserAgent().random
headers = {'User-Agent': ua}


chrome_driver_path = r"E:\development prog\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

ITEM = 'MUNW2201TF'

result = {}

# COPA
LINK_COPA = 'https://www.copa.com.ua//index.php?route=product/search&search='
response = requests.get(LINK_COPA + ITEM, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
price_element = soup.find(class_='price')

if price_element:
    if price_element.find('span', class_='price-new'):
        price = price_element.find('span', class_='price-new').get_text(strip=True)
    else:
        price = price_element.get_text(strip=True)
    result['copa.com.ua'] = price
else:
    result['copa.com.ua'] = "Цена не найдена"

# HUNTER
LINK_HUNTER = 'https://sport-hunter.com.ua/uk/index.php?route=product/search&search='
response = requests.get(LINK_HUNTER + ITEM, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
price_element = soup.find(class_='product-card__price')

if price_element:
    if price_element.find('span', class_='newprice'):
        price = price_element.find('span', class_='newprice').get_text(strip=True)
    else:
        price = price_element.get_text(strip=True)
    result['sport-hunter.com.ua'] = price
else:
    result['sport-hunter.com.ua'] = "Цена не найдена"


# KORZINA

url = "https://vkorzinu.biz.ua/"
driver.get(url)

search_input = driver.find_element(By.ID, "mod-search-searchword")
search_input.send_keys(ITEM)

search_input.submit()
page_source = driver.page_source

soup = BeautifulSoup(page_source, "html.parser")
first_result_link = soup.select_one("dl.search-results > dt.result-title > a")

href = first_result_link["href"]
response = requests.get(href, headers=headers).text
soup = BeautifulSoup(response, "html.parser")
price_element = soup.find_all("span", class_="hikashop_product_price hikashop_product_price_0")[1].text
if price_element:
    result['vkorzinu.biz.ua'] = price_element
else:
    result['vkorzinu.biz.ua'] = "Цена не найдена"



# football-world
LINK_KORZINA_2 = 'https://football-world.com.ua/ru/search?search='
response = requests.get(LINK_KORZINA_2 + ITEM, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
price_element = soup.find('div', class_='product-cart__price-current product-cart__price-current--red')
price_element_2 = soup.find('div', class_='product-cart__price-current')
if price_element:
    price = price_element.get_text(strip=True)
    result['football-world.com.ua'] = price
elif price_element_2:
    price = price_element_2.get_text(strip=True)
    result['football-world.com.ua'] = price
else:
    result['football-world.com.ua'] = "Цена не найдена"

# playfootball.com.ua
LINK_PF = 'https://playfootball.com.ua/shop/search?text='
response = requests.get(LINK_PF + ITEM, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
price_element = soup.find('span', class_='product-price__main-value')

if price_element:
    price = price_element.get_text(strip=True)
    result['playfootball.com.ua'] = price
else:
    result['playfootball.com.ua'] = "Цена не найдена"


# soccer-shop.com.ua
LINK_SC = 'https://soccer-shop.com.ua/ua/advanced_search_result.php?keywords='
response = requests.get(LINK_SC + ITEM, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
price_element = soup.find('span', class_='price sale')

if price_element:
    price = price_element.get_text(strip=True)
    price = price.replace('\xa0', '')  # Удаление неразрывного пробела
    result['soccer-shop.com.ua'] = price
else:
    result['soccer-shop.com.ua'] = "Цена не найдена"

# rozetka.com.ua
driver.get("https://rozetka.com.ua/search/?text=" + ITEM)

time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
price_element = soup.find('span', class_='goods-tile__price-value')

if price_element:
    price = price_element.get_text(strip=True)
    price = price.replace('\xa0', '')
    result['rozetka.com.ua'] = price
else:
    result['rozetka.com.ua'] = "Цена не найдена"

driver.quit()


print(result)
