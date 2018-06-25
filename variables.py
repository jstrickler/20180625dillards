#!/usr/bin/env python

x = 5
y = x

x = 10

# int x = 10;

z = x

print(x, y, z)
print(id(x), id(y), id(z))

print(x is z)

print(type(x), type(print))

print(dir(__builtins__))

