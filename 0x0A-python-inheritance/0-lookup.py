#!/usr/bin/python3

"""defines an object attribute function."""

def lookup(obj):
    """returns a list of an objects available attributes."""
    return (dir(obj))

