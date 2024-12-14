# Write a Python program to find the factorial of a number.
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from input_handler import InputHandler

class NumberCheck:
    def __init__(self, number):
        self.number = number

    def factorial(self, num=None):
        if num is None:
            num = self.number

        if num == 0 or num == 1:
            return 1
        return num * self.factorial(num - 1)

def main():
    number = InputHandler.getUserInputNumber()

    if number  != None and isinstance(number, int) and number >= 0:
        numberChecker = NumberCheck(number)
        result = numberChecker.factorial()

        print(result)

if __name__ == "__main__":
    main()