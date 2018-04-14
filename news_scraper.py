from bs4 import BeautifulSoup
import re
import requests


def get_bbc_headlines():
    """Return list of headlines from http://www.bbc.co.uk/news"""
    headlines = []

    bbc_news = 'http://www.bbc.co.uk'
    headline_class = 'gs-c-promo-heading nw-o-link-split__anchor gs-o-faux-block-link__overlay-link'

    r = requests.get(bbc_news + '/news')
    soup = BeautifulSoup(r.text, 'html.parser')

    for l in soup.find_all('a', {'class': re.compile(headline_class + '*')}):
        if l.h3:
            if (l['href'][0:1]) == '/':
                headlines.append(l.h3.string)

    return headlines


for h in get_bbc_headlines():
    print(h)
