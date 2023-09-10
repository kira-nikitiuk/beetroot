# Exercise 2: Creating a Student Class
# Implement a Student class that represents a student. It should have public attributes like name and grade, and a private attribute for storing the student's ID. Use protected attributes to store a list of courses taken by the student.

class Students:
    def __init__(self, name, grade, _courses: list, __student_id):
        self.name = name
        self.grade = grade
        self.__student_id = __student_id
        self._courses = _courses
    def info_student(self):
        return f"Name: {self.name}\nGrade: {self.grade}\nCourses: {self._courses}"
class Student(Students):
    def __init__(self, name, grade, _courses, __student_id):
        super().__init__(name, grade, _courses, __student_id)
    def add_subject(self, new_subject):
        self._courses.append(new_subject)
        return self._courses
student = Student("John", 8, ["math", "pe", "eng", "ua"], 933)
print(student.add_subject("history"))
print(student.info_student())







