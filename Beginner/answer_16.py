# Write a Python program to convert Celsius to Fahrenheit.

def celsiusToFahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

try:
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C is equal to {celsiusToFahrenheit(celsius)}°F.")
except ValueError:
    print("Please enter a valid number.")