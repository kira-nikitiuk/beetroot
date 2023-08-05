# Pytest fixtures with context manager
# Create a simple function, which performs any logic of your choice with text data, 
# which it obtains from a file object, passed to this function ( def test(file_obj) ). 
# Create a test case for this function using pytest library (Full pytest documentation). 
# Create pytest fixture, which uses your implementation of the context manager to return a file object,
# which could be used inside your function.

import os
import pytest

class FileContextManager:
    def __init__(self, folder_path, filename, mode='r'):
        self.file_path = os.path.join(folder_path, filename)
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


def process_file_content(file_obj):
    content = file_obj.read()
    lines = content.split('\n')
    return [line.strip() for line in lines if line.strip()]


@pytest.fixture
def file_obj_fixture():
    folder_path = 'test_folder'
    os.makedirs(folder_path, exist_ok=True)
    filename = 'test_file.txt'
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'w') as file:
        file.write("Line 1\nLine 2\nLine 3")

    with FileContextManager(folder_path, filename) as file_obj:
        yield file_obj

    os.remove(file_path)
    os.rmdir(folder_path)


def test_process_file_content(file_obj_fixture):
    result = process_file_content(file_obj_fixture)
    assert result == ['Line 1', 'Line 2', 'Line 3']
