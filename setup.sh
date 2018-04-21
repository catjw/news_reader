#!/usr/bin/env bash

dir=$(pwd)/
db=bbc.db
table=headlines

pip3 install --user -r requirements.txt

./install.py ${dir} ${db} ${table}