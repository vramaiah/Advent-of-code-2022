from . import get_greatest_amount, PUZZLE_INPUT_PATH, get_top_three

greatest = get_greatest_amount(PUZZLE_INPUT_PATH)
print(f"Greatest: amount:\n{greatest}")
top_3_sum = sum(get_top_three(PUZZLE_INPUT_PATH))
print(f"Top 3 sum:\n{top_3_sum}")
