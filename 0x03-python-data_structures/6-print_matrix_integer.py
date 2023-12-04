#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colnm in row:
            if colnm == row[-1]:
                print("{:d}".format(colnm), end='')
            else:
                print('{:d}'.format(colnm), end=' ')
        print()
