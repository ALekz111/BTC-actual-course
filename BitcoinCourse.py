import requests
from bs4 import BeautifulSoup
import datetime

header = {
    'user-agent': 'Slinux'
}

BTC = 0
link = 'https://www.okx.com/ru/price/bitcoin-btc'

print("[₿] Actual Bitcoin Course:\n")
while True:
    now = datetime.datetime.now()
    response = requests.get(link, headers=header).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', id="price-detail-header")

    bitcoin_course = block.find_all('div')[0].text

    if bitcoin_course != BTC:
        BTC = bitcoin_course
        print(f"BTC - [{now.strftime("%d-%m-%Y %H:%M")}] : {BTC}\n")
    else:
        continue