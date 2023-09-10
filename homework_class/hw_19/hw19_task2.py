# Create your own implementation of a built-in function range, 
# named in_range(), which takes three parameters: 'start', 'end', and optional step. 

def in_range(start, end, step=1):
    current = start
    while current < end if step > 0 else current > end:
        yield current
        current += step

if __name__ == "__main__":
    for num in in_range(1, 10, 2):
        print(num, end = " ") 

    print("\n")

    for num in in_range(10, 1, -2):
        print(num, end = " ") 
