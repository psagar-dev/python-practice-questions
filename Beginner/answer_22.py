#Write a Python program to calculate simple interest.

def interestCalculate(principal, rate, time):
    return (principal * rate * time)/ 100


try:
    input_principal = float(input("Enter the principal amount: "))
    input_rate = float(input("Enter the annual interest rate (in %): "))
    input_time = float(input("Enter the time period (in years): "))
    interest = interestCalculate(input_principal, input_rate, input_time)

    print(f"The simple interest is: {interest:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values.")