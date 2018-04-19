import unittest

import testing.headlines_database_tests as database
import testing.news_scraper_tests as scraper

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(database))
suite.addTests(loader.loadTestsFromModule(scraper))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
