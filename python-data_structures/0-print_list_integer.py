#!/usr/bin/python3
# Function that prints all integers of a list
def print_list_integer(my_list=[]):
    """Print all integers in the list, one per line."""
    for number in range(len(my_list)):
        print("{:d}".format(my_list[number]))
