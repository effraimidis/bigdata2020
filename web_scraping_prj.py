from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd

html = urlopen('https://slickdeals.net/')
soup = BeautifulSoup(html.read(), 'html.parser')


items = []
prices = []
shippings = []
for products in soup.findAll('li', {'class':'fpGridBox'}):
    try:
        item = products.find('a', {'class':'itemTitle'})
        items.append(item.text)
    except AttributeError as e:
        continue

    try:
        price = products.find('div', {'class':'itemPrice'})
        p = re.findall(r'\$[0-9]*', price.text)
        if p:
            prices.append(p[0].replace('$',''))
        else:
            prices.append('')
    except AttributeError as e:
        prices.append('')

    try:
        shipping = products.find('div', attrs={'class': 'priceInfo'})
        p = re.findall(r'\+ Free Shipping', shipping.text)
        if p:
            shippings.append(p[0])
        else:
            shippings.append('')
    except AttributeError as e:
        shippings.append('')


df = pd.DataFrame({'Item name': items, 'Price': prices, 'Free Shipping': shippings})
df.to_csv('items.csv', index=False, encoding='utf-8')




