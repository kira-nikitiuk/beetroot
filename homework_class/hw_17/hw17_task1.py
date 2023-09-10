# Task 1
# Method overloading.
# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different. For instance, 
# Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes 
# and performs talk method on input parameter.  

class Animal:
    def talk(self):
        return "say something"

class Dog(Animal):
    def talk(self):
        return "woof woof"

class Cat(Animal):
    def talk(self):
        return "meow"
    
def make_talk(animal):
    if isinstance(animal, Animal):
        return animal.talk()
    else:
        raise ValueError("Invalid animal instance")    

an_1 = Dog()
# print(an_1.talk())
print(make_talk(an_1))   

an_2 = Cat()
# print(an_2.talk())
print(make_talk(an_2))   
 



