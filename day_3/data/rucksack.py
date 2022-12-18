"""
Module with code to model a rucksack
"""

from .compartment import Compartment


class Rucksack:
    """Class to model a rucksack"""

    def __init__(self, sac_string: str):
        sac_string = sac_string.strip()
        length_sac = len(sac_string) // 2
        self.compartment_1 = Compartment(sac_string[:length_sac])
        self.compartment_2 = Compartment(sac_string[length_sac:])

    @property
    def common_item(self):
        section_1_items = self.compartment_1.items
        for item in section_1_items:
            if item in self.compartment_2.items:
                return item
            else:
                continue

    @property
    def items(self):
        item_set_1 = list(self.compartment_1.items)
        item_set_2 = list(self.compartment_2.items)
        item_set_1.extend(item_set_2)
        return tuple(item_set_1)
