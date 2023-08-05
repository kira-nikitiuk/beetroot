# Create your own implementation of a built-in function enumerate, 
# named 'with_index', which takes two parameters: 'iterable' and 'start', default is 0. 


def with_index(iterable, start=0):
    for i, item in enumerate(iterable, start):
        yield i, item

if __name__ == "__main__":
    names = [1, 2, 3, 4, 5]

    for index, name in with_index(names, start=1):
        print(name)
