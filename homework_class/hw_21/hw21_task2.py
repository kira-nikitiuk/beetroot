# Writing tests for context manager

# Take your implementation of the context manager class from Task 1 and write tests for it.
# Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed. 
# And also, write tests when your class raises errors or you have errors in the runtime context suite.

import unittest
import os
from hw21_task1 import FileContextManager  # Import the class from your module


class TestFileContextManager(unittest.TestCase):
    def setUp(self):
        self.folder_path = 'test_folder'
        os.makedirs(self.folder_path, exist_ok=True)
        self.filename = 'test_file.txt'
        self.file_path = os.path.join(self.folder_path, self.filename)

    def tearDown(self):
        if os.path.exists(self.folder_path):
            for file in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, file)
                os.remove(file_path)
            os.rmdir(self.folder_path)

    def test_file_context_manager_write(self):
        content = 'Hello, world!'
        with FileContextManager(self.folder_path, self.filename, 'w') as file:
            file.write(content)

        with open(self.file_path, 'r') as file:
            written_content = file.read()
            self.assertEqual(written_content, content)

    def test_file_context_manager_read(self):
        content = 'Hello, world!'
        with open(self.file_path, 'w') as file:
            file.write(content)

        with FileContextManager(self.folder_path, self.filename, 'r') as file:
            read_content = file.read()
            self.assertEqual(read_content, content)

    def test_file_context_manager_runtime_error(self):
        with self.assertRaises(RuntimeError):
            with FileContextManager(self.folder_path, self.filename, 'w') as file:
                raise RuntimeError("Simulated runtime error")


if __name__ == '__main__':
    unittest.main()
