import unittest
import datetime
import os
import sqlite3
import headlines_database


class TestHeadlinesDatabase(unittest.TestCase):

    def setUp(self):
        """Set up temporary test database and table"""
        self.db = 'test.db'
        self.table = 'test_table'
        self.today = str(datetime.date.today())

        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS {t} (date_added DATE, headline text)'.format(t=self.table))

        headlines = [('2018-04-20', 'headline1'),
                     ('2018-04-20', 'headline2'),
                     ('2018-04-20', 'headline2'),
                     ('2018-04-21', 'headline3'),
                     ('2018-04-21', 'headline4'),
                     ('2018-04-22', 'headline5'),
                     ('2018-04-22', 'headline6')]

        self.cursor.executemany('INSERT INTO {t} VALUES (?,?)'.format(t=self.table), headlines)
        self.connection.commit()

    def tearDown(self):
        """Removes temporary database"""
        self.connection.close()
        os.remove(self.db)

    def test_create_table(self):
        table = 'create_test_table'
        headlines_database.create_headlines_table(self.db, table)
        expected_result = [('create_test_table',),
                           ('test_table',)]

        self.cursor.execute('SELECT name FROM sqlite_master WHERE type = "table" ORDER BY name')
        result = self.cursor.fetchall()
        self.connection.commit()

        self.assertEqual(expected_result, result)

    def test_drop_table(self):
        table = 'create_test_table'
        headlines_database.drop_headlines_table(self.db, table)
        expected_result = [('test_table',)]

        self.cursor.execute('SELECT name FROM sqlite_master WHERE type = "table" ORDER BY name')
        result = self.cursor.fetchall()
        self.connection.commit()

        self.assertEqual(expected_result, result)

    def test_add_one_headline(self):
        headline = ('headline0',)
        headlines_database.add_headlines_to_table(headline, self.db, self.table)
        expected_result = ('headline0',)

        self.cursor.execute('SELECT headline FROM {t} WHERE date_added = ?'.format(t=self.table), (self.today,))
        result = self.cursor.fetchone()
        self.connection.commit()

        self.assertEqual(expected_result, result)

    def test_add_multiple_headlines(self):
        headlines = ['headline10',
                     'headline11',
                     'headline12']
        headlines_database.add_headlines_to_table(headlines, self.db, self.table)
        expected_result = [('headline10',),
                           ('headline11',),
                           ('headline12',)]

        self.cursor.execute('SELECT headline FROM {t} WHERE date_added = ?'.format(t=self.table), (self.today,))
        result = self.cursor.fetchall()
        self.connection.commit()

        self.assertEqual(expected_result, result)

    def test_get_dates_from_table(self):
        expected_result = [('2018-04-22',),
                           ('2018-04-21',),
                           ('2018-04-20',)]

        result = headlines_database.get_dates_from_table(self.db, self.table)

        self.assertEqual(expected_result, result)

    def test_get_headlines_on_date(self):
        date = ('2018-04-20',)
        expected_result = [('headline1',),
                           ('headline2',)]

        result = headlines_database.get_headlines_on_date(self.db, self.table, date)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
