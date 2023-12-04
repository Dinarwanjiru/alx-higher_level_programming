#!/usr/bin/python3
'''prints integers of a list'''
def print_list_integer(my_list=[]):
    for list_elements in range(len(my_list)):
            print("{:d}".format(my_list[list_elements]))
