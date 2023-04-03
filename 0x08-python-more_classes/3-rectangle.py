#!/usr/bin/python3
"""
This module defines a class Rectangle based on 2-rectangle.py
"""


class Rectangle:
    """
    Represents a rectangle

    Attributes:
    - width (int): width of the rectangle
    - height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle

        Args:
        - width (int): width of the rectangle
        - height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
        - value (int): the value to set to width

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
        """
        Retrieves the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
        - value (int): the value to set to height

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

    def area(self):
        """
        Computes the area of the rectangle

        Returns:
        - area (int): the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle

        Returns:
        - perimeter (int): the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.__height):
                rectangle_str += "#" * self.__width
                if i != self.__height - 1:
                    rectangle_str += "\n"
            return rectangle_str
