#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# python program to check if the input year is a leap year or not

year = 2000

# to get year (integer input)from the user
# year = input(input("enter a year"))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

