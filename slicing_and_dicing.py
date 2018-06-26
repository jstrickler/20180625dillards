#!/usr/bin/env python

actor = 'Billy Bob Thornton'

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

print(fruits[0:3])
print(fruits[:3])

# S[START:STOP]  S[:STOP]   S[START:]
print(fruits[-3:])
print(fruits[2:9])
print(fruits[-10:])

print(actor[:5])
print(actor[6:9])
print(actor[10:])


