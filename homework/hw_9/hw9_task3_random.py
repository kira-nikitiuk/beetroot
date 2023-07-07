import random
import string

def generate_random_characters(length):
    random_char = lambda: random.choice(string.ascii_letters + string.digits + string.punctuation)
    random_chars = [random_char() for i in range(length)]
    random_string = ''.join(random_chars)
    return random_string

random_chars = generate_random_characters(345)
print(random_chars)

file_path = 'C:\\Users\\Asus\\Desktop\\beetroot\\homework\\hw_9\\data.txt'

with open(file_path, "w") as file:
    for i, char in enumerate(random_chars, 1):
        file.write(char)
        if i % 13 == 0:
            file.write("\n")


