#!/usr/bin/python3
"""Module defining a Square class with size validation."""

class Square:
    """Class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
         """Print the square with the character '#' to stdout.

        If the size is 0, print an empty line.
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
