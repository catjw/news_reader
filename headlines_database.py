import datetime
import sqlite3


def create_headlines_table(db, table):
    """Creates sqlite3 table in database for storing BBC news headlines if one does not exist"""
    connection = sqlite3.connect(db)
    c = connection.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS {t} (date_added date, headline text)'.format(t=table))

    connection.commit()
    connection.close()


def add_headlines_to_table(headlines, db, table):
    """Inserts list of headlines into table in db with date of insertion"""
    connection = sqlite3.connect(db)
    c = connection.cursor()

    today = str(datetime.date.today())

    for h in headlines:
        c.execute('INSERT INTO {t} VALUES (?,?)'.format(t=table), (today, h))

    connection.commit()
    connection.close()


def get_all_headlines_from_table(db, table):
    """Return all headlines from table"""
    connection = sqlite3.connect(db)
    c = connection.cursor()

    c.execute('SELECT * FROM {t}'.format(t=table))

    headline_list = c.fetchall()

    connection.commit()
    connection.close()

    return headline_list


def get_dates_from_table(db, table):
    """Return list of distinct date tuples from table"""
    connection = sqlite3.connect(db)
    c = connection.cursor()

    c.execute('SELECT DISTINCT date_added FROM {t} ORDER BY date(date_added) DESC'.format(t=table))

    date_list = c.fetchall()

    connection.commit()
    connection.close()

    return date_list


def get_headlines_on_date(db, table, date):
    """Returns list of headline tuples for a specific date tuple"""
    connection = sqlite3.connect(db)
    c = connection.cursor()

    c.execute('SELECT DISTINCT headline FROM {t} WHERE date_added = ?'.format(t=table), date)

    headlines_on_date_list = c.fetchall()

    connection.commit()
    connection.close()

    return headlines_on_date_list


def drop_headlines_table(db, table):
    """Drops sqlite3 table in database for storing BBC news headlines if one does not exist"""
    connection = sqlite3.connect(db)
    c = connection.cursor()

    c.execute('DROP TABLE IF EXISTS {t}'.format(t=table))

    connection.commit()
    connection.close()
