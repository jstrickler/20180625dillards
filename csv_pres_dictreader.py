#!/usr/bin/env python
import csv

headings = 'Term FirstName LastName BirthPlace BirthState Party'.split()

with open('DATA/presidents.csv') as pres_in:
    rdr = csv.DictReader(pres_in, fieldnames=headings)
    for row in rdr:
        print(row['FirstName'], row['LastName'])

