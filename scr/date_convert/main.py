"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

import re
from datetime import datetime
import time
 
__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out" 
__email__ = "your email address" 


def parser(inp):
    pattern_date = "[1|2][8|9|0|1|2][0-9][0-9][0|1][0-9][0-3][0-9]"
    tf = re.match(pattern_date, inp)  # tf = true or false
    return(tf)


def german_day(i):
    day_list = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Sonnabend", "Herrentag"]
    return(day_list[i - 1])


def german_month(i):
    """Please not, my eclipse has problems with umlauts"""
    month_list = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                     "November", "Dezember"]
    return(month_list[i - 1])
    print("asasad")
    
def dateconvert(date):
    german_date = ""
    british_date = ""
    american_date = ""
    unix_date = 0
    d = datetime.strptime(date+"12", '%Y%m%d%H')
    german_date = str(german_day(d.isoweekday())) + ", " + str(d.day) + ". " + str(german_month(d.month)) + " " + str(d.year)
    british_date = d.strftime("%A, %#d %B %Y")
    american_date = d.strftime("%A, %d/%m/%Y")
    unix_date = time.mktime(d.timetuple())
    print(german_date)
    print(british_date)
    print(american_date)
    print(str(unix_date).split(".")[0])
    return (german_date, british_date, american_date, unix_date)


def error():
    print("Error.")
    print("Format allowed: YYYYMMDD.")
    print("Date allowed: 18000101 - 22001231")
    print("\n")


def main():
    while(True):
        print("1) Enter american date format")
        print("2) Enter o.g. funktionsparamter")
        print("Please enter a date")
        inp = input()
        if (inp == 1):
            us_parser()
        if (parser(inp) == None):
            error()        
        else:
            dateconvert(inp)


if __name__ == '__main__':
    main()
