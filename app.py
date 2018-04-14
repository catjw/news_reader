from flask import Flask, render_template

from headlines_database import get_headlines_from_table

app = Flask(__name__)

db = 'test.db'
table = 'one'


@app.route('/')
def display_headlines():
    return render_template('base_headlines.html', headlines=get_headlines_from_table(db, table))


if __name__ == '__main__':
    app.run()
