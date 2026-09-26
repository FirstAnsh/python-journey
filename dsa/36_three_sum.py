raw_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in raw_input.split()]

nums.sort()
triplets = []

for i in range(len(nums) - 2):
    # Skip identical elements to avoid duplicate triplets
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = len(nums) - 1

    while left < right:
        current_sum = nums[i] + nums[left] + nums[right]

        if current_sum == 0:
            triplets.append([nums[i], nums[left], nums[right]])
            
            # Skip duplicates for the second and third elements
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            left += 1
            right -= 1
        elif current_sum < 0:
            left += 1
        else:
            right -= 1

print(f"Unique triplets summing to 0: {triplets}")