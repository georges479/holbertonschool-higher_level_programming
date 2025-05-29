#!/usr/bin/python3
"""7-base_geometry.py - Class BaseGeometry with area and validator methods."""


class BaseGeometry:
    """BaseGeometry class with public instance methods."""
    def area(self):
        """Raises an exception to indicate area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
