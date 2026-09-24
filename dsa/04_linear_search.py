numbers = [12, 45, 7, 89, 34, 56]

target = int(input("Enter a number to search for: "))
found = False

for index in range(len(numbers)):
    if numbers[index] == target:
        print(f"{target} found at index {index}.")
        found = True
        break

if not found:
    print(f"{target} was not found.")