from bs4 import BeautifulSoup
import re
import requests


def get_bbc_html():
    """Return html from http://www.bbc.co.uk/news"""

    bbc_news = 'http://www.bbc.co.uk'

    r = requests.get(bbc_news + '/news')

    return r.text


def parse_bbc_headlines(bbc_news_html):
    """Return list of headlines from bbc_news_html"""
    headlines = []

    soup = BeautifulSoup(bbc_news_html, 'html.parser')

    headline_class = 'gs-c-promo-heading nw-o-link-split__anchor gs-o-faux-block-link__overlay-link'

    for l in soup.find_all('a', {'class': re.compile(headline_class + '*')}):
        if l.h3:
            if (l['href'][0:1]) == '/':
                headlines.append(l.h3.string)

    return headlines
