raw_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in raw_input.split()]

unique_elements = []
seen = set()

for num in numbers:
    if num not in seen:
        unique_elements.append(num)
        seen.add(num)

print(f"Original list: {numbers}")
print(f"Without duplicates: {unique_elements}")