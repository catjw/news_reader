#!/usr/bin/python3.6
from headlines_database import create_headlines_table
import os
import sys

user = os.environ['USERNAME']
db = sys.argv[1]
table = sys.argv[2]

create_headlines_table(db, table)

os.system('python3.6 app.py ' + db + ' ' + table)
