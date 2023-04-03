#!/usr/bin/python3
"""Defines a class rectangle"""

class Rectangle:
    """
    Represents a rectangle"""

    def __init__(self, width=0, height=0):
    """Initializes a new Rectangle object.

    Args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
    """
    self.__width = width
    self.__height = height

def __str__(self):
    """Returns a string representation of the Rectangle instance,
    filled with the '#' character.

    Returns:
        A string of '#' characters that represents the rectangle.
    """
    if self.__height == 0 or self.__width == 0:
        return ""
    rec_str = ""
    for i in range(self.__height):
        for j in range(self.__width):
            rec_str += "#"
        rec_str += "\n"
    return rec_str[:-1]

def __repr__(self):
    """Returns a string representation of the Rectangle instance.

    Returns:
        A string of the form "Rectangle(width, height)"
    """
    return "Rectangle({}, {})".format(self.__width, self.__height)

@property
def width(self):
    """Get the width of the Rectangle.

    Returns:
        The width of the Rectangle instance.
    """
    return self.__width

@width.setter
def width(self, value):
    """Set the width of the Rectangle.

    Args:
        value (int): The value to set the width of the Rectangle to.
    """
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

@property
def height(self):
    """Get the height of the Rectangle.

    Returns:
        The height of the Rectangle instance.
    """
    return self.__height

@height.setter
def height(self, value):
    """Set the height of the Rectangle.

    Args:
        value (int): The value to set the height of the Rectangle to.
    """
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value

def area(self):
    """Calculate the area of the Rectangle.

    Returns:
        The area of the Rectangle instance.
    """
    return self.__width * self.__height

def perimeter(self):
    """Calculate the perimeter of the Rectangle.

    Returns:
        The perimeter of the Rectangle instance.
    """
    if self.__width == 0 or self.__height == 0:
        return 0
    else:
        return 2 * (self.__width + self.__height)
