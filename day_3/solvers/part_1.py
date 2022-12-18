"""
Module containing code to solve day 3, part 1
"""

from day_3.data import get_sacs

from day_3.constants import VALUES


def get_sum(path):
    sacs = get_sacs(path)
    result = 0
    for sac in sacs:
        result += VALUES[sac.get_common_item()]
    return result
