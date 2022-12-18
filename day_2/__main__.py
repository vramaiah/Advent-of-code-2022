from day_2.solvers.day_1_solver import get_total_outcome as part_1

from day_2.solvers.day_2_solver import get_total_outcome as part_2

from . import PUZZLE_INPUT_PATH

outcome = part_1(PUZZLE_INPUT_PATH)
print(f"Outcome for part 1:\n{outcome}")
outcome = part_2(PUZZLE_INPUT_PATH)
print(f"Outcome for part 2:\n{outcome}")
