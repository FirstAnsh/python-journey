def sum_list(numbers, index=0):
    if index == len(numbers):
        return 0

    return numbers[index] + sum_list(numbers, index + 1)


numbers = [10, 20, 30, 40]
total = sum_list(numbers)

print(f"Numbers: {numbers}")
print(f"Sum: {total}")