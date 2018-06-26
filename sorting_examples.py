#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

f2 = sorted(fruits, key=str.lower)
print('f2:', f2, '\n')

def to_lower(s):
    print("=>", s)
    return s.lower()

f3 = sorted(fruits, key=to_lower)
print("f3:", f3, '\n')

f4 = sorted(fruits, key=len)
print("f4:", f4, '\n')

def mysort(f):
    return len(f), f.lower()

f5 = sorted(fruits, key=mysort)
print("f5:", f5, '\n')

f6 = sorted(fruits, key=lambda f: (len(f), f.lower()))
print("f6:", f6, '\n')

f7 = sorted(fruits, key=lambda e: e[-1])
print("f7:", f7, '\n')
