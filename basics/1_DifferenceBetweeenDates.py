# coding: utf-8

#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates. 
#

def isLeapYear(year):
    return ((((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0))

def daysInMonth(month, year):
    feb = 29 if (isLeapYear(year)) else 28
    days_in_month = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return days_in_month[month - 1]

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while (year1 != year2 or month1 != month2):
        days += daysInMonth(month1, year1) - day1
        month1 += 1
        day1 = 0

        if (month1 == 13):
            year1 += 1
            month1 = 1
    else: 
        days += day2

    return days


# Test routine

def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()
