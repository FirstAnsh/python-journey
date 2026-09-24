numbers = [5, 2, 7, 2, 9, 2, 4]

target = int(input("Enter a number to search for: "))
positions = []

for index, number in enumerate(numbers):
    if number == target:
        positions.append(index)

if positions:
    print(f"{target} found at indexes: {positions}")
else:
    print(f"{target} was not found.")