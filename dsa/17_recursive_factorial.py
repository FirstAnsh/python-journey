def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


number = int(input("Enter a non-negative whole number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"{number}! = {factorial(number)}")