scores = []

number_of_scores = int(input("How many scores do you want to enter? "))

for index in range(number_of_scores):
    score = float(input(f"Enter score {index + 1}: "))
    scores.append(score)

total = sum(scores)
average = total / len(scores)

print(f"\nScores: {scores}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Average score: {average:.2f}")