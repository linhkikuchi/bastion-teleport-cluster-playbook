#!/usr/bin/python

# run by crontab
# removes any files in /log/ older than 30 days

from pathlib import Path
import arrow, os

filesPath = "/var/lib/teleport/log/sessions/default"

criticalTime = arrow.now().shift(hours=+5).shift(days=-30)

for item in Path(filesPath).glob('*'):
    if item.is_file():
        itemTime = arrow.get(item.stat().st_mtime)
        if itemTime < criticalTime:
            #remove it
            print ("remove file: "+str(item.absolute()))
            os.remove(str(item.absolute()))