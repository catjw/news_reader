#!/usr/bin/python3
from flask import Flask, render_template

from headlines_database import get_all_headlines_from_table

app = Flask(__name__)

db = 'bbc.db'
table = 'headlines'


@app.route('/')
def display_headlines():
    headlines = get_all_headlines_from_table(db, table)
    if headlines:
        return render_template('base_headlines.html', headlines=headlines)
    else:
        return "No headlines in database"


if __name__ == '__main__':
    app.run()
