#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print()
# with EXPR:
#    ...

# with EXPR as VAR:
#    ...
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        print(raw_line, end='')
print()

with open('DATA/mary.txt') as mary_in:
    all_text = mary_in.read()
print(all_text)
print()
print(repr(all_text))
print()

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

with open('fruitlist.txt', 'w') as fruits_out:
    for f in fruits:
        fruits_out.write(f + '\n')
