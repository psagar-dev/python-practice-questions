#Write a Python program to convert a decimal number to binary

def decimalToBinary(decimal_number):
    if decimal_number == 0:
        return "0"
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number //= 2
    return binary_number

input_number =  int(input("Enter the decimal number: "))


print(f"The binary representation of {input_number} is {decimalToBinary(input_number)}")