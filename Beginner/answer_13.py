# Write a Python program to check if a year is a leap year.
def isLeafYear(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
def main():

    input_year = int(input("Enter a year: "))

    if isLeafYear(input_year):
        return (f"{input_year} is a leap year.")
    else:
        return (f"{input_year} is not a leap year.")
    
print(main())