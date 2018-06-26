#!/usr/bin/env python

s = 'abc'

actor = ['Mary Steenbergen', 'AR', 'Cross Creek']
name = actor[0]
state = actor[1]
movie = actor[2]

name, state, movie = actor
print(name, state, movie)

x, y, z = s
print(x)
print(y)
print(z)

items = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = items
print(x, y, z)

x, *y, z = items
print(x, y, z)

*x, y, z = items
print(x, y, z)



