#!/usr/bin/env python
import csv

with open('DATA/airport_boardings.csv') as airport_in:
    next(airport_in)
    rdr = csv.reader(airport_in)
    for row in rdr:
        print(row)
