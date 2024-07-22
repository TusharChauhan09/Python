# (d) Inheritance And Polymorphism

# (1) Inheritance


class Animal():            # Base Class

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")

my_animal = Animal()
"""
print(my_animal)
print(my_animal.who_am_i())
print(my_animal.eat())
"""

class Dog(Animal):        # New Class  / Inherted Class
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):    # Oerwrite the old method  OR Updation
        print("I am a Dog")
    
    def bark(self):            # adding new method
        print("WOOF!")

my_dog = Dog()

print(my_dog)
print(my_dog.who_am_i())
print(my_dog.eat())
print(my_dog.bark())