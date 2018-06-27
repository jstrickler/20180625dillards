#!/usr/bin/env python
import csv

with open('DATA/airport_boardings.csv') as airport_in:
    rdr = csv.DictReader(airport_in)
    for row in rdr:
        print(row['Code'], row['2010 Rank'])

