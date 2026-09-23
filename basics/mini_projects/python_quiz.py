questions = [
    {
        "question": "1. Which function displays output in Python?\na) input\nb) print\nc) len",
        "answer": "b"
    },
    {
        "question": "2. Which brackets create a list?\na) ()\nb) []\nc) {}",
        "answer": "b"
    },
    {
        "question": "3. Which operator checks whether two values are equal?\na) =\nb) ==\nc) !=",
        "answer": "b"
    }
]

score = 0

print("Welcome to the Python Basics Quiz!\n")

for item in questions:
    print(item["question"])
    answer = input("Your answer (a/b/c): ").lower().strip()

    if answer == item["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. The correct answer was {item['answer']}.\n")

print(f"Quiz complete! Your score: {score}/{len(questions)}")