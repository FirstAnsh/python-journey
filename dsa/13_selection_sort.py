numbers = [64, 25, 12, 22, 11]

for current_index in range(len(numbers) - 1):
    smallest_index = current_index

    for check_index in range(current_index + 1, len(numbers)):
        if numbers[check_index] < numbers[smallest_index]:
            smallest_index = check_index

    numbers[current_index], numbers[smallest_index] = (
        numbers[smallest_index],
        numbers[current_index]
    )

print(f"Sorted list: {numbers}")