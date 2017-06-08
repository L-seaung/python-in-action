#!/usr/bin/env python3
# -*- coding:utf-8 -*-
kilomenters = 5.5

# to take kilomenters from the user, uncomment the code below

kilometers = input("enter value in kilometers")

# conversion factor
conv_fac = 0.621371

# calculate miles

miles = kilometers * conv_fac
print("%0.3f kilomenters is equal to %0.3f miles"%(kilometers, miles))

