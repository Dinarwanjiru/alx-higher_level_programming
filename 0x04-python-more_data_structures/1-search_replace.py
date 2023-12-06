#!/usr/bin/python3
'''function that replaces all occurrences of an element by another in a new list.'''


def search_replace(my_list, search, replace):
    if my_list == 0:
        return (my_list)
    new_list = [element if element != search else replace for element in my_list]
    return (new_list)
