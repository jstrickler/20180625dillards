#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

f1 = [f.upper() for f in fruits]
print(f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print(f3, '\n')

food = ['spam', 'spam', 'spam', 'eggs', 'spam', 'spam',
        'toast', 'spam', 'spam', 'spam', 'spam',
        'bacon', 'spam', 'spam', 'spam', ]

good_food = [f for f in food if f != 'spam']
print(good_food, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

#  "{} {}".format(f, l)
last_names = [f"{f} {l}" for f, l, p in people]
print(last_names, '\n')

nums = [800,80,1000,32,255,400,5,5000]

n1 = [float(n) for n in nums if n > 200]
print(n1, '\n')

