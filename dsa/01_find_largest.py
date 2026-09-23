numbers = [12, 45, 7, 89, 34, 56]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"Numbers: {numbers}")
print(f"Largest number: {largest}")