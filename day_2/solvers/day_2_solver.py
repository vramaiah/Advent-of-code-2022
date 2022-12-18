"""
A module containing code to solve the day 2 puzzle, part 2
"""

from day_2.constants.day_2 import RULES as DAY_2_RULES


def get_outcome(match: str):
    """Gets the outcome for one game"""
    match_list = match.split(' ')
    results = DAY_2_RULES[tuple(match_list)]
    return results


def get_total_outcome(path: str):
    """Gets the total outcome of the match"""
    with open(path) as f:
        score = 0
        for lines in f.readlines():
            match_result = get_outcome(lines.strip())
            score += match_result
        return score
