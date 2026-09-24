numbers = [1, 2, 2, 3, 1, 2, 4, 3, 3]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("Number frequencies:")

for number, count in frequency.items():
    print(f"{number} appears {count} time(s)")