expression = input("Enter bracket sequence: ")

bracket_map = {')': '(', '}': '{', ']': '['}
stack = []
is_valid = True

for char in expression:
    if char in bracket_map.values():
        stack.append(char)
    elif char in bracket_map:
        if not stack or stack[-1] != bracket_map[char]:
            is_valid = False
            break
        stack.pop()

# If stack is not empty at the end, some opening brackets were unclosed
if is_valid and not stack:
    print("Valid / Balanced")
else:
    print("Invalid / Unbalanced")