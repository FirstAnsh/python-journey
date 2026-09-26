text = input("Enter a string to compress: ")

if not text:
    print("Compressed string: ''")
else:
    compressed = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(text[i - 1] + str(count))
            count = 1

    # Append the last character group
    compressed.append(text[-1] + str(count))

    result = "".join(compressed)
    
    # Return original if compressed version isn't shorter
    final_output = result if len(result) < len(text) else text
    print(f"Compressed result: {final_output}")