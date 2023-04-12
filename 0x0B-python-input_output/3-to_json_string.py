#!/usr/bin/python3
"""
    module to write to file
"""


def write_file(filename="", text=""):
    """
        This function takes in a file name and a text string as parameters
        and writes the text to the file with the given name
        The function returns the number of characters that were written to the file
    """
    with open(filename, mode='w', encoding="utf_8") as my_file:
        return my_file.write(text)
