"""This module contains a couple of functions for handling right angled triangle"""
__version__ = "1.0"
__author__ = "Prasun"

def hypothenuse(perpendicular, base):
    """This returns the length of the hypotenuse when the lengths of other
    two sides is given of a right angled triangle"""
    return (perpendicular ** 2 + base ** 2) ** 0.5


def area(perpendicular, base):
    """This returns the area of a right angled triangle when the lengths of 
    other two sides is given"""
    return 0.5 * base * perpendicular