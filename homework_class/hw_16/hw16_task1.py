# Task 1
# School
# Make a class structure in python representing people at school. 
# Make a base class called Person, a class called Student, and another one called Teacher. 
# Try to find as many methods and attributes as you can which belong to different classes, 
# and keep in mind which are common and which are not. 
# For example, the name should be a Person attribute, while salary should only be available to the teacher. 

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender 


class Student(Person):
    def __init__(self, name, age, gender, university, faculty, place_in_the_ranking, scholarship):
        super().__init__(name, age, gender)
        self.university = university
        self.faculty = faculty
        self.grades = []
        self.place_in_the_ranking = place_in_the_ranking
        self.scholarship = scholarship

    def add_new_grade(self, grade):
        self.grades.append(grade)
        return self.grades
    
    def print_grades(self):
        for grade in self.grades:
            print(grade)
    
    def calculate_the_average_mark_of_student(self):
        sum_ = sum(self.grades) / len(list(self.grades))
        return sum_
    

class Teacher(Person): 
    def __init__(self, name, age, gender, university, salary):
        super().__init__(name, age, gender)   
        self.university = university
        self.categorys = []
        self.salary = salary
        self.groups = []

    def add_new_category(self, category):
        self.categorys.append(category)
        return self.categorys
    
    def print_categorys(self):
        for category in self.categorys:
            print(category)

    def add_new_group_of_students(self, group):
        self.groups.append(group)
        return self.groups
    
    def delete_group_of_students(self, group):
        self.groups.remove(group)
        return self.groups
    
    def print_group_of_students(self):
        for group_of_students in self.groups:
            print(group_of_students)
    

student_1 = Student("Bob", 18, "male", "KNU", "MMF", 7, 2500)
student_1.add_new_grade(66)
student_1.add_new_grade(89)
student_1.add_new_grade(99)
student_1.print_grades()
print(student_1.calculate_the_average_mark_of_student())


teacher_1 = Teacher("Mr Johns", 45 , "male", "KNU", 10000)
teacher_1.add_new_category("middle category")
teacher_1.add_new_category("highest category")
teacher_1.print_categorys()

teacher_1.add_new_group_of_students("mmf")
teacher_1.add_new_group_of_students("fit")
teacher_1.add_new_group_of_students("Faculty of Law")
teacher_1.print_group_of_students()
teacher_1.delete_group_of_students("fit")
teacher_1.print_group_of_students()



          