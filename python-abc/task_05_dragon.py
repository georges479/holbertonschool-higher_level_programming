#!/usr/bin/python3
""" Nameless module for mixin and Dragon classes """


class SwimMixin:
    """SwimMixin"""
    def swim(self):
        """prints a string"""
        print("The creature swims!")


class FlyMixin:
    """FlyMixin"""
    def fly(self):
        """prints a string"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon"""
    def roar(self):
        """prints a string"""
        print("The dragon roars!")
