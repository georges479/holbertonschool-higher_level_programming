#!/usr/bin/python3
"""Module defining a Square class with size validation."""


class Square:
    """Class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#' to stdout.

        If the size is 0, print an empty line.
        Use position to determine spacing.
        """
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (isinstance(value, tuple) and
                len(value) == 2 and
                isinstance(value[0], int) and
                isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
