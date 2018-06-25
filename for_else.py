#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

target = 'z'

for f in fruits:
    if f.startswith(target):
        print(f)
        break
else:
    print("Not found")
