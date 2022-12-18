from . solver import get_total_outcome

from . import PUZZLE_INPUT_PATH

total_outcome = get_total_outcome(PUZZLE_INPUT_PATH)
print(f"Outcome:\n{total_outcome}")