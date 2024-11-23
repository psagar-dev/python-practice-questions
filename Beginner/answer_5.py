
# Write a Python program to check if a string is a palindrome.
def isPalindrome(s):
    s = s.replace(" ","").lower()

    return s == s[::-1]

def main():

    input_string = input("Enter a string: ")

    if isPalindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

main()