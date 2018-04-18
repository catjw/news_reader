from flask import Flask, render_template
import sys

from headlines_database import get_headlines_from_table

app = Flask(__name__)

db = sys.argv[1]
table = sys.argv[2]


@app.route('/')
def display_headlines():
    headlines = get_headlines_from_table(db, table)
    if headlines:
        return render_template('base_headlines.html', headlines=headlines)
    else:
        return "No headlines in database"


if __name__ == '__main__':
    app.run()
