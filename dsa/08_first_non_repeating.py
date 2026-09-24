numbers = [4, 5, 1, 2, 0, 4, 1, 2]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

first_unique = None

for number in numbers:
    if frequency[number] == 1:
        first_unique = number
        break

if first_unique is not None:
    print(f"First non-repeating number: {first_unique}")
else:
    print("No non-repeating number found.")