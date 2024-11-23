# Write a Python program to calculate compound interest

def calculateCompoundInterest(principal, rate, time,compoundsPerYear):
    rateDecimal = rate / 100
    totalAmount = principal  * ((1 + rateDecimal) / compoundsPerYear) ** (compoundsPerYear * time)
    compoundInterest = totalAmount - principal

    return totalAmount, compoundInterest

try:
    input_principal = float(input("Enter the principal amount: "))
    input_rate = float(input("Enter the annual interest rate (in %): "))
    input_time = float(input("Enter the time period (in years): "))
    input_compounds_per_year = float(input("Enter the number of times interest is compounded per year (n): "))

    totalAmu, comInterest = calculateCompoundInterest(input_principal, input_rate, input_time, input_compounds_per_year)
    print(f"\nTotal amount after {input_time} years: ${totalAmu:.2f}")
    print(f"Compound interest: ${comInterest:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values.")