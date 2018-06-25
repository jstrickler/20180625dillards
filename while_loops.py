#!/usr/bin/env python

while True:
    year = input("Enter year (or q to quit): ")
    if year == 'q':
        break
    month = input("Enter month as 2 digits (NN): ")
    try:
        date = (int(year), int(month))
    except ValueError as err:
        print(err)
        continue
    print("Creating report for {}-{}".format(year, month))

