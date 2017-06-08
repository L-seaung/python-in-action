#!/usr/bin/env python
# -*- coding:utf-8 -*-
# python program to check if the input number is odd or even
# a number is even if idvision by 2 give a remainder of 0.
# if remainder if 1, it is odd number

num = int(input("enterr a number: "))
if (num % 2) == 0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))

