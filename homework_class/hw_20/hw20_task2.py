# Write tests for the Phonebook application, which you have implemented in module 1. 
# Design tests for this solution and write tests using unittest library

import json
import unittest
from unittest.mock import patch
import sys
sys.path.append(r'C:\Users\Asus\Desktop\beetroot')  # Добавляем путь к корневой папке проекта

from homework.hw_11.hw11_task2_phonebook import load_phonebook, add_new_entries, search_by_first_name



class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.phonebook_data = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "123456789",
                "country": "USA",
                "city": "New York"
            },
        ]

    def test_load_phonebook_file_not_found(self):
        with self.assertRaises(Exception) as context:
            load_phonebook('non_existent_file.json')
        self.assertEqual(str(context.exception), "Файл не знайдено")

    @patch('builtins.input', side_effect=['Alice', 'Smith', '987654321', 'Canada', 'Toronto'])
    def test_add_new_entries(self, mock_input):
        phonebook_data = self.phonebook_data.copy()
        add_new_entries(phonebook_data)
        self.assertEqual(len(phonebook_data), len(self.phonebook_data) + 1)

    @patch('builtins.input', return_value='John')
    def test_search_by_first_name_found(self, mock_input):
        results = search_by_first_name(self.phonebook_data)
        self.assertTrue(results)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['first_name'], 'John')

    @patch('builtins.input', return_value='NonExistentName')
    def test_search_by_first_name_not_found(self, mock_input):
        results = search_by_first_name(self.phonebook_data)
        self.assertFalse(results)

    # Add more test methods for other functions

if __name__ == '__main__':
    unittest.main()
