"""
Module containing code to parse the dataset
"""

from .pair import AssignmentPair


def get_ranges(path):
    pairs = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            pairs.append(AssignmentPair(line))
    return pairs
