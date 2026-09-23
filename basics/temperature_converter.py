def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


choice = input("Convert from Celsius or Fahrenheit? Type C or F: ").upper()
temperature = float(input("Enter the temperature: "))

if choice == "C":
    converted = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C = {converted:.2f}°F")
elif choice == "F":
    converted = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F = {converted:.2f}°C")
else:
    print("Invalid choice. Run the program again and enter C or F.")