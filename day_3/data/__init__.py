"""
Module to handle data and inputs for day 3
"""

from .rucksack import Rucsack


def get_sacs(base_file_path):
    sacs = []
    with open(base_file_path) as f:
        for line in f.readlines():
            sacs.append(Rucsack(line))
    return sacs
