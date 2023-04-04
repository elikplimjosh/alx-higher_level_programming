#!/usr/bin/python3
"""
Addition function for two integers

This function takes two arguments, a and b, and returns their sum
while ensuring that both inputs are of type int.
"""

def add_integer(a, b=98):
    """
    Add two integers and return the sum

    Arguments:
    a (int): The first integer
    b (int, optional): The second integer. Defaults to 98.

    Returns:
    int: The sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

