#!/usr/bin/python3
"""
Module 1-rectangle

Defines a Rectangle class with private instance attributes width and height
"""


class Rectangle:
    """
    Rectangle class with private instance attributes width and height

    Attributes:
    - width (int): width of the rectangle (default 0)
    - height (int): height of the rectangle (default 0)
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height

        Args:
        - width (int): width of the rectangle (default 0)
        - height (int): height of the rectangle (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle

        Args:
        - value (int): width value to set

        Raises:
        - TypeError: if value is not an integer
        - ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle

        Args:
        - value (int): height value to set

        Raises:
        - TypeError: if value is not an integer
        - ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

