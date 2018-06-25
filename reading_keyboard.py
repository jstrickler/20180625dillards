#!/usr/bin/env python
import sys

if len(sys.argv) < 3:
    year = input("Enter year: ")
    month = input("Enter month as 2 digits (NN): ")
else:
    year = sys.argv[1]
    month = sys.argv[2]

try:
    date = (int(year), int(month))
except ValueError as err:
    print(err)
    exit()

print("date is", date)
