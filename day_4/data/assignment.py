"""
Module containing code related to assignments
"""


class Assignment:
    """A class to represent an assignment"""

    def __init__(self, string: str):
        """Makes a new assignment class to represent an assignment"""
        parsed = string.split('-')
        start = int(parsed[0])
        end = int(parsed[1])
        self.sections = set(range(start, end + 1))

    @property
    def items(self):
        return self.sections

    def __contains__(self, item):
        return item in self.sections

    def fully_contains(self, assignment):
        """Returns if an assignment is fully contained in the assignment"""
        for item in assignment.items:
            if item not in self:
                return False
        return True
