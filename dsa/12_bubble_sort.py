numbers = [5, 1, 4, 2, 8]

for pass_number in range(len(numbers) - 1):
    for index in range(len(numbers) - 1 - pass_number):
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]

print(f"Sorted list: {numbers}")