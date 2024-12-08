import requests
from bs4 import BeautifulSoup
import time

header = {
    'user-agent': 'Slinux'
}

link = 'https://www.okx.com/ru/price/bitcoin-btc'
while True:
    response = requests.get(link, headers=header).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', id="price-detail-header")

    bitcoin_course = block.find_all('div')[0].text
    print("Актуальный курс биткоина:",bitcoin_course)
    time.sleep(60)