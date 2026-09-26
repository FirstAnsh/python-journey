first_word = input("Enter the first word: ").lower().replace(" ", "")
second_word = input("Enter the second word: ").lower().replace(" ", "")

if sorted(first_word) == sorted(second_word):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")