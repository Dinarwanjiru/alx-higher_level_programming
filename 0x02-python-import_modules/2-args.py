#!/usr/bin/python3

if __name__ == "__main__":
    """Print number of and list of arguments"""
    import sys

    point = len(sys.argv) - 1
    if point == 0:
        print("0 arguments.")
    elif point == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(point))
    for i in range(point):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
