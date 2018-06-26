#!/usr/bin/env python

def spam(username, password):
    print(username, password)

user = 'Tim'
password = 'python'

spam(user, password)

auth = ['Robin', 'musicians']

# spam(auth)
spam(auth[0], auth[1])
spam(*auth)
print()

authd = {'user': 'Arthur', 'password': 'KING'}

def ham(*, user, password):
    print(user, password)

ham(user='Bob', password='l0l')
ham(**authd)

