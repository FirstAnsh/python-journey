raw_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in raw_input.split()]

if not nums:
    print("List is empty.")
else:
    max_so_far = nums[0]
    current_max = nums[0]

    for x in nums[1:]:
        # Decide whether to add to the existing subarray or start fresh from x
        current_max = max(x, current_max + x)
        max_so_far = max(max_so_far, current_max)

    print(f"Maximum Subarray Sum: {max_so_far}")