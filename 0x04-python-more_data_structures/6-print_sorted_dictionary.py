#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for var in sorted(a_dictionary.keys()):
        print("{}: {}".format(var, a_dictionary[var]))
