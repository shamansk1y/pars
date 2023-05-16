import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent().random
headers = {'User-Agent': ua}
ITEM = '400234.331'

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

# football-world
LINK_KORZINA_2 = 'https://football-world.com.ua/ru/search?search='
response = requests.get(LINK_KORZINA_2 + ITEM, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
price_element = soup.find('div', class_='product-cart__price-current product-cart__price-current--red')

if price_element:
    price = price_element.get_text(strip=True)
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

print(result)
