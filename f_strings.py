#!/usr/bin/env python

person = 'Billy Bob'
city = "Malvern"

print("%s is from %s" % (person, city))

#       0          1           0       1
print("{} is from {}".format(person, city))

price = 1.2

print("That costs ${:.02f}".format(price))
print(f"That costs ${price:.02f}")
