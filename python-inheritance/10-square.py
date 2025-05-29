#!/usr/bin/python3
"""9-rectangle.py: Defines a Rectangle class that inherits from"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""
    def __init__(self, size):
        """Initializes the Square instance with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size
