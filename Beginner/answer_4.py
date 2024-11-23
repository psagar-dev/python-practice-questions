# Write a Python program to reverse a string.
def reverse_string(rs):
    return rs[::-1]

def main():
    input_string = input("Enter a string: ")

    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

main()