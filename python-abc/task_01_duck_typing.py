#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""
    @abstractmethod
    def area(self):
        """Method to calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate the perimeter of the shape"""
        pass


class Circle(Shape):
    """Concrete class for Circle"""
    def __init__(self, radius):
        """Initialize the Circle with a radius"""
        self.radius = radius

    def area(self):
        """Calculate the area of the Circle"""
        return math.pi * (self.radius * self.radius)

    def perimeter(self):
        """Calculate the perimeter of the Circle"""
        return math.pi * 2 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        """Initialize the Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle"""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Return a straing representation of the shape"""
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
