raw_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in raw_input.split()]

# Two-pointer in-place approach
non_zero_pos = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
        non_zero_pos += 1

print(f"Result: {nums}")