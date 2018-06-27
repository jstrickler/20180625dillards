#!/usr/bin/env python

from dillards.animals.wombat.ham import blah
blah()

# find and load
#  dillards/animals/wombat/ham.py
from dillards.animals.wombat import ham
ham.blah()

from functools import lru_cache

@lru_cache
def doit(a, b):
    # lengthy calculation
    return x


doit(5, 10)








