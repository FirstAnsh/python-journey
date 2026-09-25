word = input("Enter a word: ").lower()

left = 0
right = len(word) - 1
is_palindrome = True

while left < right:
    if word[left] != word[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")