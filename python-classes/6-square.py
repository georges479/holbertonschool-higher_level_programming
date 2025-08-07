#!/usr/bin/env python3
"""Defines a Square class with size and position properties."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size (int): size of the square (default: 0)
            position (tuple): position (default: (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' considering position."""
        if self.__size == 0:
            print()
            return

        # Print new lines for vertical position
        for _ in range(self.__position[1]):
            print()

        # Print each line of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
