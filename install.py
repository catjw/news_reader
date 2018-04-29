#!/usr/bin/python3
from headlines_database import create_headlines_table
import os
import sys
from crontab import CronTab

project_dir = sys.argv[1]
db = project_dir + sys.argv[2]
table = sys.argv[3]
cron_command = '%sbbc_headlines.py %s %s' % (project_dir, db, table)

create_headlines_table(db, table)

user_cron = CronTab(user=True)
job = user_cron.new(command=cron_command)
job.minute.on(0)
job.hour.on(12)
user_cron.write()

os.system('./app.py')
