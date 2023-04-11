#!/usr/bin/python3
"""This module creates a class for task 1"""


class MyList(list):
    """
        This class is a subclass of the built-in list class
        and it includes an additional sort method
    """
    def print_sorted(self):
        """
            Function to return a sorted list
        """
        print(sorted(self))
