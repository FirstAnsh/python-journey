name = input("Enter your name: ")
branch = input("Enter your branch: ")
year = int(input("Enter your college year: "))
main_skill = input("Enter one skill you are learning: ")

student = {
    "name": name,
    "branch": branch,
    "year": year,
    "skills": ["Git", "GitHub", main_skill]
}

print("\n--- Student Profile ---")
print(f"Name: {student['name']}")
print(f"Branch: {student['branch']}")
print(f"Year: {student['year']}")
print(f"Skills: {', '.join(student['skills'])}")