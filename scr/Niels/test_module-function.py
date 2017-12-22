"""This program is for PS2 1.1

"""

import doctest
import random
import datetime as dt
import sys
import os
import time
import math

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "niels.heissel@stud.uni-frankfurt.de"


def dateconvert(date):
    """This procedure converts dates.

    It takes a date in format YYYYMMDD and retruns it in american, british,
    german and unix time-format.

    >>> dateconvert(20000910)
    968583600
    Herrntag, 10. September 2000
    Sunday, 10 September 2000
    Sunday, 10/09/2000

    >>> dateconvert(20160719)
    1468926000
    Dienstag, 19. Juli 2016
    Tuesday, 19 July 2016
    Tuesday, 19/07/2016


    >>> dateconvert(20000229)
    951825600
    Dienstag, 29. Februar 2000
    Tuesday, 29 February 2000
    Tuesday, 29/02/2000

    >>> dateconvert("2000-09-10")
    Wrong format.

    >>> dateconvert("09102000")
    Date is out of interval.

    >>> dateconvert(2000910)
    No valid date was given.

    >>> dateconvert(17991231)
    Date is out of interval.

    >>> dateconvert(18000101)
    Date is not compatible with unix-time.
    Mittwoch, 1. Januar 1800
    Wednesday, 1 January 1800
    Wednesday, 01/01/1800

    >>> dateconvert(22010101)
    Date is out of interval.

    >>> dateconvert(22001231)
    Date is not compatible with unix-time.
    Mittwoch, 31. Dezember 2200
    Wednesday, 31 December 2200
    Wednesday, 31/12/2200

    >>> dateconvert(20050018)
    No valid date was given.

    >>> dateconvert(20050118)
    1106049600
    Dienstag, 18. Januar 2005
    Tuesday, 18 January 2005
    Tuesday, 18/01/2005

    >>> dateconvert(20011307)
    No valid date was given.

    >>> dateconvert(20011207)
    1007726400
    Freitag, 7. Dezember 2001
    Friday, 7 December 2001
    Friday, 07/12/2001

    >>> dateconvert(20040700)
    No valid date was given.

    >>> dateconvert(20040701)
    1088679600
    Donnerstag, 1. Juli 2004
    Thursday, 1 July 2004
    Thursday, 01/07/2004

    >>> dateconvert(20040631)
    No valid date was given.

    >>> dateconvert(20040630)
    1088593200
    Mittwoch, 30. Juni 2004
    Wednesday, 30 June 2004
    Wednesday, 30/06/2004

    >>> dateconvert(20040732)
    No valid date was given.

    >>> dateconvert(20040731)
    1091271600
    Sonnabend, 31. Juli 2004
    Saturday, 31 July 2004
    Saturday, 31/07/2004

    >>> dateconvert(19990229)
    No valid date was given.

    >>> dateconvert(19990228)
    920203200
    Herrntag, 28. Februar 1999
    Sunday, 28 February 1999
    Sunday, 28/02/1999

    >>> dateconvert(20200230)
    No valid date was given.

    >>> dateconvert(20200229)
    1582977600
    Sonnabend, 29. Februar 2020
    Saturday, 29 February 2020
    Saturday, 29/02/2020

    >>> dateconvert(19691231)
    Date is not compatible with unix-time.
    Mittwoch, 31. Dezember 1969
    Wednesday, 31 December 1969
    Wednesday, 31/12/1969

    >>> dateconvert(19700101)
    43200
    Donnerstag, 1. Januar 1970
    Thursday, 1 January 1970
    Thursday, 01/01/1970

    >>> dateconvert(20380120)
    Date is not compatible with unix-time.
    Mittwoch, 20. Januar 2038
    Wednesday, 20 January 2038
    Wednesday, 20/01/2038

    >>> dateconvert(20380119)
    2147515200
    Dienstag, 19. Januar 2038
    Tuesday, 19 January 2038
    Tuesday, 19/01/2038


    >>> dateconvert(18000101)
    Date is not compatible with unix-time.
    Mittwoch, 1. Januar 1800
    Wednesday, 1 January 1800
    Wednesday, 01/01/1800

    >>> dateconvert(18000100)
    No valid date was given.

    >>> dateconvert(17990101)
    Date is out of interval.
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


doctest.testmod()

dateconvert(180001-0-1)
