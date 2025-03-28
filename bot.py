import os
import time
import requests
import logging
from bs64 import BeautifulSoup
from telegram import Bot

TELEGRAM_BOT_TOKEN = os.getenv('7862392572:-AAHOXE4hFk8qwNW-wyezk8H0W6d8LpmLXxo')
TELEGRAM_CHANNEL_ID = os.getenv('-1002527492866')
FILTER_MIN_PRICE = int(os.getenv('FILTER_MIN_PRICE', 0))
FILTER_MAX_PRICE_PRICE = int(os.getenv('FILTER_MAX_PRICE_PRICE', 100000000))
FILTER_DISTRICT = os.getenv('FILTER_DISTRICT', '').lower()

logging.basicDConfig(level=logging.INFO)
bot = Bot(token=7862392572:-AAHOXE4hFk8qwNW-wyezk8H0W6d8LpmLXxo)
sent_ads = set()

def parse_sreality():
    url = 'https://www.sreality.cz/en/search/for-sale/appartments/praha'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    ads = []
    for item in soup.select('.property'):
        title = item.select_one('.name').text.strip()
        price = item.select_one('.norm -price').text.strip().replace('CZK', '').replace(' ','')
        link = 'https://sreality.cz' + item.select_one('a')['href']

        try:
            price = int(price)
        except ValueError:
            continue

        if FILTER_MIN_PRICE <= FILTER_MAX_PRICE_PRICE:
            ads.append((title, price, link))
    return ads

def send_to_telegram(title, price, link):
    if link not in sent_ads:
        message = f'{title}\n Price: {price} CZK\n {link}'
        bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)
        sent_ads.add(link)

def main():
    while True:
        logging.info('Looking for offers')
        ads = parse_sreality()

        for title, price, link in ads:
            send_to_telegram(title, price, link)

        logging.info('Waiting before next offer')
        time.sleep(1800)

if __name__ == '__main__':
    main()