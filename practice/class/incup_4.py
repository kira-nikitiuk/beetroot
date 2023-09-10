# Exercise 4: Managing Employees
# Implement an Employee class that represents an employee in a company. 
#Each employee should have variables like name, department, manager, skills, English level and salary.
# English level field should be protected and salary field should be private. 
#Create a Department class that contains employees and methods for adding and 
#removing employees, as well as calculating the average salary for the department.



class Employee:
    def __init__(self, name, department, manager, skills, _english_level, __salary):
        self.name = name 
        self.department = department
        self.manager = manager
        self.skills = skills
        self._english_level = _english_level
        self.__salary = __salary


    def get_salary(self):
        return self.__salary   

    def __str__(self):
        return f"Name: {self.name}, Department: {self.department}, Manager: {self.manager}, Skills: {', '.join(self.skills)}, English Level: {self._english_level}, Salary: {self.__salary}"
  

class Department:
    def __init__(self):
        self.employees = []


    def adding_employee(self, employee):
        self.employees.append(employee)
        #print(self.employees)
        return self.employees


    def removing_employee(self, employee):
        self.employees.remove(employee)
        #print(self.employees)
        return self.employees
    

    def average_salary(self):
        total_salary = sum(emp.get_salary() for emp in self.employees)
        average_salary = total_salary / len(self.employees)
        return average_salary
    

    def __str__(self):
        employees_info = "\n".join(str(emp) for emp in self.employees)
        return f"Department Employees:\n{employees_info}"


employee1 = Employee("Ann", "IT", "first", ["Python"], "B1", 5000)
employee2 = Employee("Bob", "IT", "second", ["C++"], "C1", 4000)

department = Department()
department.adding_employee(employee1)
department.adding_employee(employee2)

print(department)

avg_salary = department.average_salary()
print(f"Average salary in the department: {avg_salary}")

department.removing_employee(employee1)
print(department)

avg_salary = department.average_salary()
print(f"Average salary in the department: {avg_salary}")
 


