"""
Module with code to model a rucksack compartment
"""


class Compartment:
    """Class to model a rucksack compartment"""

    def __init__(self, string: str):
        self.items = tuple(string)

    def __str__(self):
        return str(self.items)
