from bs4 import BeautifulSoup
import re
import requests

bbc_news = 'http://www.bbc.co.uk'

r = requests.get(bbc_news + '/news')

soup = BeautifulSoup(r.text, 'html.parser')

for l in soup.find_all('a',
                       {'class': re.compile('gs-c-promo-heading nw-o-link-split__anchor gs-o-faux-block-link__overlay-link*')}):
    if l.h3:
        if (l['href'][0:1]) == '/':
            print(l.h3.string)


