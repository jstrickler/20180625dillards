#!/usr/bin/env python

def spam(func):
    def toast():
        print("YOU GOT TO BE KIDDING ME!")
        func()
    return toast


@spam
def ham():
    print("Hello from ham()")

# ham = spam(ham)



ham()
ham()
ham()

print(ham)
