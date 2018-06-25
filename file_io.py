#!/usr/bin/env python
"""
Some examples of file I/O
"""

FRUITS = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape"]

def main():
    """
    Program entry point

    :return: None
    """
    read_mary1()
    read_mary1()
    read_mary1()
    write_fruits()


def read_mary1():
    """
    Read mary.txt one line at a time

    :return: None
    """
    with open('DATA/mary.txt') as mary_in:
        for raw_line in mary_in:
            line = raw_line.rstrip()
            print(line)
    print()

def read_mary2():
    """
    Read mary.txt and strip newlines

    :return: None
    """
    with open('DATA/mary.txt') as mary_in:
        for raw_line in mary_in:
            print(raw_line, end='')
    print()

def read_mary3():
    """
    Blah blah and blah

    :return: None
    """
    with open('DATA/mary.txt') as mary_in:
        all_text = mary_in.read()
    print(all_text)
    print()

def write_fruits():
    """
    Write fruit list to file

    :return:
    """
    with open('fruitlist.txt', 'w') as fruits_out:
        for f in FRUITS:
            fruits_out.write(f + '\n')

if __name__ == '__main__':  # if run as "main" script
    main()
# else
#   imported

