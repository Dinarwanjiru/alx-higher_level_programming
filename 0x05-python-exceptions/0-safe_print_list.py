#!/usr/bin/python3
def safe_print_list(my_list=[], y=0):
    count = 0
    for i in range(y):
        try:
            print("{}".format(my_list[i]), end="")
            count = count + 1
        except IndexError:
            continue
    print("")
    return count
