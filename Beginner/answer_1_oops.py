import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from input_handler import InputHandler

class NumberCheck:
    def __init__(self, number):
        self.number = number

    def isEvenOrOdd(self):
        if(self.number % 2 == 0):
            return f"The number {self.number} is even."
        else:
            return f"The number {self.number} is odd."

def main():
    number = InputHandler.getUserInputNumber()

    if number  != None:
        numberChecker = NumberCheck(number)
        result = numberChecker.isEvenOrOdd()

        print(result)

if __name__ == "__main__":
    main()