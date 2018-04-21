# News Reader

A program to retrieve BBC News headlines daily (at midday), store them in a database and then allow the user access via a web page

### Prerequisites

Python3 located in /usr/bin/ and pip

Python library requirements are detailed in [requirements.txt](requirements.txt)

### Installing

run [setup.sh](setup.sh) from the project root directory

```bash
./setup.sh
```
This will:
* Install the python modules in [requirements.txt](README.md)
* Install [bbc_headlines.py](bbc_headlines.py) to the users crontab, to run at 1200 hrs
* Run [app.py](app.py) so the headlines can be viewed

### Web App
The web app is initially run via [setup.sh](setup.sh), but can be restarted by running [app.py](app.py)
```bash
./app.py
```
The web can be viewed here [http://localhost:5000](http://localhost:5000)

## Running the tests

run [test_runner.py](test_runner.py) to run both of the unittests, these test the parsing of the html page and the creation and insertion 
of data to the database

```bash
./test_runner.py
```

