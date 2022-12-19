"""
Module with code to handle pairs
"""

from .assignment import Assignment


class AssignmentPair:
    """Class to handle an assignment pair"""

    def __init__(self, string: str):
        substrings = string.split(',')
        self.assignments = [
            Assignment(substrings[0]),
            Assignment(substrings[1])]

    def fully_contains(self):
        """Returns if there is an assignment that fully contains the other"""
        assign_1 = self.assignments[0]
        assign_2 = self.assignments[1]
        condition_1 = assign_1.fully_contains(assign_2)
        condition_2 = assign_2.fully_contains(assign_1)
        return condition_1 or condition_2
