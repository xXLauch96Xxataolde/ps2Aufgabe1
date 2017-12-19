"""This program is for PS2 1.1

"""

import random
import datetime as dt
import sys
import os
import time
import math


__author__ = "6785468: Robert am Wege, 6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


def dateconvert(date):
    date = str(date)
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])

    weekdays_english = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekdays_german = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    months_english = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    months_german = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

    try:
        weekday_english = weekdays_english[dt.date(year, month, day).weekday()]
    except ValueError:
        return print("No valid date was given.")

    try:
        d = dt.datetime(year, month, day, 12, 00)
    except ValueError:
        return print("No valid date was given.")



    unixtime = time.mktime(d.timetuple())
    unixtime = str(unixtime).split(".")
    unixtime = unixtime[0]

    print(unixtime)


    # german date
    german_weekday



dateconvert(20170222)
