# Extend UnorderedList

# Implement append, index, pop, insert methods for UnorderedList.
# Also implement a slice method, which will take two parameters
# 'start' and 'stop', and return a copy of the list starting at the position 
# and going up to but not including the stop position.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def index(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{data} not found in the list")

    def pop(self, index=None):
        if self.is_empty():
            raise ValueError("List is empty")

        if index is None:
            current = self.head
            if current.next is None:
                self.head = None
                return current.data

            while current.next.next:
                current = current.next
            popped_value = current.next.data
            current.next = None
            return popped_value
        else:
            if index < 0:
                raise ValueError("Index cannot be negative")
            if index == 0:
                popped_value = self.head.data
                self.head = self.head.next
                return popped_value
            current = self.head
            previous = None
            count = 0
            while current and count < index:
                previous = current
                current = current.next
                count += 1
            if not current:
                raise IndexError("Index out of range")
            previous.next = current.next
            return current.data

    def insert(self, index, data):
        if index < 0:
            raise ValueError("Index cannot be negative")

        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            previous = None
            count = 0
            while current and count < index:
                previous = current
                current = current.next
                count += 1
            if count < index:
                raise IndexError("Index out of range")
            previous.next = new_node
            new_node.next = current

    def slice(self, start, stop):
        if start < 0 or stop < 0:
            raise ValueError("Start and stop must be non-negative")
        if start > stop:
            raise ValueError("Start must be less than or equal to stop")

        result = UnorderedList()
        current = self.head
        index = 0
        while current and index < stop:
            if index >= start:
                result.append(current.data)
            current = current.next
            index += 1
        return result

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


my_list = UnorderedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
print(my_list.display())  
print(my_list.index(2))  
my_list.pop(1)
print(my_list.display())  
my_list.insert(1, 2)
print(my_list.display())  
sliced_list = my_list.slice(1, 3)
print(sliced_list.display())  
