#!/usr/bin/python3
"""0-lookup.py - A function to return the list of
available attributes and methods of an object."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the attributes and
        methods of the object.
    """
    return list(dir(obj))
