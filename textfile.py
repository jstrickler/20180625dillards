#!/usr/bin/env python
import os

class TextFile(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self._file = open(self._file_name)

    def get_line(self):
        return next(self._file).rstrip().upper()

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, filename):
        if filename.endswith('.txt'):
            self._file_name = filename
        else:
            raise ValueError("File name must end with .txt")

    def __str__(self):
        return self._file_name

    def __repr__(self):
        return 'TextFile({})'.format(self._file_name)

    def __len__(self):
        return os.path.getsize(self._file_name)

    def __add__(self, other):
        return 'HA HA HA'

class Person():
    def __init__(self, firstname, lastname, age):
        self._first_name = firstname
        self._last_name = lastname
        self._age = age

    @property
    def first_name(self):
        return self._first_name.upper()

p = Person('Fred', 'Jones', 25)

print(p.first_name)

