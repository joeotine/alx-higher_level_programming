#!/usr/bin/python3

class Rectangle:
    """
    A class that represents a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def get_width(self):
        """Returns the width of the rectangle."""
        return self.__width

    def set_width(self, width):
        """Sets the width of the rectangle."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def get_height(self):
        """Returns the height of the rectangle."""
        return self.__height

    def set_height(self, height):
        """Sets the height of the rectangle."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    width = property(get_width, set_width)
    height = property(get_height, set_height)

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0

    def __str__(self):
        """Returns the string representation of the rectangle."""
        if not self.__width or not self.__height:
            return ""
        return "#" * self.__width + ("\n" + "#" * self.__width) * (self.__height - 1)

    def __repr__(self):
        """Returns the object representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
