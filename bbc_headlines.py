import news_scraper
import headlines_database


def main():
    db = 'bbc.db'
    table = 'headlines'

    bbc_html = news_scraper.get_bbc_html()
    stories = news_scraper.parse_bbc_headlines(bbc_html)

    headlines_database.create_headlines_table(db, table)
    headlines_database.add_headlines_to_table(stories, db, table)


if __name__ == '__main__':
    main()
