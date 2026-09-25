def countdown(number):
    if number == 0:
        print("Blast off!")
        return

    print(number)
    countdown(number - 1)


countdown(5)