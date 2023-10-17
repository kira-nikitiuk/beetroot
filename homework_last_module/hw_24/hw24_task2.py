# Write a program that reads in a sequence of characters, 
# and determines whether it's parentheses, braces, and curly brackets are "balanced."

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

def is_balanced(expression):
    stack = Stack()
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in brackets.keys():
            stack.push(char)
        elif char in brackets.values():
            if stack.is_empty() or brackets[stack.pop()] != char:
                return False

    return stack.is_empty()

if __name__ == "__main__":
    user_input = input("Enter a sequence of characters: ")
    if is_balanced(user_input):
        print("Balanced")
    else:
        print("Not balanced")
