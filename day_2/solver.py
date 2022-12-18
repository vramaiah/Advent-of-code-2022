"""
A module containing code to solve the day 2 puzzle
"""

from .constants import RULES

def get_outcome(match: str):
    """Gets the outcome for one game"""
    match_tuple = tuple(match.split(' '))
    results = RULES[match_tuple]
    return results

def get_total_outcome(path: str):
    """Gets the total outcome of the match"""
    with open(path) as f:
        score = 0
        for lines in f.readlines():
            match_result = get_outcome(lines.strip())
            score += match_result
        return score