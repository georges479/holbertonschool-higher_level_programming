#!/usr/bin/python3
"""A class that inherits from list and adds a method to print sorted
elements."""


class MyList(list):
    """A class that print sorted elements."""

    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)

        return self
