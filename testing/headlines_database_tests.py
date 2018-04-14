import unittest
import datetime
import os
import headlines_database


class TestHeadlinesDatabase(unittest.TestCase):

    def setUp(self):
        self.db = 'test.db'
        self.table = 'test_table'
        self.today = str(datetime.date.today())

    def tearDown(self):
        os.remove(self.db)

    def testRoundTrip(self):
        headlines = ['headline1', 'headline2', 'headline3']

        expected_result = [(self.today, 'headline1'),
                           (self.today, 'headline2'),
                           (self.today, 'headline3')]

        headlines_database.create_headlines_table(self.db, self.table)
        headlines_database.add_headlines_to_table(headlines, self.db, self.table)

        results = headlines_database.get_headlines_from_table(self.db, self.table)

        headlines_database.drop_headlines_table(self.db, self.table)

        self.assertEqual(results, expected_result)


if __name__ == '__main__':
    unittest.main()
