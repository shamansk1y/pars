from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from parsing import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def main():
    item = request.form['item']
    ua = UserAgent().random
    headers = {'User-Agent': ua}

    chrome_driver_path = r"E:\development prog\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Запуск в фоновом режиме
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    result = {}

    result['copa.com.ua'] = get_copa_price(item, headers)
    result['sport-hunter.com.ua'] = get_hunter_price(item, headers)
    result['vkorzinu.biz.ua'] = get_korzina_price(item, headers, driver)
    result['football-world.com.ua'] = get_korzina_2_price(item, headers)
    result['playfootball.com.ua'] = get_playfootball_price(item, headers)
    result['soccer-shop.com.ua'] = get_soccer_shop_price(item, headers)
    result['rozetka.com.ua'] = get_rozetka_price(item, driver)
    result['epicentrk.ua'] = get_epic_price(item, headers)
    result['kasta.ua'] = get_kasta_price(item, headers)
    result['eobuv.com.ua'] = get_eobuv_price(item, headers)

    driver.quit()

    return render_template('result.html', result=result, item=item)

if __name__ == "__main__":
    app()
