import requests
from bs4 import BeautifulSoup

header = {
    'user-agent': 'Slinux'
}

BTC = 0
link = 'https://www.okx.com/ru/price/bitcoin-btc'

while True:
    response = requests.get(link, headers=header).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', id="price-detail-header")

    bitcoin_course = block.find_all('div')[0].text

    if bitcoin_course != BTC:
        BTC = bitcoin_course
        print(f"BTC: {BTC}")
    else:
        continue