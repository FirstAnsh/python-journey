raw_input = input("Enter distinct numbers separated by spaces: ")
nums = [int(x) for x in raw_input.split()]

result = []

def backtrack(start_index, current_subset):
    # Add a copy of the current subset to results
    result.append(list(current_subset))

    for i in range(start_index, len(nums)):
        # Include nums[i]
        current_subset.append(nums[i])
        # Recurse for remaining elements
        backtrack(i + 1, current_subset)
        # Backtrack: remove nums[i]
        current_subset.pop()

backtrack(0, [])

print(f"Total subsets: {len(result)}")
print(f"Subsets: {result}")