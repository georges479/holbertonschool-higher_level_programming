#!/usr/bin/python3
"""'4-inherits_from.py - Function to check if an object is an instance of
a class that inherited from a specified class."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
