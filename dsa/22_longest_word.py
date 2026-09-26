sentence = input("Enter a sentence: ")

words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

if longest_word:
    print(f"Longest word: {longest_word}")
    print(f"Length: {len(longest_word)}")
else:
    print("No words were entered.")