"""
A module containing code to solve the puzzle
"""

import logging


def get_calories(path):
    logging.basicConfig(level=logging.INFO)
    with open(path) as f:
        calorie_counts = []
        elf_calories = 0
        for line in f.readlines():
            try:
                calories = int(line.strip())
            except ValueError:
                calorie_counts.append(elf_calories)
                elf_calories = 0
            else:
                elf_calories += calories
        return calorie_counts


def get_greatest_amount(path):
    """Gets the greatest amount of calories an elf has"""
    calorie_counts = get_calories(path)
    return max(calorie_counts)


def get_top_three(path):
    calorie_counts = get_calories(path)
    calorie_counts.sort(reverse=True)
    return calorie_counts[:3]
