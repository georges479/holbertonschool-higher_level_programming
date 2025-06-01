#!/usr/bin/python3
from abc import ABC, abstractmethod
"""This module defines an abstract base class for
animals and concrete classes for Dog and Cat."""


class Animal(ABC):
    """Abstract base class for animals"""
    @abstractmethod
    def sound(self):
        """Method to return the sound made by the animal"""
        pass


class Dog(Animal):
    """Concrete class for Dog"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Concrete class for Cat"""
    def sound(self):
        return "Meow"
