#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'

print("The \"guy\" is 'working' the machine")

print("""The "guy" is 'working' the machine""")

query = """
select *
from vendors
where state = 'AZ'
"""

pattern = 'foo \bbar\b blah'
# BAD! pattern = 'foo \\bbar\\b blah'
pattern = r'foo \bbar\b blah'

actor = 'Billy Bob Thornton'

actor = actor.replace('B', 'D')

print(actor.upper())
print(actor.count('l'))
print(len(actor))




