from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from parsing import *


def main():
    ua = UserAgent().random
    headers = {'User-Agent': ua}

    chrome_driver_path = r"E:\development prog\chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    item = 'MUNW2201TF'

    result = {}

    result['copa.com.ua'] = get_copa_price(item, headers)
    result['sport-hunter.com.ua'] = get_hunter_price(item, headers)
    result['vkorzinu.biz.ua'] = get_korzina_price(item, headers, driver)
    result['football-world.com.ua'] = get_korzina_2_price(item, headers)
    result['playfootball.com.ua'] = get_playfootball_price(item, headers)
    result['soccer-shop.com.ua'] = get_soccer_shop_price(item, headers)
    result['rozetka.com.ua'] = get_rozetka_price(item, driver)

    driver.quit()

    print(result)

if __name__ == "__main__":
    main()
