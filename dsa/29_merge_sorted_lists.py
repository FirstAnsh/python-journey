list1 = [int(x) for x in input("Enter first sorted list (space-separated): ").split()]
list2 = [int(x) for x in input("Enter second sorted list (space-separated): ").split()]

merged = []
i = 0
j = 0

# Traverse both lists and pick the smaller element
while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

# Append remaining elements from either list
merged.extend(list1[i:])
merged.extend(list2[j:])

print(f"Merged sorted list: {merged}")