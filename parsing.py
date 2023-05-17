import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By


def get_copa_price(item, headers):
    link = f'https://www.copa.com.ua//index.php?route=product/search&search={item}'
    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    price_element = soup.find(class_='price')

    if price_element:
        if price_element.find('span', class_='price-new'):
            price = price_element.find('span', class_='price-new').get_text(strip=True)
        else:
            price = price_element.get_text(strip=True)
        return price
    else:
        return "Цена не найдена"

def get_hunter_price(item, headers):
    link = f'https://sport-hunter.com.ua/uk/index.php?route=product/search&search={item}'
    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    price_element = soup.find(class_='product-card__price')

    if price_element:
        if price_element.find('span', class_='newprice'):
            price = price_element.find('span', class_='newprice').get_text(strip=True)
        else:
            price = price_element.get_text(strip=True)
        return price
    else:
        return "Цена не найдена"

def get_korzina_price(item, headers, driver):
    url = "https://vkorzinu.biz.ua/"
    driver.get(url)

    search_input = driver.find_element(By.ID, "mod-search-searchword")
    search_input.send_keys(item)

    search_input.submit()
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, "html.parser")
    first_result_link = soup.select_one("dl.search-results > dt.result-title > a")

    href = first_result_link["href"]
    response = requests.get(href, headers=headers).text
    soup = BeautifulSoup(response, "html.parser")
    price_element = soup.find_all("span", class_="hikashop_product_price hikashop_product_price_0 hikashop_product_price_with_discount")[1].text
    if price_element:
        return price_element
    else:
        return "Цена не найдена"

def get_korzina_2_price(item, headers):
    link = f'https://football-world.com.ua/ru/search?search={item}'
    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    price_element = soup.find('div', class_='product-cart__price-current product-cart__price-current--red')
    price_element_2 = soup.find('div', class_='product-cart__price-current')

    if price_element:
        price = price_element.get_text(strip=True)
    elif price_element_2:
        price = price_element_2.get_text(strip=True)
    else:
        price = "Цена не найдена"
    return price

def get_playfootball_price(item, headers):
    link = f'https://playfootball.com.ua/shop/search?text={item}'
    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    price_element = soup.find('span', class_='product-price__main-value')

    if price_element:
        price = price_element.get_text(strip=True)
    else:
        price = "Цена не найдена"
    return price

def get_soccer_shop_price(item, headers):
    link = f'https://soccer-shop.com.ua/ua/advanced_search_result.php?keywords={item}'
    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    price_element = soup.find('span', class_='price sale')

    if price_element:
        price = price_element.get_text(strip=True)
        price = price.replace('\xa0', '')
    else:
        price = "Цена не найдена"
    return price

def get_rozetka_price(item, driver):
    driver.get(f"https://rozetka.com.ua/search/?text={item}")
    time.sleep(7)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    price_element = soup.find('span', class_='goods-tile__price-value')

    if price_element:
        price = price_element.get_text(strip=True)
        price = price.replace('\xa0', '')
    else:
        price = "Цена не найдена"
    return price


def get_epic_price(item, headers):
    link = f'https://epicentrk.ua/ua/search/?q={item}&sort=asc'
    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    price_element = soup.find('span', class_='card__price-sum')
    if price_element:
        price = price_element.get_text(strip=True)
    else:
        price = "Цена не найдена"
    return price


def get_kasta_price(item, headers):
    link = f'https://kasta.ua/uk/search/?q={item}&sort=price-asc'
    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    price_element = soup.find('span', class_='product_item__new-cost')
    if price_element:
        string = price_element.get_text(strip=True)
        price = string.encode('latin-1').decode('utf-8')
    else:
        price = "Цена не найдена"
    return price


def get_eobuv_price(item, headers):
    link = f'https://eobuv.com.ua/s/{item}?q={item}'
    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    price_element = soup.find('div', class_='price-final')
    if price_element:
        string = price_element.get_text(strip=True)
        price = string.replace('\xa0', ' ').strip()
    else:
        price = "Цена не найдена"
    return price