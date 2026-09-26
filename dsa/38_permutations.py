raw_input = input("Enter distinct numbers separated by spaces: ")
nums = [int(x) for x in raw_input.split()]

result = []

def backtrack(current_permutation, used):
    # Base case: full permutation formed
    if len(current_permutation) == len(nums):
        result.append(list(current_permutation))
        return

    for i in range(len(nums)):
        if not used[i]:
            # Choose
            used[i] = True
            current_permutation.append(nums[i])

            # Explore
            backtrack(current_permutation, used)

            # Unchoose (Backtrack)
            current_permutation.pop()
            used[i] = False

used = [False] * len(nums)
backtrack([], used)

print(f"Total permutations: {len(result)}")
print(f"Permutations: {result}")