#!/usr/bin/python3
"""A simple example of a custom list class that overrides
the append method."""


class VerboseList(list):
    """A custom list class that prints a message when an item is added."""
    def append(self, item):
        """Override the append method to print a message."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Override the extend method to print a message."""
        super().extend(iterable)
        x = len(iterable)
        print(f"Extended the list with {x} items.")

    def remove(self, item):
        """Override the remove method to print a message."""
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        """Override the pop method to print a message."""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
