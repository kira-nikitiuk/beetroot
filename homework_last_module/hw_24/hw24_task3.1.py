# Extend the Stack to include a method called get_from_stack that searches 
# and returns an element e from a stack. Any other element must remain on the stack
# respecting their order. Consider the case in which the element is not found - 
# raise ValueError with proper info Message

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty")

    def get_from_stack(self, target):
        if target not in self.items:
            raise ValueError(f"{target} not found in the stack")
        temp_stack = Stack()
        found = False
        while not self.is_empty():
            item = self.pop()
            if item == target:
                found = True
                break
            temp_stack.push(item)
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
        if found:
            return target
        else:
            raise ValueError(f"{target} not found in the stack")

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
element = stack.get_from_stack(3)
print(element)  
