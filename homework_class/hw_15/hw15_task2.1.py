# Task 2
# Doggy age
# Create a class Dog with class attribute 'age_factor' equals to 7. Make __init__() which takes values for a dog’s age. Then create a method `human_age` which returns the dog’s age in human equivalent.
#Вот эта формула: эквивалент человеческого возраста = 16 x ln (хронологический возраст собаки) + 31

import math

class Dog:
    def __init__(self, dog_age):
        self.dog_age = dog_age


    def human_age(self):
        human_age_ =  16 * math.log(self.dog_age) + 31
        return human_age_

dog_1 = Dog(2)
print(dog_1.human_age())


