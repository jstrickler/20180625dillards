#!/usr/bin/env python
actor = 'Billy Bob Thornton'

list1 = list()
print(list1)

list2 = list(actor)
print(list2)

colors = ['red', 'blue', 'purple', 'mauve']

list4 = []

for c in colors:
    print(c)

print()

colors.append('yellow')
print(colors)
colors.insert(2, 'pink')
colors.insert(0, 'black')
print(colors)
colors.insert(99, 'orange')
print(colors)

print(colors[3])
# print(colors[42])

more_colors = ['white', 'navy', 'chartreuse']

colors.extend(more_colors)

print(colors)

# bad:
# colors = colors + more_colors

del colors[4]
print(colors)

c1 = colors.pop()
print(c1)
print(colors)
c2 = colors.pop(3)
print(c2, colors)

colors.remove('mauve')
print(colors)

print(colors[0], colors[5], colors[-1])
