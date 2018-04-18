#!/usr/bin/env bash

dir=$(pwd)
db=${dir}/bbc.db
table=headlines

pip3 install -r requirements.txt

(crontab -l 2>/dev/null; echo "0 12 * * * ${dir}/headlines_cron.sh ${dir} ${db} ${table}") | crontab -

./install.py ${db} ${table}