#!/usr/bin/python3
"""
Print Full Name Function

This function takes a first name and an optional last name as arguments,
checks that they are valid strings, and prints the full name to the output.

Args:
    first_name (str): The first name.
    last_name (str, optional): The last name. Default is an empty string.

Raises:
    TypeError: If first_name is not a string.
    TypeError: If last_name is not a string.

Example:
    say_my_name("John", "Doe")  # Prints "My name is John Doe"
    say_my_name("Jane")         # Prints "My name is Jane"
"""

def say_my_name(first_name, last_name=""):
    """
    Print the full name

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Default is an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

