#!/usr/bin/python3

# a function that prints a matrix of integers
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for integer in line:
            print("{}".format(integer), end=" ")
        print()
