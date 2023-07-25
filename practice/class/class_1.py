class Person:
    def __init__(self, name, age, faculty, grades ):
        self.name = name
        self.age = age
        self.faculty = faculty
        self.grades = grades



    def display_info(self):
        return f"Student: \nName: {self.name} \nAge: {self.age} \nFuculty: {self.faculty} \nGrades: {self. grades}"


    def calculate_average_grade(self):
        pass



person = Person("kira", 100, "mmf", 18)
print(person.display_info())




