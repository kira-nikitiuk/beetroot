# Pick your solution to one of the exercises in this module. 
# Design tests for this solution and write tests using unittest library. 


import sys
sys.path.append(r'C:\Users\Asus\Desktop\beetroot\homework_class\hw_16')

from hw16_task1 import Person, Student, Teacher

import unittest

class TestPersonStudentTeacher(unittest.TestCase):
    def test_student_grades_and_average(self):
        student_1 = Student("Bob", 18, "male", "KNU", "MMF", 7, 2500)
        student_1.add_new_grade(66)
        student_1.add_new_grade(89)
        student_1.add_new_grade(99)
        
        self.assertEqual(student_1.grades, [66, 89, 99])
        self.assertEqual(student_1.calculate_the_average_mark_of_student(), 84.66666666666667)
    
    def test_teacher_categories_and_groups(self):
        teacher_1 = Teacher("Mr Johns", 45, "male", "KNU", 10000)
        teacher_1.add_new_category("middle category")
        teacher_1.add_new_category("highest category")
        
        self.assertEqual(teacher_1.categorys, ["middle category", "highest category"])
        
        teacher_1.add_new_group_of_students("mmf")
        teacher_1.add_new_group_of_students("fit")
        teacher_1.add_new_group_of_students("Faculty of Law")
        
        self.assertEqual(teacher_1.groups, ["mmf", "fit", "Faculty of Law"])
        
        teacher_1.delete_group_of_students("fit")
        self.assertEqual(teacher_1.groups, ["mmf", "Faculty of Law"])

if __name__ == '__main__':
    unittest.main()
