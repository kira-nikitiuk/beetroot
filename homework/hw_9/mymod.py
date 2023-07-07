import os

def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)

def count_chars(name):
    with open(name, 'r') as file:
        text = file.read()
        return len(text)

def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print("Lines:", lines)
    print("Characters:", chars)

# if __name__ == "__main__":
#     filename = r'C:\Users\Asus\Desktop\beetroot\homework\hw_9\data.txt'  
#     test(filename)
