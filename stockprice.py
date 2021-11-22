import requests
from bs4 import BeautifulSoup
import json

mystocks = ["AMD", "GME", "INTC",]
stockdata = []

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
    'symbol': symbol,
    'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
    'change' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text,
    }
    return stock

for item in mystocks:
    stockdata.append(getData(item))
    print("Getting: ", item)

print(stockdata)

with open("stockdata.json", "w") as f:
    json.dump(stockdata, f)
    


