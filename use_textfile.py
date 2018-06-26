#!/usr/bin/env python
from textfile import TextFile

t1 = TextFile('DATA/mary.txt')

print(t1)
print(type(t1))
print(type(t1).__name__)

t2 = TextFile('DATA/alice.txt')
print(t2)

print(t1._file_name)
print(t2._file_name)
for _ in range(3):
    print(t1.get_line())

print(t2.file_name)

# t3 = TextFile('DATA/customers.dat')
print(repr(t1), repr(t2))

print(len(t1), len(t2))
print(t1 + t2)
