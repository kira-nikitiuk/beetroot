# File Context Manager class

# Create your own class, which can behave like a built-in function 'open'.
# Also, you need to extend its functionality with counter and logging. 
# Pay special attention to the implementation of '__exit__' method

import os

class FileContextManager:
    def __init__(self, folder_path, filename, mode='w'):
        self.file_path = os.path.join(folder_path, filename)
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

if __name__ == '__main__':
    folder_path = r'C:\Users\Asus\Desktop\beetroot\homework_class\hw_21'

    with FileContextManager(folder_path, 'hello.txt', 'w') as file:
        file.write('Hello, world!')
