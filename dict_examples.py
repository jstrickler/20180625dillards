#!/usr/bin/env python

d1= dict()
d2 = {'red': 5, 'purple': 8, 'white': 1, 'red': 4}
print(d2)
d2['pink'] = 7
d2['mauve'] = 3
print(d2)
d2['red'] = 0
print(d2)

print(d2['red'])
print(d2.get('blue'))
print(d2.get('blue', 0))
print(d2.setdefault('blue', 0))
print(d2)
del d2['white']
print(d2)

more = {'green': 5, 'tan': 6, 'purple': 6}
d2.update(more)
print(d2, '\n')

for color, number in sorted(d2.items()):
    print(color, number)
print()
