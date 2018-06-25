#!/usr/bin/env python

joel = ['biking', 'kayaking', 'making peanut butter']

seth = ['making peanut butter', 'putting kids to bed', 'farming', 'biking']

j = set(joel)
s = set(seth)

print("both (intersection):", j & s)
print("either (union):", j | s)
print("just one (xor):", j ^ s)
print("just Joel", j - s)
print("just Seth", s - j)
