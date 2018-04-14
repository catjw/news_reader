import datetime
import sqlite3


def create_headlines_table(db, table):
    """Drops then creates sqlite3 table in database for storing BBC news headlines"""
    connection = sqlite3.connect(db)
    c = connection.cursor()

    c.execute('DROP TABLE {t}'.format(t=table))
    c.execute('CREATE TABLE {t} (date_added date, headline text)'.format(t=table))

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


def get_headlines_from_table(db, table):
    """Return headlines from table"""
    connection = sqlite3.connect(db)
    c = connection.cursor()

    c.execute('SELECT * FROM {t}'.format(t=table))

    headline_list = c.fetchall()

    connection.commit()
    connection.close()

    return headline_list


values = ['headline one',
          'heres another one',
          'surprise its number 3']

create_headlines_table('test', 'one')
add_headlines_to_table(values, 'test', 'one')
hl = get_headlines_from_table('test', 'one')

for h in hl:
    print(h)

