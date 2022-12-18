"""
Module to handle data and inputs for day 3
"""

from .rucksack import Rucsack

from .elf_group import ElfGroup


def get_sacs(path):
    sacs = []
    with open(path) as f:
        for line in f.readlines():
            sacs.append(Rucsack(line))
    return sacs

def get_groups(path):
    groups = []
    with open(path) as f:
        for i in range(100):
            string = ''
            for i in range(3):
                string += f.readline()
            groups.append(ElfGroup(string))
    return groups