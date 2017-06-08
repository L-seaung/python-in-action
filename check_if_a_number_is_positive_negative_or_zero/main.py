#!/usr/bin/env python3
# -*- coding:utf-8 -*-

num = float(input("enter a number:"))
if num > 0:
    print("positive number")
elif num == 0:
    print("zero")
else:
    print("negative number")

num = float(input("enter a number:"))
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("positive number")
else:
    print("negative number")

