"""This program is for PS2 1.1

"""

import datetime as dt
import sys
import os
import time

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "niels.heissel@stud.uni-frankfurt.de"


def dateconvert(date):
    date = str(date)
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])

    weekdays_english = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekdays_german = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Sonnabend", "Herrentag"]
    months_english = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
    months_german = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                     "November", "Dezember"]

    try:
        weekday_english = weekdays_english[dt.date(year, month, day).weekday()]
    except ValueError:
        return print("No valid date was given.")

    try:
        d = dt.datetime(year, month, day, 12, 00)
    except ValueError:
        return print("No valid date was given.")

    # unix timestamp
    unixtime = time.mktime(d.timetuple())
    unixtime = str(unixtime).split(".")
    unixtime = unixtime[0]

    print(unixtime)

    # german date
    german_weekday = str(weekdays_german[dt.date(year, month, day).weekday()])
    german_month = str(months_german[month - 1])
    german_date = german_weekday + ", " + str(day) + ". " + german_month + " " + str(year)

    print(german_date)

    # british date
    british_month = months_english[month - 1]
    british_date = weekday_english + ", " + str(day) + " " + british_month + " " + str(year)

    print(british_date)

    # american date
    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)
    american_date = weekday_english + ", " + str(day) + "/" + str(month) + "/" + str(year)

    print(american_date)


def main():
    x = input("Type 1 for american date input or 2 for normal input.")
    date = input("Type your date in your special format.")

    if x == "1":
        if len(date) == 10:
            date = date[6:] + date[0:2] + date[3:5]
            dateconvert(date)
        else:
            print("No valid date was given.")

    elif x == "2":
        dateconvert(date)


if __name__ == '__main__':
    main()
