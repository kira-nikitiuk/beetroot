# Extend the Queue to include a method called get_from_stack that searches 
# and returns an element e from a queue. Any other element must remain 
# in the queue respecting their order. Consider the case in which the element 
# is not found - raise ValueError with proper info Message

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise ValueError("Queue is empty")

    def get_from_queue(self, target):
        if target not in self.items:
            raise ValueError(f"{target} not found in the queue")
        temp_queue = Queue()
        found = False
        while not self.is_empty():
            item = self.dequeue()
            if item == target:
                found = True
                break
            temp_queue.enqueue(item)
        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())
        if found:
            return target
        else:
            raise ValueError(f"{target} not found in the queue")

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
element = queue.get_from_queue(3)
print(element) 