numbers = [2, 4, 7, 11, 15, 20, 25, 30]

target = int(input("Enter a number to search for: "))

left = 0
right = len(numbers) - 1
found = False

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print(f"{target} found at index {middle}.")
        found = True
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1

if not found:
    print(f"{target} was not found.")