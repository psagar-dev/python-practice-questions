#Write a Python program to implement a stack using a list.

class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack:", self.stack)

if __name__ == "__main__":
    stack = Stack()

    stack.push(20)
    stack.push(40)
    stack.push(30)

    stack.pop()
    stack.display()
    print("Top element:", stack.peek())
    stack.display()