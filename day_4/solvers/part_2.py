"""
Module containing code to solve day 3, part 1
"""

from day_4.data import get_ranges


def solve(path: str):
    """Function to solve day 4, part 1"""
    ranges = get_ranges(path)
    number_satisfied = 0
    for assign_range in ranges:
        if assign_range.overlaps():
            number_satisfied += 1
    return number_satisfied
