text = input("Enter a word or sentence: ").lower().replace(" ", "")

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print("\nCharacter frequencies:")

for character, count in frequency.items():
    print(f"{character}: {count}")