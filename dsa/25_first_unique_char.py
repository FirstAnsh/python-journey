text = input("Enter a string: ")

char_count = {}

# Step 1: Count frequency of each character
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

# Step 2: Find the first character with a count of 1
first_unique = None
for char in text:
    if char_count[char] == 1:
        first_unique = char
        break

if first_unique:
    print(f"First non-repeating character: '{first_unique}'")
else:
    print("No unique character found.")