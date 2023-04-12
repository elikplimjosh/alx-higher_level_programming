#!/usr/bin/python3

"""Defines a text file-reading function."""


def read_lines(filename="", nb_lines=0):
    """Print a given number of lines from a UTF8 text file to stdout.

    Args:
        filename (str): The name of the file.
        nb_lines (int): The number of lines to read from the file.
    """
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return

        lines = f.readlines()
        if nb_lines >= len(lines):
            print("".join(lines), end="")
            return

        for line in lines[:nb_lines]:
            print(line, end="")

