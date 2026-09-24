names = ["Ansh", "Aarav", "Riya", "Karan", "Meera"]

target = input("Enter a name to search for: ").strip()
found = False

for index, name in enumerate(names):
    if name.lower() == target.lower():
        print(f"{name} found at index {index}.")
        found = True
        break

if not found:
    print(f"{target} was not found.")