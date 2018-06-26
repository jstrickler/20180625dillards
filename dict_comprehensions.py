#!/usr/bin/env python

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
    'LIT': 'Little Rock',
    'NWA': 'NW Arkansas',
}

sa = {k:v for k, v in airports.items() if k.startswith('S')}
print(sa)

import os
file_sizes = {n:os.path.getsize(n) for n in os.listdir('.') if n.endswith('.py')}

print(file_sizes)
import re
with open('DATA/alice.txt') as alice_in:
    all_text = alice_in.read()
    all_words = re.findall('[a-z]+', all_text, re.I)

print(all_words)
print(len(all_words))
words = {w.lower() for w in all_words}
print(len(words))
