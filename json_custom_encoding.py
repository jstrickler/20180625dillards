#!/usr/bin/env python
# (c) 2018 CJ Associates
#
"""
Examples of custom JSON
"""
import json
from datetime import date

class Parrot(): # <1>
    """
    "You sold me a dead bird!"
    """
    def __init__(self, name, color):
        """Constructor"""
        self._name = name
        self._color = color

    @property
    def name(self): # <2>
        """Parrot name"""
        return self._name

    @property
    def color(self):
        """Parrot color"""
        return self._color


PARROTS = [  # <3>
    Parrot('Polly', 'green'),  #
    Parrot('Peggy', 'blue'),
    Parrot('Roger', 'red'),
]


DATA = {  # <10>
    'spam': [1, 2, 3],
    'ham': ('a', 'b', 'c'),
    'toast': date(2014, 8, 1),
    'parrots': PARROTS,
}

def encode(obj):  # <4>
    """
    Some custom JSON

    :param obj: object to be encoded
    :return: encoding
    """
    if isinstance(obj, date): # <5>
        return obj.ctime()  # <6>
    elif isinstance(obj, Parrot): # <7>
        return {'name': obj.name, 'color': obj.color} # <8>
    return obj  # <9>


print(json.dumps(DATA, default=encode, indent=4)) # <11>

