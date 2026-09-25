numbers = [2, 4, 7, 11, 15, 20]
target = int(input("Enter a target sum: "))

left = 0
right = len(numbers) - 1
found = False

while left < right:
    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        print(f"Pair found: {numbers[left]} + {numbers[right]} = {target}")
        found = True
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

if not found:
    print("No pair found.")
    