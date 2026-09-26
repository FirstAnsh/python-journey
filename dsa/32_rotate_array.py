raw_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in raw_input.split()]
k = int(input("Enter number of steps to rotate (k): "))

if nums:
    # Handle k greater than the list length
    k = k % len(nums)

    # In-place reversal helper function
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, len(nums) - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the remaining elements
    reverse(k, len(nums) - 1)

print(f"Rotated array: {nums}")