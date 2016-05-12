#!/usr/bin/env python

"""
Project Euler Problem 19
========================

   You are given the following information, but you may prefer to do some
   research for yourself.

     • 1 Jan 1900 was a Monday.
     • Thirty days has September,
       April, June and November.
       All the rest have thirty-one,
       Saving February alone,
       Which has twenty-eight, rain or shine.
       And on leap years, twenty-nine.
     • A leap year occurs on any year evenly divisible by 4, but not on a
       century unless it is divisible by 400.

   How many Sundays fell on the first of the month during the twentieth
   century (1 Jan 1901 to 31 Dec 2000)?

Reasoning
---------
    We can just focus on the offsets and the leap years and count the Sundays
    which are encoded as 6. Using datetime libary simplifies everything
    significantly
"""

__solution__ = "a4a042cf4fd6bfb47701cbc8a1653ada"

from datetime import date

def count_sundays():
    def is_leap(y):
        return ((y % 4 == 0) and not (y % 100 == 0)) or (y % 400 == 0)
    day = 0+1 # We start at 1901 and we are given 1900 which is not leap
    month_offset = [31,28,31,30,31,30,31,31,30,31,30,31]
    years = range(1901,2000+1)

    sundays_first = 0
    
    for y in years:
        for m in range(12):
            if day == 6:
                sundays_first += 1
            if m == 1:
                day += int(is_leap(y))
            day = (day+month_offset[m]) % 7
    return sundays_first

def count_sundays2():
    return sum([date(year,month,1).weekday() for month in range(1,12+1)].count(6) for year in range(1901,2000+1) )

if __name__ == '__main__':
    print(count_sundays())


