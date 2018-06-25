#!/usr/bin/env python


def get_message():
    return "Hello, world"


def display_message():
    m = get_message()
    print(m)

display_message()

def make_log_report(year, month, *states):
    for state in states:
        print("Making log report for {} {} ({})".format(
            year, month, state
        ))

make_log_report(2018, 1, 'AR', 'AZ', 'AL')

def mlr(*states, year=None, month=None):
    for state in states:
        print("Making log report for {} {} ({})".format(
            year, month, state
        ))

mlr('AR', "AK", "NC", "TX", month=7, year=1776)
mlr('VA')

def spam(*, filename, username):
    print(filename, username)

spam(filename='ham.txt', username='Guido')

def toast(**kwargs):
    print(kwargs)

toast(filename='ham.txt', username='Guido')
