#!/usr/local/bin/python3
import news_scraper
import headlines_database
import sys


def main():
    db = sys.argv[1]
    table = sys.argv[2]

    bbc_html = news_scraper.get_bbc_html()
    stories = news_scraper.parse_bbc_headlines(bbc_html)

    headlines_database.add_headlines_to_table(stories, db, table)


if __name__ == '__main__':
    main()
