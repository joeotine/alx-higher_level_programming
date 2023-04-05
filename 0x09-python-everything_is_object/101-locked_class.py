#!/usr/bin/python3
"""
This module is for a class that prevents creation of dynamic attributes
"""


class LockedClass():
    """Class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
