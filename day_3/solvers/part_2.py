"""
Module containing code to solve day 3, part 2
"""

from day_3.data import get_groups

from day_3.constants import VALUES


def get_sum(path):
    groups = get_groups(path)
    result = 0
    for group in groups:
        result += VALUES[group.common_item]
    return result
