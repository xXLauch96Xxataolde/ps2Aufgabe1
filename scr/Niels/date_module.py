"""This program is for PS2 1.2

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
    """Date-Converter

    This function takes a date as input and returns it in four different formats if
    possible
    """
    try:
        date = str(date)
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
    except ValueError:
        return print("Wrong format.")

    # check if years are in intervall
    if year not in range(1800, 2201):
        return print("Date is out of interval.")

    weekdays_english = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekdays_german = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Sonnabend", "Herrntag"]
    months_english = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
    months_german = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                     "November", "Dezember"]

    # check if date is real and assign weekday
    try:
        weekday_english = weekdays_english[dt.date(year, month, day).weekday()]
    except ValueError:
        return print("No valid date was given.")

    # check if date is real and turn into datetime format
    try:
        d = dt.datetime(year, month, day, 13, 00)  # 13 because our time-zone is plus 1
    except ValueError:
        return print("No valid date was given.")

    # turn datetime format into unix format and check if unix format is possible
    try:
        # unix timestamp
        unixtime = time.mktime(d.timetuple())
        unixtime = str(unixtime).split(".")
        unixtime = unixtime[0]
        if int(unixtime) < 0 or int(unixtime) > 2147515200:
            print("Date is not compatible with unix-time.")
        else:
            print(unixtime)
    except OverflowError:
        print("Date is not compatible with unix-time.")

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

    return german_date, british_date, american_date, unixtime


def american_format(date):
    if len(date) == 10:
            date = date[6:] + date[0:2] + date[3:5]
            dateconvert(date)
    else:
        print("No valid date was given.")


def function_format(date):
    dateconvert(date)


def main():
    while True:
        x = input("Please select your preferred input format: 1 for YYYYMMDD or 2 for american date (MM/DD/YYYY).")

        if x == "2":
            date = input("Type your date in your preferred format.")
            american_format(date)
            break

        elif x == "1":
            date = input("Type your date in your preferred format.")
            function_format(date)
            break

        else:
            print("Please enter '1' or '2'")


if __name__ == '__main__':
    main()
