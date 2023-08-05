# Create your own implementation of a built-in function enumerate, 
# named 'with_index', which takes two parameters: 'iterable' and 'start', default is 0. 


class Enumerate:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < len(self.iterable):
            item = self.iterable[self.start]
            self.start += 1
            return item
        else:
            raise StopIteration


my_list = [1, 2, 3, 4, 5]
iterator = Enumerate(my_list)

for item in iterator:
    print(item)
