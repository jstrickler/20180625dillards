#!/usr/bin/env python

actor = 'Mary Steenbergen', 'AR', 'Cross Creek'

print(actor[0], actor[1])

name, state, movie = actor

print(name, state)

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

for p in people:
    print(p[0], p[1])
print('-' * 60)

for p in people:
    first_name, last_name, product = p
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product in people:
    print(first_name, last_name)
print('-' * 60)

colors = ['red', 'grey', 'pink', 'orange']

for i, color in enumerate(colors):
    print(i, color)
print()

print(list(enumerate(colors)))

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}
print(list(airports.items()))

for abbr, name in airports.items():
    print(abbr, name)
print()


