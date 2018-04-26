#!/usr/bin/python3
from flask import Flask, render_template

import headlines_database

app = Flask(__name__)

db = 'bbc.db'
table = 'headlines'


@app.route('/')
def display_headlines():
    dates = headlines_database.get_dates_from_table(db, table)
    headlines = {}

    for date in dates:
        headlines[date] = headlines_database.get_headlines_on_date(db, table, date)

    if dates:
        return render_template('base_headlines.html', dates=dates, headlines=headlines)
    else:
        return "No headlines in database"


if __name__ == '__main__':
    app.run()
