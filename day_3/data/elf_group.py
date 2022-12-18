"""
Module with code to model a group of elves
"""


from .rucksack import Rucsack

class ElfGroup:
    """Class to model a group of elves"""

    def __init__(self, string: str):
        raw_sacks = string.strip().split('\n')
        self.sac_1 = Rucsack(raw_sacks[0])
        self.sac_2 = Rucsack(raw_sacks[1])
        self.sac_3 = Rucsack(raw_sacks[2])

    @property
    def common_item(self):
        for item in self.sac_1.items:
            if item in self.sac_2.items and item in self.sac_3.items:
                return item
            else:
                continue
