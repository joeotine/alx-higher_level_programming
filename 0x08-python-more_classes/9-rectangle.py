#!/usr/bin/python3
"""
Rectangle Class.
This module contains an empty class that defines a rectangle based on 8-rectangle.py
"""


class Rectangle:
    """
    Defines a rectangle.

    Attributes:
        width (int): An integer indicating the width of the rectangle object.
        height (int): An integer indicating the height of the rectangle object.
        number_of_instances (int, public): An integer indicating the number of objects.
        print_symbol (any, public): Used as symbol for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """An object constructor method.

        Initiatilizes Rectangle with width and height.

        Args:
            width (int): An integer representing object width.
                Has a default value of 0.
            height (int): An integer representing object height.
                Has a default value of 0.
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += "\n"
        return rec_str[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for del"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Gets the width private attribute value.

        Returns:
            The width private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width private attribute value.
        Validates the assignment of the width private attribute.

        Args:
            value (int): the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height private attribute value.

        Returns:
            The height private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height private attribute value.
        Validates the assignment of the height private attribute.

        Args:
            value (int): the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A public object method.

        Returns:
            The current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """A public object method.

        Returns:
            The current rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
