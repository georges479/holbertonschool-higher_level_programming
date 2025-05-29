#!/usr/bin/python3
"""3-is_kind_of_class.py - Function to check if an object is an instance"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or a subclass."""
    return isinstance(obj, a_class)
