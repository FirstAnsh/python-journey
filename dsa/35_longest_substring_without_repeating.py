text = input("Enter a string: ")

char_index_map = {}
left = 0
max_length = 0
longest_sub = ""

for right, char in enumerate(text):
    # If the character is already inside the current window, move the left boundary
    if char in char_index_map and char_index_map[char] >= left:
        left = char_index_map[char] + 1

    char_index_map[char] = right
    current_length = right - left + 1

    if current_length > max_length:
        max_length = current_length
        longest_sub = text[left:right + 1]

print(f"Longest substring: '{longest_sub}'")
print(f"Length: {max_length}")