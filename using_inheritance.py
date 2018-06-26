#!/usr/bin/env python

class Wombat():
    def bark(self):
        print("woof woof")

class Person():
    def __init__(self, name):
        self._name = name

    def id(self):
        print("I am", self._name)

p1 = Person('Fred')
p1.id()

class HogFan(Person, Wombat):
    def id(self):
        super().id()
        for _ in range(3):
            print("Woooo Pig Sooey!!")

h1 = HogFan('Joel')
h1.id()
h1.bark()

class HokieFan(Person):
    def id(self):
        super().id()
        print("Hokie Hokie Hi")

h2 = HokieFan('Susan')
h2.id()
