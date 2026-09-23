number = int(input("Enter a whole number: "))

if number > 0:
    print("It is a positive number.")
elif number < 0:
    print("It is a negative number.")
else:
    print("It is zero.")

if number % 2 == 0:
    print("It is even.")
else:
    print("It is odd.")