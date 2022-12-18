from day_2.solvers.day_1_solver import get_total_outcome

from . import PUZZLE_INPUT_PATH

outcome = get_total_outcome(PUZZLE_INPUT_PATH)
print(f"Outcome for part 1:\n{outcome}")