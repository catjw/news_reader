# News Reader

A program to retrieve BBC News headlines daily (at midday), store them in a database and then allow the user access via a web page

### Prerequisites

Python 3.6 located in /usr/local/bin/ and pip

Python library requirements are detailed in [requirements.txt]

### Installing

run setup.sh from the project root directory

```
./setup.sh
```

## Running the tests

run test_runner.py to run both of the unittests, these test the parsing of the html page and the creation and insertion 
of data to the database

```angular2html
python3.6 test_runner.py
```