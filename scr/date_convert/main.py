"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

import re
from datetime import datetime
 
__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out" 
__email__ = "your email address" 


def parser(inp):
    pattern_date = "[1|2][8|9|0|1|2][0-9][0-9][0|1][0-9][0-3][0-9]"
    tf = re.match(pattern_date, inp)  # tf = true or false
    return(tf)


def dateconvert(date):
    german_date = ""
    british_date = ""
    american_date = ""
    unix_date = 0
    d = datetime.strptime(date, '%Y%m%d')
    date_string = d.strftime('%Y%m%d')
    print(date_string)
    return (german_date, british_date, american_date, unix_date)


def error():
    print("Error.")
    print("Format allowed: YYYYMMDD.")
    print("Date allowed: 18000101 - 22001231")
    print("\n")


def main():
    while(True):
        print("Please enter a date")
        inp = input()
        if (parser(inp) == None):
            error()        
        else:
            dateconvert(inp)
    

if __name__ == '__main__':
    main()
