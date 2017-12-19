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
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekdays_german = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    try:
        weekday = weekdays[dt.date(year, month, day).weekday()]
    except ValueError:
        return print("No valid date was given.")
    month = months[month - 1]

    print(str(weekday) + ",", str(day) + ".", month, year)


dateconvert(20170230)
