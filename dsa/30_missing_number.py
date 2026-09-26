raw_input = input("Enter numbers from 1 to N with one missing (space-separated): ")
nums = [int(x) for x in raw_input.split()]

# The list has size n - 1, meaning the full range is 1 to n
n = len(nums) + 1

# Expected sum of first n natural numbers: n * (n + 1) // 2
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print(f"Missing number: {missing}")