# Write a program that reads in a sequence of characters and prints them 
# in reverse order, using your implementation of Stack.

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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def reverse_string_using_stack(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)

    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

if __name__ == "__main__":
    user_input = input("Enter a sequence of characters: ")
    reversed_input = reverse_string_using_stack(user_input)
    print("Reversed sequence: ", reversed_input)
